'''
Created on Jan 14, 2016

@author: ncarlson
'''

import os
import os.path
import shutil
import PDFManager

def getPDFFiles(path):
    files = []
    for dirpath,dirnames, filenames in os.walk(path):
        for f in filenames:
            print os.path.join(dirpath,f)
        for filename in [f for f in filenames if f.endswith(".pdf")]:
            files.append(os.path.join(dirpath,filename))
    return files

def getTXTFiles(path):
    files = []
    for dirpath,dirnames, filenames in os.walk(path):
        for filename in [f for f in filenames if f.endswith(".txt")]:
            files.append(os.path.join(dirpath,filename))
    return files

def getNewFiles(students):
    files = {}
    for s in students:        
        path = s.submitPath
        files[s.lastName+","+s.firstName] = getPDFFiles(path)
    
def sortFiles(students,course):
    str = ""
    for s in students:
        count = 0
        files = getPDFFiles(s.submitPath)
        print("%d files found for %s %s" % (len(files),s.firstName,s.lastName))
        for f in files:
            fileText = PDFManager.getStr(f)
            if PDFManager.isControlledPDF(text=fileText):
                
                count+=1
                assignmentNumber = PDFManager.getAssignmentNumber(text=fileText)                
                filename = "%s-%s,%s.pdf" % (assignmentNumber,s.lastName,s.firstName)
                try:
                    creditNumber = course.assignments[assignmentNumber]
                except:
                    creditNumber = -1
                if "Notes" in assignmentNumber:
                    print("Notes found for %s %s for Credit %s" % (s.firstName, s.lastName, creditNumber))
                try:
                    dst = s.gradedPath+"\\%d\\%s" % (creditNumber,filename)
                except:
                    dst = s.gradedPath+"\\%s\\%s" % (creditNumber,filename)
                #Check if graded folder exists and create if necessary
                path = os.path.split(dst)[0]
                if not os.path.exists(path):
                    os.makedirs(path)
                shutil.move(f, dst)
        str+="Moved %d files submitted by %s %s \r\n" % (count,s.firstName, s.lastName)
    return str
            
            
def getNotes(path):
    notesFile = ""
    files = getPDFFiles(path)
    for f in files:
        if "Notes" in f:
            notesFile = f
            break
    return notesFile

def notesExist(path,credit=""):
    if credit=="":
        notes = getNotes(path)
    else:
        fullPath = "%s%d\\" % (path,int(credit))
        notes = getNotes(fullPath)
    if notes=="":
        return False
    else:
        return True


        

if __name__ == '__main__':
    print(notesExist("C:\\Users\\ncarlson\\Google Drive\\IT3\\Graded\\%s\\%s\\" % ("IT3 Jan 2016","Robinson,Nathan"), 1))