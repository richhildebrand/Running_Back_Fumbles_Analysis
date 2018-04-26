from .dictionaryHelper import addOrReplaceStringKeyValuePair, addIntegerKeyValuePair, getByType, getValueOrZero

def getOutputFormat():
    columnHeaders = { }
    columnHeaders['Player Id'] = { 'defaultValue': 'no value given', 'type': 'string'}
    columnHeaders['Name'] = { 'defaultValue': 'no value given', 'type': 'string'}
    columnHeaders['Games Played Fumbles'] = { 'defaultValue': 'no value given', 'type': 'int'}
    columnHeaders['Games Played Rushing'] = { 'defaultValue': 'no value given', 'type': 'int'}
    columnHeaders['Rushing Fumbles'] = { 'defaultValue': 'no value given', 'type': 'int'}
    columnHeaders['Rushing Attempts'] = { 'defaultValue': 'no value given', 'type': 'int'}
    columnHeaders['Rushing Yards'] = { 'defaultValue': 'no value given', 'type': 'int'}

    columnHeaders['Fumbles Per Game'] = { 'defaultValue': 'no value given', 'type': 'calculated'}
    columnHeaders['Carries Per Fumble'] = { 'defaultValue': 'no value given', 'type': 'calculated'}
    columnHeaders['Yards Per Fumble'] = { 'defaultValue': 'no value given', 'type': 'calculated'}
    columnHeaders['Yards Per Carry'] = { 'defaultValue': 'no value given', 'type': 'calculated'}

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
        value = getValueOrZero(dataPoint, key)
        if (value >= minValue):
            filteredData[id] = dataPoint

    return filteredData

def calculateXperY(combinedFumbleData, newKey, x, y):
    for key, playerData, in combinedFumbleData.items():
        xValue = playerData.get(x)
        yValue = playerData.get(y)
        xPerY = safeZeroDivision(xValue, yValue)

        playerData[newKey] = xPerY

    return combinedFumbleData

def calculateFumblesPerGame(combinedFumbleData):
    for key, playerData, in combinedFumbleData.items():
        fumbles = playerData['Fumbles']
        gamesPlayed = playerData['Games Played']
        fumblesPerGame = safeZeroDivision(fumbles, gamesPlayed)

        playerData['Fumbles Per Game'] = fumblesPerGame

    return

def safeZeroDivision(numerator, denominator):
    try:
        return "%.4f" % (numerator/denominator)
    except ZeroDivisionError:
        return 0