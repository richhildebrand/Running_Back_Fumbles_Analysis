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
    for key, value in definitions.items():
        definition = definitions[key]
        defaultValue = definition.get('defaultValue', 'no default value set')
        dictionary[key] = dictionary.get(key, defaultValue)

    return dictionary

def writeHeadersFromDefinitions(definitions, writer):
    headers = []
    for definition in definitions:
        headerValue = definition['key']
        headers.append(headerValue)
    writer.writerow(headers)
    return

def writeRowFromDictionary(definitions, dictionary, writer):
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