'''
Created on Jan 6, 2016

@author: ncarlson
'''
import time
import datetime

class Assignment(object):
    '''
    classdocs
    '''
    
    number = ""
    credit = -1
    score = 0


    def __init__(self,number="",credit="",score="",dueDate = datetime.date(2199,1,1)):
        '''
        Constructor
        '''
        self.number=number
        self.credit = credit
        self.score = score
        self.dateSubmitted = datetime.date.today()
        if isinstance(dueDate,datetime.date):
            self.dueDate = dueDate
        else:
            split = dueDate.split('/')
            self.dueDate = datetime.date(int(split[2]),int(split[0]),int(split[1]))
            
                