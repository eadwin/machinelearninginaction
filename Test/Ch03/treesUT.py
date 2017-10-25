#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'Decision Tree Unit Test'
__author__ = 'Eadwin'
__mtime__ = 'Otc 24 2017'


# code is far away from bugs with the god animal protecting
#
#         ┌─┐       ┌─┐
#      ┌──┘ ┴───────┘ ┴──┐
#      │                 │
#      │       ───       │
#      │  ─┬┘       └┬─  │
#      │                 │
#      │       ─┴─       │
#      │                 │
#      └───┐         ┌───┘
#          │         │
#          │         │
#          │         │
#          │         └──────────────┐
#          │                        │
#          │                        ├─┐
#          │                        ┌─┘
#          │                        │
#          └─┐  ┐  ┌───────┬──┐  ┌──┘
#            │ ─┤ ─┤       │ ─┤ ─┤
#            └──┴──┘       └──┴──┘
#
#               神兽保佑，永无Bug！
"""

import trees


dataSet, labels = trees.createDataSet()
print dataSet
print labels

print(trees.splitDataSet(dataSet, 0, 1))
print(trees.splitDataSet(dataSet, 1, 1))
print dataSet[:1]
a = {}
a = dataSet[:1]
a.append(dataSet[2:])
print a

shannonEnt = trees.calcShannonEnt(dataSet)
print shannonEnt

