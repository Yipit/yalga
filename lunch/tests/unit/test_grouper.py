#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from lunch.models import group_by


def test_grouping():
    group_by(2, [1, 2, 3, 4, 5, 6, 7]).should.equal([
        [1, 3, 5, 7], [2, 4, 6]
    ])
