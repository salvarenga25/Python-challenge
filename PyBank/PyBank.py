#import libraries to be used
import csv
import os

#Files to be used for reading and writing
csvOpen = os.path.join(".","PyBank","Resources", "budget_data.csv")
csvOut = os.path.join(".","PyBank","Analysis","analysis.txt")

#Variable declaration to be used for the analysis
GreatestIncrease = 0
GreatestDecrease = 0
GreatestIncreaseMonth = ''
GreatestIncreaseMonth = ''
avgDiff = 0 
totalDiff = 0


#We will spread the csv data into two sets for better easier manipulation
yearDict = []       
balanceDict = []    

#Starting to read the file 
with open(csvOpen) as inputFile:
    count = 0
    total = 0
    csvreader = csv.reader(inputFile, delimiter=',')
    header = next(csvreader)
   


    #Reading the csv
    for row in csvreader:
        count = count + 1
        total = total + int(row[1])
        yearDict.append(row[0])
        balanceDict.append(row[1])
        
    #Iterate through both sets to properly obtain max and min change in profits/loss    
    for i  in range(0,count-1): 
        #We use range 0 to count - 1 because we are calculating by profit/loss of the next month - profit/loss of current month
        #so we need to compare the next item in the set, if we put only count as the las range, we will suffer of Index Out of Bounds error 
        #temp variable will contain the difference from one month to another
        temp = int(balanceDict[i+1]) - int(balanceDict[i])
        totalDiff = totalDiff + temp

        #We analyze if the current difference is either bigger than the current max or lower than the current minimum change
        #we also want to grab the proper month/year 
        if temp > GreatestIncrease:
                GreatestIncrease = temp
                GreatestIncreaseMonth = yearDict[i+1]
        if temp < GreatestDecrease:
                GreatestDecrease = temp   
                GreatestDecreaseMonth = yearDict[i+1]
        

    #Calculating the average change
    avgDiff = totalDiff/(count-1)


#Printing the requested analysis into the console
print("\nFinancial Analysis\n")
print("---------------------------\n")    
print("Total Months: " + str(count))
print("Total: $" + str(total))
print("Average Change: $" + str(round(avgDiff,2)))
print("Greatest Increase in Profits: " + GreatestIncreaseMonth + " ($" + str(GreatestIncrease)+ ")")
print("Greatest Decrease in Profits: " + GreatestDecreaseMonth + " ($" +  str(GreatestDecrease) + ")\n")



#opening and writing a txt file to output the analysis, the file is in the "Analysis" folder
with open(csvOut, "w") as outFile:
    outFile.write("Financial Analysis\n\n") 
    outFile.write("---------------------------\n")
    outFile.write("\nTotal Months: " + str(count))           
    outFile.write("\nTotal: $" + str(total))
    outFile.write("\nAverage Change: $" + str(round(avgDiff,2)))
    outFile.write("\nGreatest Increase in Profits: " + GreatestIncreaseMonth + " ($" + str(GreatestIncrease) + ")")
    outFile.write("\nGreatest Decrease in Profits: " + GreatestDecreaseMonth + " ($" +  str(GreatestDecrease) + ")")
   
    


    

