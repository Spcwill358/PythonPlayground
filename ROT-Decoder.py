#Basic ROT Cipher decoder

codedText = input("Enter the coded text: ")
distanceValue = int(input("Enter the distance value: "))
decodedText = ""

for character in codedText:
    charValue = ord(character)
    shiftAmount = charValue - distanceValue
    if charValue < ord(" "):
        shiftAmount = ord("~") - (ord(" ") - shiftAmount + 1)
    decodedText += chr(shiftAmount)
print(decodedText)
