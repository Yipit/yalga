#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import time
from django.shortcuts import render
from lunch.models import Person, WeeklyGroup
from django.http import HttpResponse


def index(request):
    Person.create_yipit_people()
    everybody = Person.objects.all()
    return render(request, 'index.html', {
        'everybody': everybody,
        'now': time.time(),
    })


def ajax_generate(request):
    people_ids = json.loads(request.POST['json_list'])
    number_of_groups = request.POST['number_of_groups']

    groups = WeeklyGroup.generate_random(people_ids, int(number_of_groups))
    return HttpResponse(json.dumps([g.to_dict() for g in groups]))


def html_group_page(request, code):
    self = WeeklyGroup.objects.get(code=code)
    return render(request, 'group.html', {
        'group': self
    })



def generated_groups(request, group_codes):
    group_codes = group_codes.split('|')
    groups = WeeklyGroup.objects.filter(code__in=group_codes)

    return render(request, 'generated.html', {
        'groups': groups,
    })
