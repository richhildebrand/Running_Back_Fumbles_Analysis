import sys
sys.path.append('./code')
import code.csvHelper as csvHelper
import code.fumbleDataHelper as fumbleDataHelper

print ('Starting import')
numberOfRowsToRead = sys.maxsize
fumbleData = csvHelper.readRowsFrom(numberOfRowsToRead, './stats/Career_Stats_Fumbles.csv')
rushingData = csvHelper.readRowsFrom(numberOfRowsToRead, './stats/Career_Stats_Rushing.csv')

#combinedData = fumbleData.filterAtLeast(combinedData, 'Rushing Attempts', 50)


collectAfterYear = 2010
columnDefinitions = fumbleDataHelper.getOutputFormat()
combinedData = fumbleDataHelper.combineAllPlayerData(fumbleData, {})
combinedData = fumbleDataHelper.combineAllPlayerData(rushingData, combinedData)

combinedData = fumbleDataHelper.filterAtLeast(combinedData, 'Rushing Attempts', 50)

csvHelper.writeRows(combinedData, columnDefinitions, './output/results.csv')
print ('Ending import')