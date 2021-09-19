#
# Author: Lexi LaMonica
# All rights reserved
#
class Student():
    
    def getLetterGrade(self):
        'Function is setting letterGrade and calling calcLetterGrade then returning letterGrade'
        self.letterGrade = ''
        self.calcLetterGrade()
        return self.letterGrade
    def getPercentGrade(self):
        'Function is returning percent'
        return self.percent

    def getName(self, name):
        'Function is assigning name then returning'
        self.name = name
        return self.name
    def calcLetterGrade(self):
        'Using a if else to find students grade'
        if self.percent < 60:
            letter = 'F'
        elif self.percent < 70:
            letter = 'D'
        elif self.percent < 80:
            letter = 'C'
        elif self.percent < 90:
            letter = 'B'
        else:
            letter = 'A'
        self.letterGrade = letter
    def setName(self, name):
        'Assiging name'
        self.name = name
    def setPercentGrade(self, percent):
        'Function is setting percent'
        self.percent = percent
    def addBonus(self, bonus):
        'Function is calculating the bonus'
        self.percent *= 1 + (bonus / 100)

    def printStudentInfo(self):
        'Function is returing the end print'
        return 'Name: {}\nPercent Grade: {}\nLetter Grade: {}'.format(self.name, round(self.percent,2), self.getLetterGrade())
