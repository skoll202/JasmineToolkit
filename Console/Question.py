'''
Created on Feb 19, 2016

@author: ncarlson
'''

from random import shuffle

class Question(object):
    '''
    classdocs
    '''


    def __init__(self, question,incorrectAnswers=[],correctAnswers=[],type='multipleChoice',objective=-1):
        '''
        Constructor
        '''
        self.question = question
        self.incorrectAnswers = incorrectAnswers
        self.correctAnswers = correctAnswers
        self.type = type
        self.objective = objective
    
    def getRandomAnswers(self):
        answers = self.incorrectAnswers+self.correctAnswers
        shuffle(answers)
        return answers
    
    def isCorrect(self,answers):
        correct=0
        for a in answers:
            if a in self.correctAnswers:
                correct+=1
        if correct==len(self.correctAnswers):
            return True
        else:
            return False
        