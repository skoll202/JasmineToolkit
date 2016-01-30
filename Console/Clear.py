'''
Created on Jan 18, 2016

@author: ncarlson
'''
def run(data, param):
    layer2 = {}
    returnText = "" 
    
    def clearAssignments(data, param):
        currentCourse = data['currentCourse']
        students = currentCourse.students
        for s in students:
            s.assignments = []
        returnText = "All assignments cleared"
        return returnText
    
    layer2['assignments'] = clearAssignments
    
    words = param.split(' ',1)
    if words[0] in layer2.keys():
        if len(words)<2:
            words.append("")
        returnText = layer2[words[0]](data,words[1])
    else:
        returnText="Command '%s' not found" % words[0]
    return returnText