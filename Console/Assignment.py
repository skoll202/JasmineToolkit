'''
Created on Jan 6, 2016

@author: ncarlson
'''
import time

class Assignment(object):
    '''
    classdocs
    '''
    
    number = ""
    credit = -1
    score = 0


    def __init__(self,number="",credit="",score=""):
        '''
        Constructor
        '''
        self.number=number
        self.credit = credit
        self.score = score
        self.dateSubmitted = time.strftime("%c")
        