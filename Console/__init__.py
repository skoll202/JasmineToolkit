import os
import pickle

import Course
import Student
import Assignment

import Print
import Remove
import Add
import Set
import Save
import Quit
import Sort
import Scan
import Clear
import Grade

command = {}
courses = []
currentCourse=""
dataPath = "C:\\Users\\ncarlson\\Google Drive\\IT3\\TESTING\\"

returnText = ""

def getCurrentCourse():
    global currentCourse
    if currentCourse == "":
        return "FAIL"
    else:
        for c in courses:
            if c.name==currentCourse:
                return c
        
def setCurrentCourse(course):
    global currentCourse
    currentCourse = course

def getInput():
    return raw_input(">")

command['quit'] = Quit.run

command['add'] = Add.run

command['set'] = Set.run

command['remove'] = Remove.run

command['print'] = Print.run

command['save'] = Save.run

command['sort'] = Sort.run

command['scan'] = Scan.run

command['clear'] = Clear.run

command['grade'] = Grade.run

def processInput(param):
    words = param.split(' ',1)
    data = {}
    data['currentCourse'] = getCurrentCourse()
    data['courses'] = courses
    data['dataPath'] = dataPath
    if words[0] in command.keys():
        if words[0]!="set" and words[0]!="add" and words[0]!="quit":
            if data['currentCourse']!="FAIL":
                if len(words)<2:
                    words.append("")
                print(command[words[0]](data,words[1]))
                try:
                    setCurrentCourse(data['currentCourse'].name)
                except:
                    pass
            else:
                print("You must set a current course before proceeding.")
        else:
            if len(words)<2:
                words.append("")
            print(command[words[0]](data,words[1]))
            try:
                setCurrentCourse(data['currentCourse'].name)
            except:
                pass
    else:
        print "Command %s not found." % words[0]
    

try:
    courses = pickle.load(open("C:\\Users\\ncarlson\\Google Drive\\IT3\\TESTING\\courses.p"))
    settings = pickle.load(open("C:\\Users\\ncarlson\\Google Drive\\IT3\\TESTING\\settings.p"))
    if 'currentCourse' in settings.keys():
        for c in courses:
            if settings['currentCourse']==c.name:
                currentCourse = c.name
                break
    
except Exception:
    courses = []

assignments = {}
assignmentsFile = open("assignmentsTESTING.csv")
lines = assignmentsFile.readlines()
for line in lines:
    (number,credit,dueDate) = line.split(",")
    dueDate = dueDate.strip("\n")
    newAssignment = Assignment.Assignment(number,credit,"0",dueDate)
    assignments[number] = newAssignment
for c in courses:
    c.assignments = assignments
try:
    
    pass
        
except Exception:
    print("Error: No assignment file found.  No assignments will be loaded.")

###############Clear Assignments for students###################
for c in courses:
    for s in c.students:
        s.assignments = []
################################################################

print "Welcome."
while True:
    response = getInput()
    processInput(response)
    print returnText
    returnText = ""

