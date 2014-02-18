__author__ = 'Sotaya'

import os
import random

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data/')

with open(DATA_PATH + 'quiz_test.dat', 'r') as f:
    quests = f.readlines()
    f.close()

quiz_list = []

for line in quests:
    quiz_list.append(line.split(','))

random.shuffle(quiz_list)

for l in quiz_list:
    answer = l[len(l)-1].replace('\n', '')
    for k, a in enumerate(l):
        print k, a
    break