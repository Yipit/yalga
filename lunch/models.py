#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
import hashlib
import random

from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse
from itertools import izip_longest as zip_longest


def weighted_randomness(restaurants, total_restaurants):
    l = sorted((random.random() * x.score, x) for x in restaurants)
    return [x for x in restaurants[-total_restaurants:]]


def group_by(n, iterable):
    groups = [[] for _ in range(n)]

    for current, item in enumerate(iterable):
        group_id = current % n
        groups[group_id].append(item)

    return groups



class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()
    yelp_url = models.URLField()

    def __unicode__(self):
        return "Restaurant: {0} [{1}]".format(self.name, self.score)

    def to_dict(self):
        return {
            'name': self.name,
            'score': self.score,
            'yelp_url': self.yelp_url,
        }

    @classmethod
    def create_restaurants(Person):
        for name, score in settings.RESTAURANTS:
            Restaurant.objects.get_or_create(name=name, score=score)


class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=False, blank=True)

    def __unicode__(self):
        return "{0} <{1}>".format(self.name, self.email)

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
        }

    @classmethod
    def create_yipit_people(Person):
        for name in settings.PEOPLE:
            Person.objects.get_or_create(name=name)

    class Meta:
        verbose_name_plural = 'people'

class WeeklyGroup(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Person)
    code = models.CharField(max_length=44, unique=True)
    winning_restaurant = models.ForeignKey(Restaurant, null=True, blank=True)
    date = models.DateField()
    email_sent_at = models.DateTimeField(null=True, blank=True)
    round1 = models.ManyToManyField(Restaurant, related_name='groups_round1')
    round2 = models.ManyToManyField(Restaurant, related_name='groups_round2')
    round3 = models.ManyToManyField(Restaurant, related_name='groups_round3')

    def save(self, *args, **kw):
        ret = super(WeeklyGroup, self).save(*args, **kw)
        all_restaurants = list(Restaurant.objects.all())

        if self.round1.count() == 0:
            for venue in weighted_randomness(all_restaurants, 3):
                self.round1.add(venue)
                all_restaurants.remove(venue)

        if self.round2.count() == 0:
            for venue in weighted_randomness(all_restaurants, 3):
                self.round2.add(venue)
                all_restaurants.remove(venue)

        if self.round3.count() == 0:
            for venue in weighted_randomness(all_restaurants, 3):
                self.round3.add(venue)
                all_restaurants.remove(venue)

        return ret

    def __unicode__(self):
        return "Group for {0}".format(self.date)

    @classmethod
    def generate_random(cls, people_going, total_groups):
        previous_group_ids = cls.objects.filter(date=datetime.now().date()).delete()
        participants = list(Person.objects.filter(id__in=people_going))
        random.shuffle(participants)

        groups = []
        for index, _people in enumerate(group_by(total_groups, participants)):
            people = filter(bool, _people)
            group = WeeklyGroup.objects.create(
                name=settings.GROUP_NAMES[index],
                code=cls.generate_code(time.time(), people),
                date=datetime.now().date(),
            )
            map(group.members.add, people)
            groups.append(group)

        return groups

    @classmethod
    def generate_code(self, *salt):
        return hashlib.sha1(str(salt)).hexdigest()

    def to_dict(self):
        return {
            'members': [member.to_dict() for member in self.members.all()],
            'code': self.code,
            'winning_restaurant': self.winning_restaurant and self.winning_restaurant.to_dict() or None,
            'name': self.name,
            'date': self.date.isoformat(),
            'url': self.get_url(),
            'id': self.id
        }
    def get_url(self):
        return reverse('group_page', kwargs={'code': self.code})
