#
# Author: Lexi LaMonica
# All rights reserved
#
import math 

def problem1():
    'Problem #1'
    var = ['54', '2', '32' ]
    var1 = ['21', '14', '63']

    varMinimum = min(var)
    varMinimum2 = min(var1)

    total= int(varMinimum) + int(varMinimum2)
    print(total)
problem1()



def problem2():
    'Problem #2'
    var = ['31', '3', '8']
    var1 = ['4', '43', '4']
    
    total = var[-1]
    total1 = var1[-1]
    
    overall = int(total) + int(total1)
    overallSum = overall / 2
    return(overallSum)
print(problem2())



def problem3():
    'Problem #3'
    
    firstVal = math.sqrt(5)
    SecondVal = math.sqrt(8)
    total = float(firstVal + SecondVal)
    print(total)
problem3()


'Problem #4'

emptyList = [ ]
number = int(input("Enter the 1st number:"))
number2 = int(input("Enter the 2nd number:"))
number3 = int(input("Enter the 3rd number:"))
emptyList.append(number)
emptyList.append(number2)
emptyList.append(number3)

highestNum = max(emptyList)
lowestNum = min(emptyList)
print("The highest number is " + str(highestNum)) 
print("The lowest number is " + str(lowestNum))
total = int(number + number2 + number3) /3
print("The average is: " + str(int(total)))
        

def problem5():
    'Problem #5'

    bigString = ('hello' + 'hi' + 'bye')
    return bigString
print(problem5())

