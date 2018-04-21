import csvHelper as csvHelper
import fumbleDataHelper as fumbleDataHelper

print ('Starting import')
rowsInMemory = csvHelper.readRowsFrom(100, '../stats/Career_Stats_Fumbles.csv')

combinedFumbleData = {}
for rowNumber, rowData, in rowsInMemory.items():
    player = fumbleDataHelper.updatePlayerInCollection(rowData, combinedFumbleData)
#print(combinedFumbleData)

csvHelper.writeRowsFromNestedDictionary(combinedFumbleData, '../output/results.csv')
print ('Ending import')