#
# Author: Lexi LaMonica
# All rights reserved
#
import math

#Problem 1
def listOfWordsInFile(filename, letter):
    'Problem 1'
    result = []
    with open('example.txt') as f:
        for line in f:
            for word in line.strip().split():
                if letter.lower() in word.lower():
                    result.append(word)
    return result
print(listOfWordsInFile('example.txt', 'r'))
'''
Pseudocode for problem #1
Write a function 
Set an empty list to a value 
Open the file
Do a for statement to find the word inside the file 
Do another for statement to strip and split 
Use an if statement to find the words but in lower
Then append the result into the list
Return the list 
'''

#Problem 2
def convertCase(infile, outfile):
    'Problem 2'
    infile = open('example.txt', 'r')
    r = infile.readlines()
    outfile = open('convertCase.txt', 'w')
    for lines in r:
         a = lines.swapcase()
         outfile.write(a)
    infile.close()
    outfile.close()
convertCase('example.txt','convertCase.txt')
'''
Pseudocode for problem #2
open the file
set a value to readlines
then write an outfile
write a for loop to swapcases
use .write to output the swapcases
then close the files
'''
#Problem 3
import csv
def highestLowestGrades():
    'Problem 3'
    f = open ('exam_grades.csv')
    grades = []
    for line in f:
        for g in line.split(','):
                grades.append(int(g))
    print('Lowest Grade:', min(grades))
    print('highest Grade:', max(grades))
highestLowestGrades()

'''
Pseudocode for problem #3
open the file
set the file to a value
set another value to a empty list
write a for loop to look into the file
write another for loop to split the file
then append the numbeer into the list
print the min
print the max
'''
