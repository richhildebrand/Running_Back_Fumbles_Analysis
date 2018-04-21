import csv

def readRowsFrom(numberOfRowsToRead, pathToFile): 
    rows = {}
    with open(pathToFile, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for rowNumber, rowData in enumerate(reader):
            rows[rowNumber] = rowData
            if(rowNumber > numberOfRowsToRead):
                break
    return rows

def writeRowFromDictionary(dictionary, pathToFile):
    with open(pathToFile, 'w') as csv_file:
        writer = csv.writer(csv_file)
        values = []
        for key, value in dictionary.items():
            valueAsString = str(value)
            values.append(valueAsString)
        writer.writerow(values)
    return