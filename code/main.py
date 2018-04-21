print ('Starting import')
import csv

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

stopAtRow = 100
combinedFumbleData = {}
with open('../stats/Career_Stats_Fumbles.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for rowNumber,rowData in enumerate(reader):
        player = updatePlayerInCollection(rowData, combinedFumbleData)
        if(rowNumber > stopAtRow):
            break

print (combinedFumbleData)
with open('../output/results.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for playerId, playerStats in combinedFumbleData.items():
            writer.writerow([playerId])


print ('Ending import')