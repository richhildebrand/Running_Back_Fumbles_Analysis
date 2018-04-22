import dictionaryHelper as dictionaryHelper

def getOutputFormat():
    headers = []
    headers[0] = 'Player Id'
    headers[1] = 'Name'
    headers[2] = 'Games Played'
    headers[3] = 'Fumbles'
    headers[4] = 'Rushing Attempts'
    headers[5] = 'Rushing Yards'

    return headers

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

    dictionaryHelper.addOrReplaceStringKeyValuePair(player, row, 'Player Id')
    dictionaryHelper.addOrReplaceStringKeyValuePair(player, row, 'Name')
    dictionaryHelper.addIntegerKeyValuePair(player, row, 'Games Played')
    dictionaryHelper.addIntegerKeyValuePair(player, row, 'Fumbles')

    allPlayers[playerId] = player
    return

def combinePlayerRushingData(row, allPlayers):
    playerId = row['Player Id']
    player = allPlayers.get(playerId, {})

    dictionaryHelper.addIntegerKeyValuePair(player, row, 'Rushing Attempts')
    dictionaryHelper.addIntegerKeyValuePair(player, row, 'Rushing Yards')

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