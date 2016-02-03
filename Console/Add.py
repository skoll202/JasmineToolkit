'''
Created on Jan 12, 2016

@author: ncarlson
'''
import os

import Course
import Student

def run(data, param):
    layer2 = {}
    returnText = "" 
    
    def addStudent(data,param):
        currentCourse = data['currentCourse']
        
        if currentCourse=="":
            returnText="Current Course not set"
        else:
            fname = raw_input("First Name:")
            lname = raw_input("Last Name:")
            submitPath = raw_input("Submit Path:")
            student = Student.Student(fname,lname,currentCourse)
            if submitPath=="":
                submitPath="C:\\Users\\ncarlson\\Google Drive\\IT3\\TESTING\\"+currentCourse.name+"\\"+lname+","+fname+"\\"
            student.submitPath = submitPath
            student.gradedPath = "C:\\Users\\ncarlson\\Google Drive\\IT3\\TESTING\\Graded\\"+currentCourse.name+"\\"+lname+","+fname+"\\"
            if not os.path.exists(submitPath):
                os.makedirs(submitPath)
            currentCourse.students.append(student)
            returnText = "Student Added Successfully"
            return returnText
    layer2['student'] = addStudent
    
    def addCourse(data,param):
        courses = data['courses']    
        name=raw_input("Course Name:")
        unique = True
        for c in courses:
            if c.name == name:
                returnText = "Name already exists"
                unique = False
                break
        if unique:
            course = Course.Course(name)
            courses.append(course)        
            returnText = "Course Created Successfully"
            return returnText
    layer2['course'] = addCourse
    
    def addAssignment(data,param):
        currentCourse = data['currentCourse']
        assignmentName = ''
        if param!='':
            assignmentName = param
        if assignmentName=='':
            assignmentName = raw_input("Assignment Name:")
        credit = raw_input("Credit:")
        currentCourse.assignments[assignmentName]=int(credit)
        return "Assignment %s added to credit %s successfully" % (assignmentName,credit)
    layer2['assignment'] = addAssignment

        
    words = param.split(' ',1)
    if words[0] in layer2.keys():
        if len(words)<2:
            words.append("")
        returnText = layer2[words[0]](data,words[1])
    else:
        returnText="Command '%s' not found" % words[0]
    return returnText