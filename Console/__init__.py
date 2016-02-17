import os
import pickle

import Course
import Student

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
import Submit

import FileManager
import Assignment

command = {}
courses = []
currentCourse=""
dataPath = "C:\\Users\\ncarlson\\Google Drive\\IT3\\"

returnText = ""

def getCurrentCourse():
    global currentCourse
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

command['submit'] = Submit.run

def processInput(param):
    words = param.split(' ',1)
    data = {}
    data['currentCourse'] = getCurrentCourse()
    data['courses'] = courses
    data['dataPath'] = dataPath
    if words[0] in command.keys():
        
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
    courses = pickle.load(open("C:\\Users\\ncarlson\\Google Drive\\IT3\\courses.p"))
    settings = pickle.load(open("C:\\Users\\ncarlson\\Google Drive\\IT3\\settings.p"))
    if 'currentCourse' in settings.keys():
        for c in courses:
            if settings['currentCourse']==c.name:
                currentCourse = c.name
                break
    
except Exception:
    courses = []

assignments = {}

try:
    assignmentsFile = open("assignments.csv")
    lines = assignmentsFile.readlines()
    for line in lines:
        (number,credit) = line.split(",")
        assignments[number] = int(credit.rstrip())
    for c in courses:
        c.assignments = assignments
        
except Exception:
    print("Error: No assignment file found.  No assignments will be loaded.")

for c in courses:
    for s in c.students:
        for a in s.assignments:
            if a.credit!=-1:
                try:
                    saveFile = open(s.gradedPath+"\\%d\\%s.txt" % (a.credit,a.number))
                    str = saveFile.readline()
                    (score,dateSubmitted) = str.split(" - ")
                    if score!="0" and score!=a.score:
                        a.score = score
                        print("new score for %s %s credit %d would be %s instead of %s" % (s.firstName,s.lastName,int(a.credit),score,a.score))
                except:
                    s.assignments.remove(a)
        for i in range(1,16):
            files = FileManager.getTXTFiles(s.gradedPath+"%d\\" % i)
            for f in files:
                filename = os.path.split(f)[1]
                num = os.path.splitext(filename)[0]
                assignments = s.getAssignmentsDictForCredit(i)
                if num not in assignments.keys():
                    saveFile = open(f)
                    str = saveFile.readline()
                    (score,dateSubmitted) = str.split(" - ")
                    assignment = Assignment.Assignment()
                    assignment.score = score
                    assignment.number = num
                    assignment.dateSubmitted = dateSubmitted
                    try:
                        assignment.credit = c.assignments[num]
                    except:
                        assignment.credit = -1
                    s.assignments.append(assignment)
                    print("New assignment found for %s %s:%s in credit %d" % (s.firstName,s.lastName,num,i))

###############Clear Assignments for students###################
#for c in courses:
#    for s in c.students:
#        s.assignments = []
################################################################

print "Welcome.\r\n"
processInput("print ungraded notes")
print(returnText)
returnText = ""
while True:
    response = getInput()
    processInput(response)
    print returnText
    returnText = ""

