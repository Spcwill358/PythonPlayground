# Put your code below:
fileName = input("Enter the input file name: ")
count = 0
stop = False

file = open(fileName, 'r')
for i in file:
    count += 1

lineCount = "The file has " + str(count) + " lines."
print(lineCount)

while stop == False:
    viewLine = int(input("Enter a line number [0 to quit]: "))
    if viewLine == 0:
        stop = True
    elif viewLine > count:
        print("ERROR: line number must be less than", count, ".")
    else:
        file = open(fileName, 'r')
        line = file.readlines()
        print(viewLine, ":", line[viewLine - 1])
