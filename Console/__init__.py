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
settings = {}

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
    data['settings'] = settings
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
   

if os.path.exists(dataPath+"settings.txt"):
    #read settings from settings txt file
    settingsFile = open(dataPath+"settings.txt")
    data = settingsFile.readlines()
    
    #Settings Template
    settingsData = {}
    settingsData['currentCourse']=""
    settingsData['courses']=""
    
    for d in data:
        if "=" in d:
            #is a setting
            (k,value) = d.split("=")
            settings[k]=value.rstrip()
        else:
            #not a setting
            pass
    settingsFile.close()
    print settings
    for k in settingsData.keys():
        if k not in settings.keys():
            settings[k]=""
#create settings txt file if it doesnt exist with standard settings 
else:
    settingsFile = open(dataPath+"settings.txt","w")    
    print settingsData
    for s in settingsData.keys():
        print s
        settingsFile.write(s+"="+settingsData[s]+"\r\n")
    settingsFile.close()
    
def loadStudentData(course,name):
    studentFile = open(dataPath+"%s\\%s.txt" % (course.name,name))
    slines = studentFile.readlines()
    tempData = {}
    tempData['assignments'] = []
    for line in slines:
        if "=" in line:
            (k,value) = line.split("=")
            if k=="assignment":
                value=value.rstrip()
                (number,credit,score,dateSubmitted) = value.split(",")
                newAssignment = Assignment.Assignment(number,credit,score)
                newAssignment.dateSubmitted = dateSubmitted
                tempData['assignments'].append(newAssignment)
            else:
                tempData[k]=value.rstrip()
    studentFile.close()
    newStudent = Student.Student(tempData['firstName'],tempData['lastName'],course,tempData['assignments'])
    newStudent.gradedPath = "C:\\Users\\ncarlson\\Google Drive\\IT3\\Graded\\"+course.name+"\\"+tempData['lastName']+","+tempData['firstName']+"\\"
    #print newStudent.lastName
    #for a in newStudent.assignments:
        #print a.number
    return newStudent
     
courseNames = settings['courses'].split(",")
for c in courseNames:
    newCourse = Course.Course(c)
    courseFile = open(dataPath+"%s.txt" % c)
    cLines = courseFile.readlines()
    for l in cLines:
        if "=" in l:
            (k,value) = l.split("=")
            if k=="student":
                newStudent = loadStudentData(newCourse,value.rstrip())
                newCourse.students.append(newStudent)
            elif k=="notesWeight":
                newCourse.notesWeight=value.rstrip()
            elif k=="projectWeight":
                newCourse.projectWeight=value.rstrip()
            else:
                pass
                 
    courseFile.close()
    courses.append(newCourse)

try:
    #courses = pickle.load(open("C:\\Users\\ncarlson\\Google Drive\\IT3\\courses.p"))
    #settings = pickle.load(open("C:\\Users\\ncarlson\\Google Drive\\IT3\\settings.p"))
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
                    saveFile = open(s.gradedPath+"\\%d\\%s.txt" % (int(a.credit),a.number))
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
                #print s.lastName
                #print assignments
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

