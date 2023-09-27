# Created by: Michael Williams

# Purpose: To convert a string into a series of binary as a simple form of encryption. 
#          The script takes the string, assess the ASCII value of each character and 
#          adds on to it. Then it converts the new ASCII value into binary. Afterward
#          each letter, represented in binary form, is bit shifted to the left by one.

# Accepts an input of a string to be converted
plaintext = input("Enter a message: ")

# Creates an empty string to store the string converted by an ASCII value of + 1
textASCII = ''

#Iterates through the plaintext string, converting to a ASCII value and adding to the value
for character in plaintext:
    ordValue = ord(character)
    cipherValue = ordValue + 1
    # This part determines if you've reached the end of the ASCII character set, '~'
    # If so, roll around to the first character in the set ' ' 
    if cipherValue > ord('~'):
        cipherValue = ord(' ') 
    textASCII += chr(cipherValue)

# Creates an empty string with the final encrypted text
encryptedText = ''

# 
count = 0

for character in textASCII:
    binary = ''
    valueToConvert = ord(textASCII[count])
    checkNumber = 128
    for i in range(8):
        if valueToConvert >= checkNumber:
            binary += '1'
            valueToConvert -= checkNumber
            checkNumber = checkNumber / 2
        else:
            binary += '0'
            checkNumber = checkNumber / 2
    firstBit = binary[0]
    remainingBits = binary[1:8]
    binary = remainingBits + firstBit
    if count < (len(textASCII) - 1):
        binary += ' '
    encryptedText += binary
    count += 1
print(' ')
print(encryptedText)
