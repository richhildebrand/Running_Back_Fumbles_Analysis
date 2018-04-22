from .dictionaryHelper import addOrReplaceStringKeyValuePair, addIntegerKeyValuePair

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

    #calculateFumblesPerGame(combinedData)
    return combinedData

def combinePlayerData(row, allPlayers):
    playerId = row['Player Id']
    player = allPlayers.get(playerId, {})

    addOrReplaceStringKeyValuePair(player, row, 'Player Id')
    addOrReplaceStringKeyValuePair(player, row, 'Name')
    addIntegerKeyValuePair(player, row, 'Games Played Fumbles')
    addIntegerKeyValuePair(player, row, 'Games Played Rushing')
    addIntegerKeyValuePair(player, row, 'Fumbles')
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