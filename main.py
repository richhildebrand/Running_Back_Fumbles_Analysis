import sys
sys.path.append('./code')
import code.csvHelper as csvHelper
import code.fumbleDataHelper as fumbleDataHelper

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
combinedData = fumbleDataHelper.filterAtLeast(combinedData, 'Rushing Attempts', 50)

combinedData = fumbleDataHelper.calculateXperY(combinedData, 'Fumbles Per Game', 'Fumbles', 'Games Played Fumbles')
combinedData = fumbleDataHelper.calculateXperY(combinedData, 'Carries Per Fumble', 'Rushing Attempts', 'Fumbles')
combinedData = fumbleDataHelper.calculateXperY(combinedData, 'Yards Per Fumble', 'Rushing Yards', 'Fumbles')
combinedData = fumbleDataHelper.calculateXperY(combinedData, 'Yards Per Carry', 'Rushing Yards', 'Rushing Attempts')
csvHelper.writeRows(combinedData, columnDefinitions, './output/results.csv')
print ('Ending import')