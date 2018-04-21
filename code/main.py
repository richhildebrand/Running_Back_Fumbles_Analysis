print ('Starting import')

import csv

with open('../stats/Career_Stats_Fumbles.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for i,row in enumerate(reader):
        print(row['Name'], row['Position'], row['Fumbles'])
        if(i >= 9):
            break


print ('Ending import')