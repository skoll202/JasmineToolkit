'''
Created on Jan 12, 2016

@author: ncarlson
'''
import math
import pickle

def run(data, param):
    currentCourse = data['currentCourse'].name
    courses = data['courses']
    
    for c in courses:
        for s in c.students:
            file = open(s.submitPath+"grades.txt","w")
            for credit in range(1,15):
                scores = c.getScoresForCredit(credit)
                #print(scores)
                creditScore = scores[s.lastName+","+s.firstName]
                assignments = s.getAssignmentsForCredit(credit)
                for a in assignments:
                    file.write("%s:%s - %s\r\n" % (a.number,a.score,a.dateSubmitted))
                file.write("Credit %d Score:%d\r\n\r\n" % (credit,math.ceil(creditScore*100)))
            file.close()
    pickle.dump(courses,open("C:\\Users\\ncarlson\\Google Drive\\IT3\\courses.p","wb"))
    settings = {}
    settings['currentCourse'] = currentCourse
    pickle.dump(settings,open("C:\\Users\\ncarlson\\Google Drive\\IT3\\settings.p","wb"))
    returnText = "Saved Successfully"
    return returnText