'''
Created on Jan 12, 2016

@author: ncarlson
'''

import FileManager

def run(data, param):
    layer2 = {}
    returnText = "" 
    
    def sortFiles(data,param):
        courses = data['courses']
        currentCourse = data['currentCourse']
        students = currentCourse.students
        return FileManager.sortFiles(students, currentCourse)
    
    layer2['files'] = sortFiles
        
    words = param.split(' ',1)
    if words[0] in layer2.keys():
        if len(words)<2:
            words.append("")
        returnText = layer2[words[0]](data,words[1])
    else:
        returnText="Command '%s' not found" % words[0]
    return returnText