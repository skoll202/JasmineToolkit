'''
Created on Jan 12, 2016

@author: ncarlson
'''


def run(data, param):
    layer2 = {}
    returnText = "" 
    
    def setCurrentCourse(data,param):        
        returnText=""
        currentCourse = data['currentCourse']
        courses = data['courses']
        i=1
        for c in courses:
            print("%d.%s" % (i,c.name))
            i+=1
        number = int(raw_input("Course Number:"))
        if number>0 and number<=len(courses):
            currentCourse=courses[number-1]
            data['currentCourse']=currentCourse
            returnText="Current Course is now "+currentCourse.name
        else:
            returnText="Invalid Selection - %d" % number
        return returnText
    layer2["course"] = setCurrentCourse
        
    words = param.split(' ',1)
    if words[0] in layer2.keys():
        if len(words)<2:
            words.append("")
        returnText = layer2[words[0]](data,words[1])
    else:
        returnText="Command '%s' not found" % words[0]
    return returnText