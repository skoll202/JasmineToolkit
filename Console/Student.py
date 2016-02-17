'''
Created on Jan 6, 2016

@author: ncarlson
'''
import Assignment
import Course

class Student(object):
    '''
    classdocs
    '''
    assignments = []
    firstName = ""
    lastName = ""
    submitPath = ""
    gradedPath = ""
    

    def __init__(self, first, last, course,assignments = []):
        '''
        Constructor
        '''
        self.firstName = first
        self.lastName = last
        self.course = course
        self.assignments = assignments
        
    
        
    def getScoreForCredit(self,credit):
        pass
    
    def getScoreForAssignment(self,assignmentNumber):
        score = 0
        for a in self.assignments:
            if a.number==assignmentNumber:
                score = a.score
                break
        return score
    
    def getSubmitDateForAssignment(self,assignmentNumber):
        date = 0
        for a in self.assignments:
            if a.number==assignmentNumber:
                date = a.dateSubmitted
                break
        return date
    
    def getScoreForNotes(self,credit):
        return self.getScoreForAssignment("Credit%dNotes" % int(credit))
    
    def setScoreForAssignment(self,score, assignmentNumber, credit):
        exists = False
        for a in self.assignments:
            if a.number == assignmentNumber:
                exists = True
                a.score = score
                break
        if not exists:
            assignment = Assignment()
            assignment.number = assignmentNumber
            assignment.score = score
            assignment.credit = credit
            self.assignments.append(assignment)
    def getAssignmentsForCredit(self,credit):
        creditAssignments = []
        for a in self.assignments:
            if str(a.credit)==str(credit):
                creditAssignments.append(a)
        return creditAssignments
    def getAssignmentsDictForCredit(self,credit):
        creditAssignments = {}
        for a in self.assignments:
            if str(a.credit)==str(credit):
                creditAssignments[a.number]=a
        return creditAssignments