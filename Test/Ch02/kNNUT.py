#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'kNNUT'
__author__ = 'Eadwin'
__mtime__ = 'Otc 20 2017'

kNN: k Nearest Neighbors unit test

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

from numpy import *
import kNN
import matplotlib
import matplotlib.pyplot as plt


# datingDataMat, datingLabels = kNN.file2matrix('datingTestSet.txt')
# print (datingDataMat)
# print (datingLabels[0:20])
#
# normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
# print (normMat)
# print (ranges)
# print (minVals)
#
# kNN.datingClassTest('datingTestSet.txt')
#
# kNN.classifyPerson()
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
# ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0*array(datingLabels), \
#            15.0*array(datingLabels))
# ax.axis([-2, 25, -0.2, 2.0])
# plt.xlabel('Percentage of Time Spent Playing Video Games')
# plt.ylabel('Liters of Ice Cream Consumed Per Week')
# plt.show()


#imgVect = kNN.img2vector('testDigits/0_0.txt')
#print(imgVect[0,1])

kNN.handwritingClassTest()
