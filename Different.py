"""
File: dif.py
Project 4.10

Deterines whether or not the contents of two text
files are the same.  Outputs "Yes" if that is the
case or "No" and the first two lines that differ if
that is not the case.
"""

firstInput = input("Enter the first file name: ")
secondInput = input("Enter the second file name: ")

firstFile = open(firstInput, 'r')
secondFile = open(secondInput, 'r')

firstFileLines = firstFile.readlines()
secondFileLines = secondFile.readlines()
match = True

for line in range(len(firstFileLines)):
    if firstFileLines[line] != secondFileLines[line]:
        print("")
        print("No")
        print(firstFileLines[line]+secondFileLines[line])
        match = False
        break

if match == True:
    print("")
    print("Yes")
