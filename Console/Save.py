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
    settings = {}
    settings['currentCourse'] = currentCourse
    pickle.dump(settings,open("C:\\Users\\ncarlson\\Google Drive\\IT3\\settings.p","wb"))
    returnText = "Saved Successfully"
    return returnText