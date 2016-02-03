'''
Created on Jan 14, 2016

@author: ncarlson
'''

import FileManager
import Assignment
from Console import PDFManager
from _ast import Num
import os
import sys
import datetime

def run(data, param):
    layer2 = {}
    returnText = "" 
    
    def checkForDueAssignments(data,param):
        currentCourse = data['currentCourse']
        assignments = currentCourse.assignments
        for a in currentCourse.assignments.keys():
            if assignments[a].dueDate<datetime.date.today():
                for s in currentCourse.students:
                    isSubmitted = False
                    for sa in s.assignments:
                        if sa.number==a:
                            isSubmitted = True
                            break
                    if not isSubmitted:
                        s.assignmentNotSubmitted()
    
    def scanFiles(data,param):
        currentCourse = data['currentCourse']
        students = currentCourse.students
        returnText = ""
        for s in students:
            
            count = 0
            path = s.gradedPath
            
            files = FileManager.getPDFFiles(path)
            printCount = 1
            
            for f in files:
                sys.stdout.write("\rScanning file %d of %d for %s %s\r\n" % (printCount,len(files),s.firstName,s.lastName))
                sys.stdout.flush()
                printCount+=1
                
                filename = os.path.split(f)[1]
                num = filename.split("-")[0]
                new = True
                for a in s.assignments:
                    if a.number == num:
                        new = False
                if filename.find("packet")!=-1:
                    new=False
                if new:
                    count+=1
                    text = PDFManager.getStr(f)
                    score = PDFManager.getScore(text = text)
                    assignment = Assignment.Assignment()
                    assignment.score = score
                    assignment.number = num
                    try:
                        assignment.credit = currentCourse.assignments[num]
                    except:
                        assignment.credit = -1
                    s.assignments.append(assignment)
                    if assignment.dateSubmitted<currentCourse.assignments[num].dueDate:
                        s.assignmentSubmittedOnTime()
            returnText+="Added %d grades for %s %s \r\n" % (count,s.firstName,s.lastName)
        currentCourse.students = students
        data['currentCourse'] = currentCourse
        for i in range(1,16):
            for s in students:
                path = s.gradedPath+"%d\\"%i
                destPath = s.gradedPath
                files = FileManager.getPDFFiles(path)
                for f in files:
                    filename = os.path.split(f)[1]
                    if filename.find("packet")!=-1:
                        files.remove(f)
                if (len(files)>0):
                    PDFManager.merge(files, destPath+"packet%d.pdf"%i)
        checkForDueAssignments(data, param)
        return returnText
                    
    
    layer2['files'] = scanFiles
    
    words = param.split(' ',1)
    if words[0] in layer2.keys():
        if len(words)<2:
            words.append("")
        returnText = layer2[words[0]](data,words[1])
    else:
        returnText="Command '%s' not found" % words[0]
    return returnText