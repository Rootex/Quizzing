__author__ = 'Sotaya'

import os
import random
import tts
import json

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data/')


class MutiChoice:
    options = {0: "", 1: "A", 2: "B", 3: "C", 4: "D"}
    stats = {"questions_answered": 0, "correct_answer": 0}

    def __init__(self, path='./'):
        self.talk = tts.Reader()
        try:
            with open(path + 'quiz_test_multi_choice.dat', 'r') as quiz_file:
                quests = quiz_file.readlines()
                self.quiz_list = [line.split(',') for line in quests]
        except IOError:
            print("Cannot find quiz_test_multi_choice.dat in the given path!")

    def check(self):
        test = self.quiz_list[:]
        random.shuffle(test)

        for question in test:
            answer = str(question[-1]).strip()
            for k, a in enumerate(question[:-1]):
                print(MutiChoice.options[k], a)
                self.talk.speak(MutiChoice.options[k])
                self.talk.speak(a)
            user_answer = input("Enter your answer: ")
            if answer == user_answer:
                print("Correct answer")
                self.talk.speak("Correct answer")
                self.stats["questions_answered"] += 1
                self.stats["correct_answer"] += 1
            elif user_answer == "":
                pass
            else:
                print("Wrong answer")
                self.talk.speak("Wrong answer")
                self.stats["questions_answered"] += 1
        with open(DATA_PATH+'stats.json', 'a') as f:
            json.dump(self.stats, f)


class Essay:
    def __init__(self, path='./'):
        self.talk = tts.Reader()
        try:
            with open(path + 'quiz_essay.dat', 'r') as quiz_file:
                quests = quiz_file.read()
                self.seg = quests.split('@')
                self.quiz_list = {}
                for i in self.seg:
                    self.quiz_list[i.split(',')[0]] = i.split(',')[1]
        except IOError:
            print("Cannot find quiz_test_multi_choice.dat in the given path!")

    def check(self):
        test = self.quiz_list
        try:
            for key, question in enumerate(test):
                print(question + '\n')
                response = input("To show answer enter (show) or (skip) to continue: ")
                if response.lower() == "show":
                    print(test[question] + '\n')
                elif response.lower() == "skip":
                    pass
                else:
                    raise ValueError("Wrong response")
        except ValueError as e:
            print(e.message)
            raise ValueError()

if __name__ == '__main__':
    obj = MutiChoice(DATA_PATH)
    obj.check()