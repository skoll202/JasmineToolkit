'''
Created on Jan 11, 2016

@author: ncarlson
'''

import Course

def run(data, param):
    layer2 = {}
    returnText = "" 
    
    def removeStudent(data,param):
        currentCourse = data['currentCourse']
        i=1
        for s in currentCourse.students:
            print("%d.%s" % (i,s.firstName+" "+s.lastName))
            i+=1
        number=int(raw_input("Student Number:"))
        if number>0 and number<=len(currentCourse.students):            
            student = currentCourse.students[number-1]
            currentCourse.students.remove(student)
            returnText="Student Removed Successfully"
        else:
            returnText="Invalid Selection.  No Students Removed"
        return returnText
    layer2['student'] = removeStudent
    
    def removeCourse(data,param):        
        currentCourse = data['currentCourse']
        courses = data['courses']
        i=1
        for s in courses:
            print("%d.%s" % (i,s.name))
            i+=1
        number=int(raw_input("Course Name:"))
        if number>0 and number<=len(courses): 
            course = courses[number-1]        
            courses.remove(course)
            if currentCourse==course.name:
                currentCourse=""        
            returnText = "Course Removed Successfully"
        else:
            returnText = "Invalid Course Selection"
        return returnText
    layer2['course'] = removeCourse
    
    def removeAssignment(data,param):
        currentCourse = data['currentCourse']
        words = param.split(' ',1)
        if words[0]!="":
            assignmentNumber = param
            if assignmentNumber in currentCourse.assignments.keys():
                credit = currentCourse.assignments[assignmentNumber]
                currentCourse.assignments[assignmentNumber]=-1
                returnText = "Assignment %s removed from credit %d" % (assignmentNumber,credit)
            else:
                returnText = "Assignment not found."
        else:
            returnText = "No assignment number given."            
        return returnText            
    layer2['assignment'] = removeAssignment
    
    words = param.split(' ',1)
    if words[0] in layer2.keys():
        if len(words)<2:
            words.append("")
        returnText = layer2[words[0]](data,words[1])
    else:
        returnText="Command '%s' not found" % words[0]
    return returnText