#Prompts the user for a file to be copied from and a name for a new file
#that it will be copied into
inputFile = input("Enter a file to be copied: ")
outputFile = input("Enter a name for the file to be copied to: ")

#Begins a counter to add for numbering lines in the text file
count = 0

#Opens the file to be read
file1 = open(inputFile, 'r')

#Opens the file to be written to
file2 = open(outputFile, 'w')

#Iterates line by line and adds a #> to each line with spacing justified right
for line in file1:
    count += 1   
    file2.write("%4d" % count + "> " + line)

#Closes both the new file and the one copied from
file1.close()
file2.close()
