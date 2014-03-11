__author__ = 'Sotaya'

import os
import random

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data/')
options = {0: "", 1: "A", 2: "B", 3: "C", 4: "D"}

with open(DATA_PATH + 'quiz_test.dat', 'r') as f:
    quests = f.readlines()
    f.close()

quiz_list = []

for line in quests:
    quiz_list.append(line.split(','))

random.shuffle(quiz_list)

for l in quiz_list:
    answer = str(l[len(l)-1]).rstrip("\n").strip()
    ll = l[:len(l)-1]
    for k, a in enumerate(ll):
        print options[k], a
    user_answer = raw_input("Enter your answer: ")
    if answer == user_answer:
        print "Correct answer"
    else:
        print "Wrong answer"
