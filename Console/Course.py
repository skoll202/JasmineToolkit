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
    def addDefaultAssignments(self):
        assignments = {
            "1.2.2": 1,
            "1.2.4": 1,
            "1.3.5": 1,
            "1.3.7": 1,
            "1.4.5": 1,
            "3.1.3": 1,
            "3.2.5": 1,
            "3.2.6": 1,
            "3.3.5": 1,
            "3.3.6": 1,
            "3.4.7": 1,
            "3.4.8": 1,
            "3.4.9": 1,
            "Credit1Notes":1 ,
            
            "3.5.12": 2,
            "3.5.13": 2,
            "3.5.14": 2,
            "3.6.9": 2,
            #"3.7.4": 2,
            "3.7.5": 2,
            "3.8.5": 2,
            "3.8.6": 2,
            #"3.9.7": 2,
            "3.9.8": 2,
            "3.10.3": 2,
            "Credit2Notes":2 ,
            
            "2.1.8":2 ,
            "2.2.6":2 ,
            "2.4.6":2 ,
            "2.3.3":2 ,
            "2.4.7":2 ,
            "2.5.3":2 ,
            

            "4.1.5": 3,
            "4.1.6": 3,
            #"4.2.4": 3,
            #"4.2.5": 3,
            #"4.3.5": 3,
            "4.3.6": 3,
            "4.4.3": 3,
            "4.4.4": 3,
            #"4.5.9": 3,
            #"4.5.10": 3,
            "4.5.11": 3,
            #"4.5.12": 3,
            "4.5.14": 3,
            "4.5.17": 3,
            "4.5.18": 3,
            "4.6.6": 3,
            "4.6.7": 3,
            "Credit3Notes":3 ,

            
            "Credit4Notes":4 ,

            "5.1.5":5 ,
            "5.2.3": 5,
            "5.2.4":5 ,
            "5.3.4": 5,
            "5.3.5":5 ,
            "5.4.4": 5,
            "5.4.5":5 ,
            "5.5.5":5 ,
            "5.6.8": 5,
            "5.7.7": 5,
            "5.7.9": 5,
            "5.7.12": 5,
            "5.8.5": 5,
            "5.8.6": 5,
            "5.8.7": 5,
            "5.9.4": 5,
            "5.9.5":5 ,
            "5.10.4": 5,
            "5.10.5": 5,
            "Credit5Notes":5 ,

            "6.1.6":6 ,
            "6.2.7": 6,
            "6.3.6":6 ,
            "6.4.4":6 ,
            "6.5.4": 6,
            "6.6.5": 6,
            "6.6.6": 6,
            "6.6.7": 6,
            "6.7.3":6 ,
            "Credit6Notes":6 ,

            "6.9.6":7 ,
            "6.8.3":7 ,
            "6.9.7":7 ,
            "6.9.8":7 ,
            "6.10.4":7 ,
            "6.11.4":7 ,
            "6.11.5":7 ,
            "6.11.7":7 ,
            "6.11.8":7 ,
            "6.12.6":7 ,
            "6.12.7":7 ,
            "6.13.3":7 ,
            "6.13.4":7 ,
            "6.13.5":7 ,
            "6.13.9":7 ,
            "6.14.3":7 ,
            "Credit7Notes":7 ,

            "7.1.9": 8,
            "7.1.10":8 ,
            "7.2.4": 8,
            "7.2.5": 8,
            "7.3.4": 8,
            "7.3.5":8 ,
            "7.4.4": 8,
            "7.4.5": 8,
            "7.4.6":8 ,
            "7.5.3":8 ,
            "8.2.7":8 ,
            "8.1.6":8 ,
            "8.3.4": 8,
            "8.3.5": 8,
            "8.3.6":8 ,
            "8.4.8": 8,
            "8.4.9":8 ,
            "Credit8Notes":8 ,

            "9.1.8":9 ,
            "9.2.4":9 ,
            "9.3.4":9 ,
            "9.4.4":9 ,
            "9.4.7":9 ,
            "9.5.7":9 ,
            "9.5.8":9 ,
            "9.6.4": 9,
            "9.6.5":9 ,
            "9.7.4": 9,
            "9.7.6":9 ,
            "9.8.4": 9,
            "9.8.7": 9,
            "9.8.8":9 ,
            "9.9.4": 9,
            "9.9.5": 9,
            "Credit9Notes":9 ,

            "10.1.3":10 ,
            "10.2.6":10 ,
            "10.3.3":10 ,
            "10.3.6":10 ,
            "10.4.4":10 ,
            "10.5.7":10 ,
            "10.5.8":10 ,
            "11.1.5":10 ,
            "11.2.6":10 ,
            "11.2.11":10 ,
            "11.2.12":10 ,
            "11.3.4":10 ,
            "11.3.5":10 ,
            "11.4.6":10 ,
            "11.4.7":10 ,
            "11.5.3":10 ,
            "Credit10Notes":10,

            "12.1.3": 11,
            "12.1.4": 11,
            "12.2.6": 11,
            "12.2.7": 11,
            "12.3.3": 11,
            "12.4.4": 11,
            "12.4.5": 11,
            "12.5.7": 11,
            "12.6.5": 11,
            "12.6.10": 11,
            "12.7.4": 11,
            "12.7.5": 11,
            "12.8.5": 11,
            "12.9.6": 11,
            "12.9.7": 11,
            "12.10.4": 11,
            "12.10.5": 11,
            "Credit11Notes": 11,

            "13.1.2": 12,
            "13.1.3": 12,
            "13.1.6": 12,
            "13.1.7": 12,
            "13.1.11": 12,
            "13.1.12": 12,
            "13.1.13": 12,
            "13.2.3": 12,
            "13.2.4": 12,
            "13.2.5": 12,
            "13.3.5": 12,
            "13.4.8": 12,
            "13.4.9": 12,
            "13.4.10": 12,
            "13.5.8": 12,
            "13.5.9": 12,
            "13.5.10": 12,
            "Credit12Notes": 12,

            "13.6.5": 13,
            "13.7.8": 13,
            "13.7.9": 13,
            "13.7.10": 13,
            "13.7.11": 13,
            "13.7.12": 13,
            "13.8.3": 13,
            "13.9.7": 13,
            "13.10.5": 13,
            "13.11.4": 13,
            "13.11.5": 13,
            "13.11.6": 13,
            "Credit13Notes": 13}
        return assignments

    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        self.assignments = self.addDefaultAssignments()
        self.students = []
        self.notesWeight = .3
        self.projectWeight = .3
        
    