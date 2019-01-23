import csv


exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
# exampleData = list(exampleReader)
# print(exampleData)
# print(exampleData[0][0])
# print(exampleData[0][1])
# print(exampleData[0][2])

for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile, delimiter='\t', lineterminator='\n\n')
outputWriter.writerow(['span', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.14159, 4])
outputFile.close()
