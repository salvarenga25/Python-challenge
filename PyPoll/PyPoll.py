#Import necessary libraries
import os
import csv

#Variables to keep the path of files to be used
csvOpen = os.path.join(".","PyPoll","Resources", "election_data.csv")
csvOut = os.path.join(".","PyPoll","Analysis","analysis.txt")
count = 0

#Dictionaries to be used
charlesCas = []
dianaDe = []
raymonAnth = []

#File to be read
with open(csvOpen, encoding="UTF-8") as csvIn:
    csvreader = csv.reader(csvIn,delimiter=',')

    header = next(csvreader)
    #adding IDs to each candidate
    for row in csvreader:
        count = count + 1
        if  row[2]=="Charles Casper Stockham":
            charlesCas.append(row[0])

        elif row[2] == "Diana DeGette":
            dianaDe.append(row[0])

        elif row[2] == "Raymon Anthony Doane":
            raymonAnth.append(row[0])    


#Variables to be used on the analysis
percentageCharles = round((len(charlesCas)/count) * 100,3)
percentageDiana  =  round((len(dianaDe)/count) * 100,3)
percentageRaymon =  round((len(raymonAnth)/count) * 100,3)

#Dictionary containing the candidates names and percentage after data has been processed
#Used to be easier to find who has the greatest percentage
resultsDict = {
    "Charles Casper Stockham": percentageCharles,
    "Diana DeGette": percentageDiana,
    "Raymon Anthony Doane":percentageRaymon
    }

#Printing the results in the terminal
print("\nElection Results")
print("\n--------------------")
print("\nTotal Votes: " + str(count) + " "+str())
print("Charles Casper Stockham: " + str(percentageCharles) + "%" + " (" + str(len(dianaDe)) + ")" )
print("Diana DaGette: " + str(percentageDiana) + "%" + " (" + str(len(dianaDe)) + ")" )
print("Raymon Anthony Doane: " + str(percentageRaymon) + "%" + " (" + str(len(raymonAnth)) + ")" )
print("\n--------------------")
print("\nWinner: " + max(resultsDict, key = resultsDict.get))
print("\n--------------------\n")

#Printing out to the output file with proper formatting
with open(csvOut, "w") as outFile:
    outFile.write("Election Analysis\n") 
    outFile.write("\n---------------------------")
    outFile.write("\n\nTotal Votes: " + str(count) + " "+str())           
    outFile.write("\n\n----------------------------")
    outFile.write("\nCharles Casper Stockham: " + str(percentageCharles) + "%")
    outFile.write("\nDiana DaGette: " + str(percentageDiana) + "%")
    outFile.write("\nRaymon Anthony Doane: " + str(percentageRaymon) + "%")
    outFile.write("\n\n----------------------------")
    outFile.write("\n\nWinner: " +  max(resultsDict, key = resultsDict.get) )
    outFile.write("\n\n----------------------------")