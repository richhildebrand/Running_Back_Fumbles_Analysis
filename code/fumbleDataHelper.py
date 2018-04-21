def getColumnValueOrZero(column, row):
    value = row[column]
    try:
        return int(value)
    except ValueError:
        return 0

def updatePlayerInCollection(row, collection):
    gamesPlayed = getColumnValueOrZero('Games Played', row)
    fumbles = getColumnValueOrZero('Fumbles', row)

    key = row['Player Id']
    player = collection.get(key, {})
    if (player):
        player['Games Played'] = player['Games Played'] + gamesPlayed
        player['Fumbles'] = player['Fumbles'] +  fumbles
        collection[key] = player
        return player

    player = {}
    player['Games Played'] = gamesPlayed
    player['Fumbles'] = fumbles
    collection[key] = player
    return player