#
# Author: Lexi LaMonica
# All rights reserved
#

def createStudentDictionary():
    'Funcation that returns a dictionary that goes through a file'
    studentDict={}

    f = open('class_roster.txt')
    line = f.readline()
    
    
    studentDict = {}
    while line:
        first_name,last_name,student_id,year = line.split(',')
        student_year = year.strip(' \n ')
        student_tup = (first_name, last_name, student_year); studentDict.update({student_id: student_tup})
        line = f.readline()
    f.close()
    return studentDict
    

students = createStudentDictionary()


def studentSearch(dictionary, studentID):
    'Funcation that formats the dictionary above'
    try:
        combining = dictionary[studentID]
        
        total = "First Name: {} \nLast Name: {} \nSchool Year: {} ".format(combining[0], combining[1], combining[2])
        return total
    except KeyError:
        errorsum = 'No student found with ID ' + studentID + '.\n'
        return errorsum
students = createStudentDictionary()
    

