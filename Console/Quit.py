'''
Created on Jan 12, 2016

@author: ncarlson
'''
import Save

def run(data, param):
    if data['currentCourse']!="FAIL":
        Save.run(data, param)
    else:
        print("No data saved.  Current course was not set correctly.")
    print "Goodbye."
    exit()