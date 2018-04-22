import sys
sys.path.append('./code')
import code.csvHelper as csvHelper
import code.fumbleDataHelper as fumbleDataHelper

print ('Starting import')
dataAfter = 2010
numberOfRowsToRead = sys.maxsize
fumbleData = csvHelper.readRowsFrom(numberOfRowsToRead, './stats/Career_Stats_Fumbles.csv')
fumbleData = fumbleDataHelper.filterAtLeast(fumbleData, 'Year', dataAfter)

rushingData = csvHelper.readRowsFrom(numberOfRowsToRead, './stats/Career_Stats_Rushing.csv')
rushingData = fumbleDataHelper.filterAtLeast(rushingData, 'Year', dataAfter)



collectAfterYear = 2010
columnDefinitions = fumbleDataHelper.getOutputFormat()
combinedData = fumbleDataHelper.combineAllPlayerData(fumbleData, {})
combinedData = fumbleDataHelper.combineAllPlayerData(rushingData, combinedData)

combinedData = fumbleDataHelper.filterAtLeast(combinedData, 'Rushing Attempts', 50)

csvHelper.writeRows(combinedData, columnDefinitions, './output/results.csv')
print ('Ending import')