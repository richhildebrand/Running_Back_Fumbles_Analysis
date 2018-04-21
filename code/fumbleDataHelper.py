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

def updatePlayerInCollection(row, allPlayers):
    playerId = row['Player Id']
    player = allPlayers.get(playerId, {})

    addOrReplaceStringKeyValuePair(player, row, 'Player Id')
    addOrReplaceStringKeyValuePair(player, row, 'Name')
    addIntegerKeyValuePair(player, row, 'Games Played')
    addIntegerKeyValuePair(player, row, 'Fumbles')

    allPlayers[playerId] = player
    return