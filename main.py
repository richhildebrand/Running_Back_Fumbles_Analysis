import sys
sys.path.append('./code')
import code.csvHelper as csvHelper
import code.fumbleDataHelper as fumbleDataHelper

print ('Starting import')
numberOfRowsToRead = 5
fumbleData = csvHelper.readRowsFrom(numberOfRowsToRead, './stats/Career_Stats_Fumbles.csv')
rushingData = csvHelper.readRowsFrom(numberOfRowsToRead, './stats/Career_Stats_Rushing.csv')

columnDefinitions = fumbleDataHelper.getOutputFormat()
combinedData = fumbleDataHelper.combineAllRushingData(rushingData, {})
combinedData = fumbleDataHelper.combineAllFumbleData(fumbleData, combinedData)

csvHelper.writeRows(combinedData, columnDefinitions, '../output/results.csv')
print ('Ending import')