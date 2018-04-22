from .dictionaryHelper import addOrReplaceStringKeyValuePair, addIntegerKeyValuePair

def getOutputFormat():
    columnHeaders = { }
    columnHeaders['Player Id'] = { 'defaultValue': 'no value given'}
    columnHeaders['Name'] = { 'defaultValue': 'no value given'}
    columnHeaders['Games Played'] = { 'defaultValue': 'no value given'}
    columnHeaders['Fumbles'] = { 'defaultValue': 'no value given'}
    columnHeaders['Rushing Attempts'] = { 'defaultValue': 'no value given'}
    columnHeaders['Rushing Yards'] = { 'defaultValue': 'no value given'}

    return columnHeaders

def combineAllRushingData(collection, combinedData): 
    for rowNumber, rowData, in collection.items():
        combinePlayerRushingData(rowData, combinedData)

    #calculateFumblesPerGame(combinedData)
    return combinedData

def combineAllFumbleData(collection, combindedData): 
    for rowNumber, rowData, in collection.items():
        combinePlayerFumbleData(rowData, combindedData)

    #calculateFumblesPerGame(combindedData)
    return combindedData

def combinePlayerFumbleData(row, allPlayers):
    playerId = row['Player Id']
    player = allPlayers.get(playerId, {})

    addOrReplaceStringKeyValuePair(player, row, 'Player Id')
    addOrReplaceStringKeyValuePair(player, row, 'Name')
    addIntegerKeyValuePair(player, row, 'Games Played')
    addIntegerKeyValuePair(player, row, 'Fumbles')

    allPlayers[playerId] = player
    return

def combinePlayerRushingData(row, allPlayers):
    playerId = row['Player Id']
    player = allPlayers.get(playerId, {})

    addOrReplaceStringKeyValuePair(player, row, 'Player Id')
    addOrReplaceStringKeyValuePair(player, row, 'Name')
    addIntegerKeyValuePair(player, row, 'Rushing Attempts')
    addIntegerKeyValuePair(player, row, 'Rushing Yards')

    allPlayers[playerId] = player
    return

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