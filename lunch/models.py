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
    members = models.ManyToManyField(Person)
    code = models.CharField(max_length=44, unique=True)
    winning_restaurant = models.ForeignKey(Restaurant, null=True, blank=True)
    date = models.DateField()
    email_sent_at = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return "Group for {0}".format(self.date)

    @classmethod
    def generate_random(self, people_going, total_groups):
        participants = list(Person.objects.filter(id__in=people_going))
        random.shuffle(participants)

        groups = []
        for _people in group_by(total_groups, participants):
            people = filter(bool, _people)
            group = WeeklyGroup.objects.create(
                code=self.generate_code(time.time(), people),
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
            'date': self.date.isoformat(),
            'url': self.get_url(),
            'id': self.id
        }
    def get_url(self):
        return reverse('group_page', kwargs={'code': self.code})
