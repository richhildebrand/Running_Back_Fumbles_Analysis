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
    value = newInformation[key]
    currentInformation[key] = value
    return