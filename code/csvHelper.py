import csv

def readRowsFrom(numberOfRowsToRead, pathToFile): 
    rows = {}
    with open(pathToFile, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for rowNumber, rowData in enumerate(reader):
            if(rowNumber >= numberOfRowsToRead):
                break
            rows[rowNumber] = rowData

    return rows

def writeRows(dictionary, definitions, filePath):
    keysToPrint = list(definitions.keys())
    
    with open(filePath, 'w', newline='') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=keysToPrint)
        writer.writeheader()

        for key, row, in dictionary.items():
            writeRow(row, definitions, writer)

def writeRow(dictionary, definitions, writer):
    ensureKeys(dictionary, definitions)
    writer.writerow(dictionary)

def ensureKeys(dictionary, definitions): 
    for key, definition in definitions.items():
        defaultValue = definition.get('defaultValue', 'no default value set')
        dictionary[key] = dictionary.get(key, defaultValue)

    return dictionary