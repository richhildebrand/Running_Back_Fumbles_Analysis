import dictionaryHelper as dictionaryHelper

def updatePlayersInCollection(collection): 
    combinedFumbleData = {}
    for rowNumber, rowData, in collection.items():
        updatePlayerInCollection(rowData, combinedFumbleData)

    calculateFumblesPerGame(combinedFumbleData)
    return combinedFumbleData

def updatePlayerInCollection(row, allPlayers):
    playerId = row['Player Id']
    player = allPlayers.get(playerId, {})

    dictionaryHelper.addOrReplaceStringKeyValuePair(player, row, 'Player Id')
    dictionaryHelper.addOrReplaceStringKeyValuePair(player, row, 'Name')
    dictionaryHelper.addIntegerKeyValuePair(player, row, 'Games Played')
    dictionaryHelper.addIntegerKeyValuePair(player, row, 'Fumbles')

    allPlayers[playerId] = player
    return

def calculateFumblesPerGame(combinedFumbleData):
    for key, playerData, in combinedFumbleData.items():
        gamesPlayed = playerData['Games Played']
        fumbles = playerData['Fumbles']
        fumblesPerGame = safeZeroDivision(gamesPlayed, fumbles)

        playerData['Fumbles Per Game'] = fumblesPerGame

    return

def safeZeroDivision(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return 0