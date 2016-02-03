'''
Created on Jan 11, 2016

@author: ncarlson
'''

import math
import time

def run(data, param):
    layer2 = {}
    returnText = "" 
    def printStudents(data,param):
        returnText = ""
        currentCourse = data['currentCourse']        
        for s in currentCourse.students:
            returnText+=s.lastName+","+s.firstName+" - %d xp\r\n" % s.xp
        return returnText
    layer2['students'] = printStudents
    
    def printCourses(data,param):
        courses = data['courses']
        returnText = ""
        for course in courses:
            returnText+=course.name+"\r\n"
        return returnText
    layer2['courses'] = printCourses
    
    def printCurrent(data,param):
        layer3={}
        returnText=""
        def printCurrentCourse(data,param):
            returnText=""
            currentCourse = data['currentCourse'].name
            returnText=currentCourse
            return returnText
        layer3['course'] = printCurrentCourse
        
        words = param.split(' ',1)
        if words[0] in layer3.keys():
            if len(words)<2:
                words.append("")
            returnText = layer3[words[0]](data,words[1])  
        return returnText      
    layer2['current'] = printCurrent
    
    def printCredit(data,param):
        words = param.split(' ',1)
        returnText = ""
        currentCourse = data['currentCourse']
        students = currentCourse.students
        scores = currentCourse.getScoresForCredit(int(words[0]))
        for s in students:
            score = scores[s.lastName+","+s.firstName]
            returnText+="%s,%s - %d\r\n" % (s.lastName,s.firstName,math.ceil(score*100))
        return returnText
    layer2['credit'] = printCredit
            
    def printGrades(data,param):
        currentCourse = data['currentCourse']
        returnText = ""
        for credit in range(1,15):
            returnText+="Credit %d:\r\n"%credit
            scores = currentCourse.getScoresForCredit(credit)
            for s in scores.keys():
                returnText+="%s:%d \r\n" % (s,math.ceil(scores[s]*100))
            returnText+="\r\n"
        return returnText
    layer2['grades'] = printGrades
    
    def printCourse(data,param):
        layer2 = {}
        
        def printCourseAssignments(data,param):
            currentCourse = data['currentCourse']
            returnText=''
            for c in range(1,16):
                assignments = currentCourse.getAssignmentObjectsForCredit(c)
                returnText+="Credit %d\r\n" % c
                for a in assignments:
                    returnText+="%s - Due %s\r\n" % (a.number,a.dueDate.isoformat())
                returnText+="\r\n"
            return returnText
        layer2['assignments'] = printCourseAssignments
        
        words = param.split(' ',1)
        if words[0] in layer2.keys():
            if len(words)<2:
                words.append("")
            returnText = layer2[words[0]](data,words[1])
        else:
            returnText="Command '%s' not found" % words[0]
        return returnText
    layer2['course'] = printCourse
    
    words = param.split(' ',1)
    if words[0] in layer2.keys():
        if len(words)<2:
            words.append("")
        returnText = layer2[words[0]](data,words[1])
    else:
        returnText="Command '%s' not found" % words[0]
    return returnText

    




