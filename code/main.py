import csvHelper as csvHelper
import dictionaryHelper as dictionaryHelper
import fumbleDataHelper as fumbleDataHelper

print ('Starting import')
numberOfRowsToRead = 5
fumbleData = csvHelper.readRowsFrom(numberOfRowsToRead, '../stats/Career_Stats_Fumbles.csv')
rushingData = csvHelper.readRowsFrom(numberOfRowsToRead, '../stats/Career_Stats_Rushing.csv')

combinedData = fumbleDataHelper.combineAllRushingData(rushingData, {})
combinedData = fumbleDataHelper.combineAllFumbleData(fumbleData, combinedData)

csvHelper.writeRowsFromNestedDictionary(combinedData, '../output/results.csv')
print ('Ending import')