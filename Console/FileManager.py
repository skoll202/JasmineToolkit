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
        for filename in [f for f in filenames if f.endswith(".pdf")]:
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
        for f in files:
            fileText = PDFManager.getStr(f)
            if PDFManager.isControlledPDF(text=fileText):
                
                count+=1
                assignmentNumber = PDFManager.getAssignmentNumber(text=fileText)                
                filename = "%s-%s,%s.pdf" % (assignmentNumber,s.lastName,s.firstName)
                try:
                    creditNumber = course.assignments[assignmentNumber].credit
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
            
        
        

if __name__ == '__main__':
    pass