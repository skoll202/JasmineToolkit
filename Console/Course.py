'''
Created on Jan 6, 2016

@author: ncarlson
'''

from __future__ import division

class Course(object):
    '''
    classdocs
    '''
    name = ""
    
    def getAssignmentsForCredit(self,credit):
        assignments = []
        for a in self.assignments.keys():
            if self.assignments[a]==credit:
                assignments.append(a)
            elif self.assignments[a]=="%d" % credit:
                assignments.append(a)
        return assignments
    def getScoresForCredit(self,credit):
        scores = {}
        creditAssignments = self.getAssignmentsForCredit(credit)        
        for s in self.students:
            scores[s.lastName+","+s.firstName] = 0
            studentAssignments = s.getAssignmentsForCredit("%d"%credit)
            studentAssignmentPoints = 0
            studentNotesPoints = 0
            studentProjectPoints = 0
            assignmentPoints=0
            notesPoints=0
            projectPoints=0
            for a in studentAssignments:
                if "Notes" in a.number:
                    studentNotesPoints+=int(a.score)
                elif "Project" in a.number:
                    studentProjectPoints+=int(a.score)
                else:
                    studentAssignmentPoints+=int(a.score)
            for a in creditAssignments:
                if "Notes" in a:
                    notesPoints+=100
                elif "Project" in a:
                    projectPoints+=100
                else:
                    assignmentPoints+=100
            if assignmentPoints>0:
                if notesPoints>0:
                    if projectPoints==0:
                        assignmentPercentage = studentAssignmentPoints/assignmentPoints*.7                        
                        notesPercentage = studentNotesPoints/notesPoints*.3
                        scores[s.lastName+","+s.firstName]=assignmentPercentage+notesPercentage
                    else:
                        assignmentPercentage = studentAssignmentPoints/assignmentPoints*.4
                        notesPercentage = studentNotesPoints/notesPoints*.3
                        projectPercentage = studentProjectPoints/projectPoints*.3
                        scores[s.lastName+","+s.firstName]=assignmentPercentage+notesPercentage+projectPercentage
                else:
                    if projectPoints==0:
                        scores[s.lastName+","+s.firstName]=studentAssignmentPoints/assignmentPoints
                    else:
                        assignmentPercentage = studentAssignmentPoints/assignmentPoints*.7
                        projectPercentage = studentProjectPoints/projectPoints*.3
                        scores[s.lastName+","+s.firstName]=assignmentPercentage+projectPercentage
            else:
                scores[s.lastName+","+s.firstName]=-1
        return scores
  

    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        self.assignments = {}
        self.students = []
        self.notesWeight = .3
        self.projectWeight = .3
        
    