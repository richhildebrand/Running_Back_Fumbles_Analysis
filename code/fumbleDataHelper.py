from .dictionaryHelper import addOrReplaceStringKeyValuePair, addIntegerKeyValuePair, getByType

def getOutputFormat():
    columnHeaders = { }
    columnHeaders['Player Id'] = { 'defaultValue': 'no value given', 'type': 'string'}
    columnHeaders['Name'] = { 'defaultValue': 'no value given', 'type': 'string'}
    columnHeaders['Games Played Fumbles'] = { 'defaultValue': 'no value given', 'type': 'int'}
    columnHeaders['Games Played Rushing'] = { 'defaultValue': 'no value given', 'type': 'int'}
    columnHeaders['Fumbles'] = { 'defaultValue': 'no value given', 'type': 'int'}
    columnHeaders['Rushing Attempts'] = { 'defaultValue': 'no value given', 'type': 'int'}
    columnHeaders['Rushing Yards'] = { 'defaultValue': 'no value given', 'type': 'int'}

    return columnHeaders

def combineAllPlayerData(collection, combinedData): 
    for rowNumber, rowData, in collection.items():
        combinePlayerData(rowData, combinedData)

    return combinedData

def combinePlayerData(row, allPlayers):
    playerId = row['Player Id']
    player = allPlayers.get(playerId, {})

    headers = getOutputFormat()
    for key, header, in headers.items():
        getByType(player, row, key, header['type'])

    allPlayers[playerId] = player
    return

def filterAtLeast(dataCollection, key, minValue):
    filteredData = {}
    for id, dataPoint, in dataCollection.items():
        value = dataPoint.get(key, 0)
        if (value >= minValue):
            filteredData[id] = dataPoint

    return filteredData


def calculateFumblesPerGame(combinedFumbleData):
    for key, playerData, in combinedFumbleData.items():
        fumbles = playerData['Fumbles']
        gamesPlayed = playerData['Games Played']
        fumblesPerGame = safeZeroDivision(fumbles, gamesPlayed)

        playerData['Fumbles Per Game'] = fumblesPerGame

    return

def safeZeroDivision(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return 0