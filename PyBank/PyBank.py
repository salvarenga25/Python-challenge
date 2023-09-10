import csv
import os

csvOpen = os.path.join(".","PyBank","Resources", "budget_data.csv")
#csvpath='/Users/Guara/Documents/Challenges/python-challenge/PyBank/Resources/budget_data.csv'
#PyBank/Resources/budget_data.csv
#df = pd.read_csv(csvOpen, encoding='UTF-8')
#df.head()

with open(csvOpen) as inputFile:
    count = 0
    total = 0
    csvreader = csv.reader(inputFile, delimiter=',')
    header = next(csvreader)
    GreatestIncrease = 0
    GreatestDecrease = 0
    GreatestIncreaseMonth = ''
    GreatestIncreaseMonth = ''
    yearDict = []
    balanceDict = []
    totalDiff = 0


    #Reading the csv
    for row in csvreader:
        count = count + 1
        total = total + int(row[1])
        yearDict.append(row[0])
        balanceDict.append(row[1])
        
    #Iterate through both dictonaries to properly obtain max and min increase in profits    
    for i  in range(0,count-1): 

        temp = int(balanceDict[i+1]) - int(balanceDict[i])
        totalDiff = totalDiff + temp
        if temp > GreatestIncrease:
                GreatestIncrease = temp
                GreatestIncreaseMonth = yearDict[i+1]
        if temp < GreatestDecrease:
                GreatestDecrease = temp   
                GreatestDecreaseMonth = yearDict[i+1]
        


    avgDiff = totalDiff/(count-1)
        #print(row)
    round(avgDiff,2)

    average = total/(count-1)    
    print("Financial Analysis")
    print("---------------------------")    
    print("Total Months: " + str(count))
    print("Total: $" + str(total))
    print("Average Change: $" + str(round(avgDiff,2)))
    print("Greatest Increase in Profits: " + GreatestIncreaseMonth + " " + str(GreatestIncrease))
    print("Greatest Decrease in Profits: " + GreatestDecreaseMonth + " " +  str(GreatestDecrease))
    print("Total Diff: " + str(totalDiff))
   # print(str(avgDiff))
    print("")

    print(yearDict)
    print(balanceDict)
    


    #PyBank/Resources/budget_data.csv