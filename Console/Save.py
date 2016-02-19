'''
Created on Jan 12, 2016

@author: ncarlson
'''
import math
import pickle
import os

def run(data, param):
    currentCourse = data['currentCourse'].name
    courses = data['courses']
    dataPath = data['dataPath']
    settings = data['settings']
    for c in courses:
        coursesTXT = open(dataPath+"courses.txt","w")
        
        for s in c.students:
            file = open(s.submitPath+"grades.txt","w")
            for credit in range(1,15):
                
                
                
                scores = c.getScoresForCredit(credit)
                #print(scores)
                creditScore = scores[s.lastName+","+s.firstName]
                allAssignments = data['currentCourse'].getAssignmentsForCredit(credit)
                assignments = s.getAssignmentsDictForCredit(credit)
                for a in assignments.keys():
                    try:                    
                        saveFile = open(s.gradedPath+"%d\\%s.txt" % (credit,a),"w")
                    except:                        
                        try:
                            os.mkdir(s.gradedPath+"%d\\" % (credit))
                            saveFile = open(s.gradedPath+"%d\\%s.txt" % (credit,a),"w")
                        except:
                            os.mkdir(s.gradedPath)
                            os.mkdir(s.gradedPath+"%d\\" % (credit))
                            saveFile = open(s.gradedPath+"%d\\%s.txt" % (credit,a),"w")
                    score = s.getScoreForAssignment(a)
                    date = s.getSubmitDateForAssignment(a)
                    saveFile.write("%s - %s" % (score,date))
                    saveFile.close()
                
                for a in sorted(allAssignments):
                    if a in assignments.keys():
                        score = assignments[a].score
                        dateSubmitted = assignments[a].dateSubmitted
                    else:
                        score = 0
                        dateSubmitted = ""
                    file.write("%s:%s - %s\r\n" % (a,score,dateSubmitted))
                file.write("Credit %d Score:%d\r\n\r\n" % (credit,math.ceil(creditScore*100)))
            file.close()
            
            
            
    pickle.dump(courses,open("C:\\Users\\ncarlson\\Google Drive\\IT3\\courses.p","wb"))
    #settings = {}
    #settings['currentCourse'] = currentCourse
    pickle.dump(settings,open("C:\\Users\\ncarlson\\Google Drive\\IT3\\settings.p","wb"))
    
    #Save settings txt file
    settingsFile = open(dataPath+"settings.txt","w")    
    for s in settings.keys():
        if s=="courses":
            names = []
            for c in courses:
                names.append(c.name)
            settingsFile.write("courses="+",".join(names)+"\r\n")
        else:
            settingsFile.write(s+"="+settings[s]+"\r\n")
    settingsFile.close()
    
    for c in courses:
        courseFile = open(dataPath+"%s.txt" % c.name, "w")
        courseFile.write("name=%s\r\n" % c.name)
        courseFile.write("notesWeight=%f\r\n" % float(c.notesWeight))
        courseFile.write("projectWeight=%f\r\n" % float(c.projectWeight))
        for s in c.students:
            courseFile.write("student=%s,%s\r\n" % (s.lastName,s.firstName))
        courseFile.close()
        for s in c.students:
            studentFile = open(dataPath+"%s\\%s,%s.txt" % (c.name,s.lastName,s.firstName),"w")
            studentFile.write("firstName=%s\r\n" % s.firstName)
            studentFile.write("lastName=%s\r\n" % s.lastName)
            studentFile.write("course=%s\r\n" % c.name)
            for a in s.assignments:
                studentFile.write("assignment=%s,%s,%s,%s\r\n" % (a.number,a.credit,a.score,a.dateSubmitted))
            studentFile.close()
    
    returnText = "Saved Successfully"
    return returnText