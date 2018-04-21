import csvHelper as csvHelper
import fumbleDataHelper as fumbleDataHelper

print ('Starting import')
rowsInMemory = csvHelper.readRowsFrom(100, '../stats/Career_Stats_Fumbles.csv')
dataToPrint = fumbleDataHelper.updatePlayersInCollection(rowsInMemory)
csvHelper.writeRowsFromNestedDictionary(dataToPrint, '../output/results.csv')
print ('Ending import')