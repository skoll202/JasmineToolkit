'''
Created on Jan 21, 2016

@author: ncarlson
'''

import Assignment


def run(data, param):
    layer2 = {}
    returnText = "" 
    
    def gradeNotes(data, param):
        currentCourse = data['currentCourse']
        words = param.split(' ',1)
        if words[0]=='for':
            words = words[1].split(' ',1)
        if words[0]=='credit':
            credit = int(words[1])
            for s in currentCourse.students:
                currentGrade = 0
                notesAssignment = None
                for a in s.assignments:
                    if a.number=="Credit%dNotes"%credit:
                        currentGrade = a.score
                        notesAssignment = a
                        break
                grade = raw_input("Grade for %s,%s(%d):" % (s.lastName,s.firstName,int(currentGrade)))
                if grade=='':
                    grade=currentGrade
                if notesAssignment==None:
                    notesAssignment = Assignment.Assignment("Credit%dNotes"%credit,credit,grade)
                    s.assignments.append(notesAssignment)
                else:
                    notesAssignment.score = grade
        return "Notes grades submitted."     
    layer2['notes'] = gradeNotes
    
    def gradeProjects(data,param):
        currentCourse = data['currentCourse']
        words = param.split(' ',1)
        if words[0]=='for':
            words = words[1].split(' ',1)
        if words[0]=='credit':
            credit = int(words[1])
            for s in currentCourse.students:
                currentGrade = 0
                projectAssignment = None
                for a in s.assignments:
                    if a.number=="Credit%dProject"%credit:
                        currentGrade = a.score
                        projectAssignment = a
                        break
                grade = raw_input("Grade for %s,%s(%d):" % (s.lastName,s.firstName,int(currentGrade)))
                if grade=='':
                    grade=currentGrade
                if projectAssignment==None:
                    projectAssignment = Assignment.Assignment("Credit%dNotes"%credit,credit,grade)
                    s.assignments.append(projectAssignment)
                else:
                    projectAssignment.score = grade
        return "Project grades submitted." 
    
    def gradeCredit(data,param):
        words = param.split(' ',1)
        returnText = ''
        if words[1]=='notes':
            returnText = gradeNotes(data,"credit %s" % words[0])
        elif words[1]=='project':
            returnText = gradeProjects(data,"project %s" % words[0])
        return returnText
    layer2['credit'] = gradeCredit
    
    words = param.split(' ',1)
    if words[0] in layer2.keys():
        if len(words)<2:
            words.append("")
        returnText = layer2[words[0]](data,words[1])
    else:
        returnText="Command '%s' not found" % words[0]
    return returnText