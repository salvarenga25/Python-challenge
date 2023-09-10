import csv
import os
csvOpen = os.path.join(".","PyBank","Resources", "budget_data.csv")
#csvpath='/Users/Guara/Documents/Challenges/python-challenge/PyBank/Resources/budget_data.csv'
#PyBank/Resources/budget_data.csv
with open(csvOpen) as inputFile:
    count = 0
    total = 0
    csvreader = csv.reader(inputFile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        count = count + 1
        total = total + int(row[1])
        print(row)
    print(count)
    print(total)



    #PyBank/Resources/budget_data.csv