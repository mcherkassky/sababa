__author__ = 'mcherkassky'
import os
import json

f = open('distribution.txt', 'rb')

distribution = {}
for line in f.readlines():
    line = line.replace('\n', '').split(':::')
    distribution[line[0]] = line[1]

