import sys
sys.path.append('./code')
import code.csvHelper as csvHelper
import code.fumbleDataHelper as fumbleDataHelper

print ('Starting import')
numberOfRowsToRead = sys.maxsize
fumbleData = csvHelper.readRowsFrom(numberOfRowsToRead, './stats/Career_Stats_Fumbles.csv')
rushingData = csvHelper.readRowsFrom(numberOfRowsToRead, './stats/Career_Stats_Rushing.csv')

collectAfterYear = 2010
columnDefinitions = fumbleDataHelper.getOutputFormat()
combinedData = fumbleDataHelper.combineAllPlayerData(fumbleData, {}, collectAfterYear)
combinedData = fumbleDataHelper.combineAllPlayerData(rushingData, combinedData, collectAfterYear)

csvHelper.writeRows(combinedData, columnDefinitions, './output/results.csv')
print ('Ending import')