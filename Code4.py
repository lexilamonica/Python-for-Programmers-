#
# Author: Lexi LaMonica
# All rights reserved
#
import math

def getFileAsString(infile):
    'Opening the file and turning it into a string'
    infile = open('exam_grades.csv', 'r')
    emptylist = []
    for line in infile:
        for grade in line.split(','):
                emptylist.append(int(grade))
    infile.close()
    return emptylist
getFileAsString('exam_grades.csv')
    

def checkGrades():
    'Checking what the user choose for the option with a if statment'
    fileContents = getFileAsString('exam_grades.csv')
    enter_choice = getChoice()
    if enter_choice == 1:
        print('The lowest grade is ' , min(fileContents))
    elif enter_choice == 2:
        print('The highest grade is ' , max(fileContents))
    elif enter_choice == 3:
        avg_sum = 0
        for score in fileContents:
            avg_sum += int(score)
        avg = avg_sum/len(fileContents)
        print('The average grade is ' , avg )
    elif enter_choice == 4:
        user = int(input('Enter a number to search for: '))
        if (user in fileContents):
            print('The grade',user, 'was present')
        else:
            print('The grade' ,user, 'was not present')

def getChoice():
    'Giving the user the options on what to pick by using a formanted string and while statment' 
    lowest = str('Press 1 for the lowest grade')
    highest = str('Press 2 for the highest grade')
    averageOfGrade = str('Press 3 for the average grade')
    searchForGrade = str('Press 4 to search for a grade')
    total = print("{}\n{}\n{}\n{}".format(lowest, highest, averageOfGrade, searchForGrade))
    enter_choice = eval(input('Enter a choice: '))
    while(0>enter_choice or enter_choice>4):
        print('Invalid choice, needs to be between 1 - 4 ')
        enter_choice = int(input('Enter a choice:'))
    return enter_choice
checkGrades()

