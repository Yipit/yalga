#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from lunch.models import Restaurant, WeeklyGroup, Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    list_filter = ('name', 'email',)

admin.site.register(Person, PersonAdmin)

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'score', 'yelp_url',)
    list_filter = ('name', 'score', 'yelp_url',)

    ordering = ('-score',)

admin.site.register(Restaurant, RestaurantAdmin)

class WeeklyGroupAdmin(admin.ModelAdmin):
    list_display = ('date', 'winning_restaurant', 'email_sent_at',)

admin.site.register(WeeklyGroup, WeeklyGroupAdmin)
