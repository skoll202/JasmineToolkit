'''
Created on Feb 17, 2016

@author: ncarlson
'''


def run(data, param):
    layer2 = {}
    returnText = "" 
    
    def submitCredit(data, param):
        currentCourse = data['currentCourse']
        words = param.split(' ',1)
        credit = words[0]
        isSubmitted = "No"
        for s in currentCourse.students:
            if s.isPacketSubmitted(credit):
                isSubmitted = "Yes"
            input = raw_input("Submitted packet for %s %s credit %s?(%s):" % (s.firstName,s.lastName,credit,isSubmitted))   
            if input.lower()==isSubmitted.lower() or input.lower()==isSubmitted[0].lower():
                pass
            else:
                if len(input)>1:
                    if input.lower()=="yes":
                        s.submitPacket
                    else:
                        returnText = "I did not understand your input for %s %s.  No changes made for this student.\r\n" % (s.firstName,s.lastName)
                else:
                    if input.lower()=="y":
                        s.submitPacket(credit)
                    elif input.lower()=="n":
                        isSubmitted = "no"
                    else:
                        returnText = "I did not understand your input for %s %s.  No changes made for this student.\r\n" % (s.firstName,s.lastName)
    layer2['credit'] = submitCredit
    
    
    
    words = param.split(' ',1)
    if words[0] in layer2.keys():
        if len(words)<2:
            words.append("")
        returnText = layer2[words[0]](data,words[1])
    else:
        returnText="Command '%s' not found" % words[0]
    return returnText