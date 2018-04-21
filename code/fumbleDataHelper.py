import dictionaryHelper as dictionaryHelper

def updatePlayerInCollection(row, allPlayers):
    playerId = row['Player Id']
    player = allPlayers.get(playerId, {})

    dictionaryHelper.addOrReplaceStringKeyValuePair(player, row, 'Player Id')
    dictionaryHelper.addOrReplaceStringKeyValuePair(player, row, 'Name')
    dictionaryHelper.addIntegerKeyValuePair(player, row, 'Games Played')
    dictionaryHelper.addIntegerKeyValuePair(player, row, 'Fumbles')

    allPlayers[playerId] = player
    return