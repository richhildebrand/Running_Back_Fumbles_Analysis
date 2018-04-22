from collections import defaultdict

def getByType(currentInformation, newInformation, key, dataType):
    if (dataType == 'int'):
        addIntegerKeyValuePair(currentInformation, newInformation, key)

    return addOrReplaceStringKeyValuePair(currentInformation, newInformation, key)

def getValueOrZero(dictionary, key):
    try:
        value = dictionary[key]
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

def combine(d1, d2):
    return { **d1, **d2 }