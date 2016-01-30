'''
Created on Jan 12, 2016

@author: ncarlson
'''
# coding: utf-8

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from PyPDF2 import PdfFileMerger, PdfFileReader
from cStringIO import StringIO
from gettext import gettext
import os

def getStr(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

def getAssignmentNumber(path=None, text=None):
    if text==None and path!=None:
        text = getStr(path)
    text="".join([x if ord(x) < 128 else '?' for x in text])
    if isExam(text=text):        
        index = text.find("Exam??Report:")
        c="?"
        num = 15
        if (index<0):
            index = text.find("Exam Report")
            c=" "
            num = 13
        number = text[index+num]+text[index+num+1]
        i=num+2
        while text[index+i]!=c:
            number+=text[index+i]
            i+=1  
    elif isLab(text=text):
        index = text.find("Lab??Report:")
        c = "?"
        num=14
        if(index<0):
            index = text.find("Lab Report:")
            c = " "
            num=12
        number = text[index+num]+text[index+num+1]
        i=num+2
        while text[index+i]!=c:
            number+=text[index+i]
            i+=1      
    return number
    
def merge(files, outFileName):
    merger = PdfFileMerger()
    for f in sorted(files):
        file = open(f,'rb')
        pdfFile = PdfFileReader(file,strict=False)
        merger.append(pdfFile)    
    merger.write(outFileName)

def getScore(path=None, text=None):
    if text==None and path!=None:
        text = getStr(path)
    text="".join([x if ord(x) < 128 else '?' for x in text])
    index = text.find("Your??Score:")
    if index<0:
        index=text.find("Your Score:")
        score = 0
        if (isExam(text=text)):        
            score = text[index+13]+text[index+14]
            if score=="10" and text[index+15]=="0":
                score+=text[index+15]
        elif (isLab(text=text)):
            num=20
            score = text[index+num]+text[index+num+1]
            if score=="10" and text[index+num+2]=="0":
                score+=text[index+num+2]
    else:
        score = 0
        if (isExam(text=text)):        
            score = text[index+13]+text[index+14]
            if score=="10" and text[index+15]=="0":
                score+=text[index+15]
        elif (isLab(text=text)):
            score = text[index+25]+text[index+26]
            if score=="10" and text[index+27]=="0":
                score+=text[index+27]
    return score


def isExam(path=None,text=None):
    if text==None and path!=None:
        text = getStr(path)
    text="".join([x if ord(x) < 128 else '?' for x in text])
    index = text.find("Exam??Report:")
    if index>-1:
        index = text.find("Exam Report:")
    else:
        if index>-1:
            return True
        else:
            return False

def isLab(path=None,text=None):
    if text==None and path!=None:
        text = getStr(path)
    text="".join([x if ord(x) < 128 else '?' for x in text])
    index = text.find("Lab??Report:")
    if index>-1:
        return True
    else:
        index = text.find("Lab Report:")
        if index>-1:
            return True
        else:
            return False

def isNotes(path=None,text=None):
    return False

def isProject(path=None,text=None):
    return False

def isControlledPDF(path=None,text=None):
    if text==None and path!=None:
        text = getStr(path)
    if isExam(text=text) or isLab(text=text) or isNotes(text=text) or isProject(text=text):
        return True
    else:
        return False

def getStudentName(path,students):
    pass

if __name__ == '__main__':
    files = []
    path = "C:\\Users\\ncarlson\\Google Drive\\IT3\\Graded\\IT3 Jan 2016\\Curtis,Arriana\\1\\1.2.2-Curtis,Arriana.pdf"  
    files.append(path)
    text2 = getStr(path)
    #print(text2)
    print isExam(text=text2)
    print isLab(text=text2)
    print getAssignmentNumber(text=text2)
    print getScore(text=text2)
    
    path2 = "C:\\Users\\ncarlson\\Google Drive\\IT3\\Graded\\IT3 Jan 2016\\Courts,Baily\\1\\1.2.2-Courts,Baily.pdf"  
    files.append(path)
    text2 = getStr(path)
    #print(text2)
    print isExam(text=text2)
    print isLab(text=text2)
    print getAssignmentNumber(text=text2)
    print getScore(text=text2)
    
    path3 = "C:\\Users\\ncarlson\\Google Drive\\IT3\\Graded\\IT3 Jan 2016\\Kelly,Dylon\\1\\1.2.2-Kelly,Dylon.pdf"  
    files.append(path)
    text2 = getStr(path)
    #print(text2)
    print isExam(text=text2)
    print isLab(text=text2)
    print getAssignmentNumber(text=text2)
    print getScore(text=text2)
    
    merge(files, "C:\\Users\\ncarlson\\Google Drive\\IT3\\Graded\\IT3 Jan 2016\\testMerge.pdf"  )