"""
File: ceaserCracker.py
Author: Michael Williams

Decrypts Casear Cipher encrypted text that you don't 
know the rotation key value and prints the result. 
The other input is the various distance values that 
need to be checked and printed to a list.
"""

# Prompts the user for the encypted message and how many rotation keys to try
encryptedText = input("Enter the encrypted text message: ")
distance = int(input("Enter the distance values to check [ex: 50 would check roations 50 down to 0]: "))
# Creates an empty string to store all of the outputs
potentialAnswers = ''

# Iterates the number of attempts by the total distance value to check
for attempts in range(distance):
# Creates an empty string to store each individual attempt to crack the encrypted message  
    plainText = ''
    for ch in encryptedText:
# Converts each character in the message into its ASCII value and subtracts the distance from it
        ordValue = ord(ch)
        cipherValue = ordValue - distance
# Checks to see if the value is less than the lowest ASCII printable character (a space), if so
# roll-over to the last character in the set ( a tilde)
        if cipherValue < ord(' '):
            cipherValue = ord('~') - (distance - (ordValue - ord(' ')) - 1)
# Converts the new character value back from the ASCII value to the character and store in the plaintext variable
        plainText +=  chr(cipherValue)
# Creates the layout of the final output to display how many characters each attempt was rotated
    potentialAnswers += "Rotation " + str(distance) + ": "
    potentialAnswers += plainText  
    potentialAnswers += '\n'
# Iterates the count down by 1 until the distance is 0
    distance -= 1
print(potentialAnswers)
