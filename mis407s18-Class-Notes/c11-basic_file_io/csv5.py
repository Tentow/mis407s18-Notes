import csv
csvFile = open('sample2.csv', 'w', newline='')
sampleWriter = csv.writer(csvFile)
sampleWriter.writerow(['Bob', 'Jones', '1234 Elm Street'])
sampleWriter.writerow(['Jill', 'Green', '4321 Pine Avenue'])
csvFile.close()
