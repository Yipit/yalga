#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sure import scenario
from lunch.models import Person, WeeklyGroup


def cleanup(context):
    for Model in [Person, WeeklyGroup]:
        Model.objects.all().delete()

clean_test_db = scenario(cleanup, cleanup)


@clean_test_db
def test_groups_can_be_created_randomly(context):
    ("Groups should be created from a certain number")

    # Given there are 4 people in the databse
    people_going = [
        Person.objects.create(name='Unaiz', email='unaiz@yipit.com').id,
        Person.objects.create(name='Sean', email='sean@yipit.com').id,
        Person.objects.create(name='Jordan', email='jordan@yipit.com').id,
        Person.objects.create(name='Jim', email='jim@yipit.com').id,
    ]
    # When I create groups randomly
    groups = WeeklyGroup.generate_random(people_going, total_groups=2)

    # Then there should be 2 groups
    groups.should.have.length_of(2)
    g1, g2 = groups

    # And each group has 2 people
    g1.members.count().should.equal(2)
    g2.members.count().should.equal(2)


@clean_test_db
def test_groups_can_be_created_with_odd_number_of_people(context):
    ("We should be able to create groups even with an odd number of members")

    # Given there are 4 people in the databse
    people_going = [
        Person.objects.create(name='Unaiz', email='unaiz@yipit.com').id,
        Person.objects.create(name='Sean', email='sean@yipit.com').id,
        Person.objects.create(name='Jordan', email='jordan@yipit.com').id,
        Person.objects.create(name='Jim', email='jim@yipit.com').id,
        Person.objects.create(name='Vin', email='vin@yipit.com').id,
    ]
    # When I create groups randomly
    groups = WeeklyGroup.generate_random(people_going, total_groups=2)

    # Then there should be 2 groups
    groups.should.have.length_of(2)
    g1, g2 = groups

    # And each group has 3 people
    g1.members.count().should.equal(3)
    g2.members.count().should.equal(2)
