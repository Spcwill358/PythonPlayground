# Comments will be added ASAP
encodedText = input("Enter the coded text: ")
binaryString = ''
count = 0
shiftedString = ''
total = 0

for bit in encodedText:     
    if bit == ' ':
        lastBit = binaryString[-1]
        remainingBits = binaryString[:count - 1]
        flippedBit = lastBit + remainingBits + ' '
        shiftedString += flippedBit
        binaryString = ''
        count = 0
    binaryString += bit
    total += 1
    count += 1
    if total == len(encodedText):
        lastBit = binaryString[-1]
        remainingBits = binaryString[:count - 1]
        flippedBit = lastBit + remainingBits + ' '
        shiftedString += flippedBit
        binaryString = ''
        count = 0
    if binaryString == ' ':
        binaryString = '' 
    if binaryString == '':
        count = 0 

octalString = ''
binaryToOctal = ''
total = 0

for bit in shiftedString:
    value = 64
    count = 0
    totalValue = 0
    if bit == ' ' or total == (len(shiftedString) - 1):
        if len(binaryToOctal) == 6:
            value = 32
        for number in binaryToOctal:
            totalValue += int(binaryToOctal[count]) * value
            value = value / 2
            count += 1
        totalValue -= 1
        octalString += chr(int(totalValue))
        binaryToOctal = ''
    binaryToOctal += bit
    if binaryToOctal == ' ':
        binaryToOctal = ''
    total += 1
print(octalString)
