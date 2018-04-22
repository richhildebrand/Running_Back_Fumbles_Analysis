import csv

def getValueOrDefault(key, dictionary):


def readRowsFrom(numberOfRowsToRead, pathToFile): 
    rows = {}
    with open(pathToFile, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for rowNumber, rowData in enumerate(reader):
            rows[rowNumber] = rowData
            if(rowNumber > numberOfRowsToRead):
                break
    return rows

def writeHeadersFromDictionary(dictionary, pathToFile, writer):
    keys = []
    for key, value in dictionary.items():
        keyAsString = str(key)
        keys.append(keyAsString)
    writer.writerow(keys)

    return

def writeRowFromDictionary(dictionary, pathToFile, writer):
    values = []
    for key, value in dictionary.items():
        valueAsString = str(value)
        values.append(valueAsString)
    writer.writerow(values)

    return

def writeRowsFromNestedDictionary(dictionary, pathToFile):
    with open(pathToFile, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        firstKey = list(dictionary.keys())[0]
        firstItem = dictionary[firstKey]
        writeHeadersFromDictionary(firstItem, pathToFile, writer)

        for key, nestedDictionary, in dictionary.items():
            writeRowFromDictionary(nestedDictionary, pathToFile, writer)
    return