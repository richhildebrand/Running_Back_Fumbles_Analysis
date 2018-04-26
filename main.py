import sys
sys.path.append('./code')
import code.csvHelper as csvHelper
import code.fumbleDataHelper as fumbleDataHelper
import code.dictionaryHelper as dictionaryHelper

print ('Starting import')
collectAfterYear = 2010
numberOfRowsToRead = sys.maxsize
fumbleData = csvHelper.readRowsFrom(numberOfRowsToRead, './stats/Career_Stats_Fumbles.csv')
fumbleData = fumbleDataHelper.filterAtLeast(fumbleData, 'Year', collectAfterYear)

rushingData = csvHelper.readRowsFrom(numberOfRowsToRead, './stats/Career_Stats_Rushing.csv')
rushingData = fumbleDataHelper.filterAtLeast(rushingData, 'Year', collectAfterYear)

columnDefinitions = fumbleDataHelper.getOutputFormat()
combinedData = fumbleDataHelper.combineAllPlayerData(fumbleData, {})
combinedData = fumbleDataHelper.combineAllPlayerData(rushingData, combinedData)
combinedData = fumbleDataHelper.filterAtLeast(combinedData, 'Rushing Attempts', 200)

combinedData = fumbleDataHelper.calculateXperY(combinedData, 'Fumbles Per Game', 'Rushing Fumbles', 'Games Played Fumbles')
combinedData = fumbleDataHelper.calculateXperY(combinedData, 'Carries Per Fumble', 'Rushing Attempts', 'Rushing Fumbles')
combinedData = fumbleDataHelper.calculateXperY(combinedData, 'Yards Per Fumble', 'Rushing Yards', 'Rushing Fumbles')
combinedData = fumbleDataHelper.calculateXperY(combinedData, 'Yards Per Carry', 'Rushing Yards', 'Rushing Attempts')

combinedData = dictionaryHelper.addStandardDeviation(combinedData, 'Yards Per Fumble')
combinedData = dictionaryHelper.addStandardDeviation(combinedData, 'Yards Per Carry')

csvHelper.writeRows(combinedData, columnDefinitions, './output/results.csv')
print ('Ending import')