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
import pyPdf

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

def getStrAlt(path):
    content = ""
    # Load PDF into pyPDF
    pdf = pyPdf.PdfFileReader(file(path, "rb"))
    # Iterate pages
    for i in range(0, pdf.getNumPages()):
        # Extract text from page and add to content
        content += pdf.getPage(i).extractText() + "\n"
    # Collapse whitespace
    #content = " ".join(content.replace("\xa0", " ").strip().split())
    return content

def getAssignmentNumber(path=None, text=None):
    if text==None and path!=None:
        text = getStr(path)
    number = None
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
    elif isNotes(text=text):
        index = text.lower().find("credit")
        if index>-1:
            running = True
            i=6
            credit = ""
            while running:
                character = text[index+i]
                if character.isdigit():
                    credit+=character
                    i+=1
                else:
                    if credit=="":
                        i=i+1
                    else:
                        running = False               
                    
            number = "Credit%sNotes"%credit
    return number
    
def merge(files, outFileName):
    try:
        merger = PdfFileMerger()
        notes = None
        
        for f in files:
            filename = os.path.split(f)[1]
            if "Credit" in filename:
                notes = f
        if notes != None:
            files.remove(notes)
            file = open(notes,'rb')
            pdfFile = PdfFileReader(file,strict=False)
            merger.append(pdfFile)
        for f in sorted(files):
            file = open(f,'rb')
            pdfFile = PdfFileReader(file,strict=False)
            merger.append(pdfFile)    
        merger.write(outFileName)
    except:
        print("Error writing pdf file %s" % outFileName)

def getScore(path=None, text=None):
    if text==None and path!=None:
        text = getStr(path)
    text="".join([x if ord(x) < 128 else '?' for x in text])
    index = text.find("Your??Score:")
    if index<0:
        index=text.find("Your Score:")
        score = 0
        if (isExam(text=text)):  
            extra0 = 15 
            num = 13     
            score = text[index+num]+text[index+num+1]
            while "(" in score:
                num=num+1
                score = text[index+num]+text[index+num+1]
                extra0 = num+2
            while "%" in score:
                num=num-1
                score = text[index+num]+text[index+num+1]
                extra0 = num+2
            
            if score=="10" and text[index+extra0]=="0":
                score+=text[index+extra0]
        elif (isLab(text=text)):
            num=20
            extra0=num+2
            score = text[index+num]+text[index+num+1]
            while "(" in score:
                num=num+1
                score = text[index+num]+text[index+num+1]
                extra0 = num+2
            while "%" in score:
                num=num-1
                score = text[index+num]+text[index+num+1]
                extra0 = num+2
            if score=="10" and text[index+extra0]=="0":
                score+=text[index+extra0]
    else:
        score = 0
        if (isExam(text=text)):        
            extra0 = 15 
            num = 13     
            score = text[index+num]+text[index+num+1]
            while "(" in score:
                num=num+1
                score = text[index+num]+text[index+num+1]
                extra0 = num+2
            while "%" in score:
                num=num-1
                score = text[index+num]+text[index+num+1]
                extra0 = num+2
            if score=="10" and text[index+extra0]=="0":
                score+=text[index+extra0]
        elif (isLab(text=text)):
            num=25
            score = text[index+num]+text[index+num+1]
            extra0=num+2
            while "(" in score:
                num=num+1
                score = text[index+num]+text[index+num+1]
                extra0 = num+2
            while "%" in score:
                num=num-1
                score = text[index+num]+text[index+num+1]
                extra0 = num+2
            if score=="10" and text[index+extra0]=="0":
                score+=text[index+extra0]
    if score=='(0':
        score = '0'
    return score


def isExam(path=None,text=None):
    if text==None and path!=None:
        text = getStr(path)
    text="".join([x if ord(x) < 128 else '?' for x in text])
    index = text.find("Exam??Report:")
    if index>-1:
        return True
    else:
        index = text.find("Exam Report:")
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
    if text==None and path!=None:
        text = getStr(path)
    text="".join([x if ord(x) < 128 else '?' for x in text])
    index = text.lower().find("notes")
    if index>-1:
        return True
    else:
        index = text.lower().find("notes")
        if index>-1:
            return True
        else:
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
    path = "C:\\Users\\ncarlson\\Google Drive\\IT3\\IT3 Jan 2016\\White,Tyris\\Ghost.pdf"  
    files.append(path)
    #text2 = getStr(path)
    text2 = getStrAlt(path)
    print(text2)
    print isExam(text=text2)
    print isLab(text=text2)
    print getAssignmentNumber(text=text2)
    print getScore(text=text2)
    