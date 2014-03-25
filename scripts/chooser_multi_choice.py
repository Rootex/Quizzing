__author__ = 'Sotaya'

import os
import random

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data/')


class Quiz:
    options = {0: "", 1: "A", 2: "B", 3: "C", 4: "D"}

    def __init__(self, path='./'):
        try:
            with open(path + 'quiz_test_multi_choice.dat', 'r') as quiz_file:
                quests = quiz_file.readlines()
                self.quiz_list = [line.split(',') for line in quests]
        except IOError:
            print "Cannot find quiz_test_multi_choice.dat in the given path!"

    def check(self):
        test = self.quiz_list[:]
        random.shuffle(test)

        for question in test:
            answer = str(question[-1]).strip()
            for k, a in enumerate(question[:-1]):
                print Quiz.options[k], a
            user_answer = raw_input("Enter your answer: ")
            if answer == user_answer:
                print "Correct answer"
            else:
                print "Wrong answer"
