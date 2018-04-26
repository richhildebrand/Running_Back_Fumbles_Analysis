from collections import defaultdict
import statistics

def getByType(currentInformation, newInformation, key, dataType):
    if (dataType == 'int'):
        addIntegerKeyValuePair(currentInformation, newInformation, key)
        return

    return addOrReplaceStringKeyValuePair(currentInformation, newInformation, key)

def getValueOrZero(dictionary, key):
    try:
        valueAsString = str(dictionary[key])
        value = valueAsString.replace(',', '').strip()
        return int(value)
    except (ValueError, KeyError):
        return 0

def addIntegerKeyValuePair(currentInformation, newInformation, key):
    currentValue = getValueOrZero(currentInformation, key)
    valueToAdd = getValueOrZero(newInformation, key)

    newValue = currentValue + valueToAdd
    currentInformation[key] = newValue
    return

def addOrReplaceStringKeyValuePair(currentInformation, newInformation, key): 
    value = newInformation.get(key, False)
    currentInformation[key] = value or currentInformation.get(key)
    return

def addStandardDeviation(dictionaries, key):
    allValues = []
    for id, item, in dictionaries.items():
        value = float(item[key])
        allValues.append(value)

    mean = statistics.mean(allValues)
    std = statistics.pstdev(allValues) #use pstd because we have the whole population

    p1std = mean + 1 * std
    p2std = mean + 2 * std
    p3std = mean + 3 * std

    n1std = mean - 1 * std
    n2std = mean - 2 * std
    n3std = mean - 3 * std

    for id, item, in dictionaries.items():
        value = float(item[key])
        if n3std > value: item[key + '_std'] = -3
        if n3std < value < n2std: item[key + '_std'] = -2
        if n2std < value < n1std: item[key + '_std'] = -1

        if n1std < value < p1std: item[key + '_std'] = 0

        if p1std < value < p2std: item[key + '_std'] = 1
        if p2std < value < p3std: item[key + '_std'] = 2
        if p3std < value: item[key + '_std'] = 3

    return dictionaries



def combine(d1, d2):
    return { **d1, **d2 }

