
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period


#Script 1
#The total number of months included in the dataset the data set is in the resources folder, 
# the month are in the first column
# open the file 
# loop for each row
# increament the counter to count the number of months.
# print the total count.

#----------------Script One Begin --------------------------------------------#
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    recordCounter = 0 

    # Read each row of data after the header
    for row in csvreader:
        recordCounter = recordCounter + 1
    
    print(" the total number of months are: " +str( recordCounter))

txtpath = os.path.join('.', 'analysis', 'PyBankReport.txt')

reportFile= open(txtpath,"w+")
reportFile.write("Financial Analysis")
reportFile.write("\r\n")

reportFile.write("----------------------------")
reportFile.write("\r\n")

reportFile.write("Total Months: " + str(recordCounter))
reportFile.write("\r\n")


#----------------Script One End -----------------------------------------------#


#Script 2
#The net total amount of "Profit/Losses" over the entire period
# loop through the dataset and add the profit/Loss values from column #2.
# print the net total profit/loss value over the entire period.

#Total: $38382578

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    profitLossValue =  int(0)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #for row in csvreader:
    # Read each row of data after the header
    for row in csvreader:
        profitLossValue = profitLossValue + int(row[1])

    print("Total profit Loss value is: " +str( profitLossValue))
reportFile.write("Total: " + str(profitLossValue))

reportFile.write("\r\n")


#Script 3
# The average of the changes in "Profit/Losses" over the entire period
# loop through the dataset and add the profit/Loss values from column #2.
# Solution 
    # Option #1 : divide the total of profit/loss value with the number of rows/records.
    # Optino #2 : is there any python library for csv function to get the average.

monthCounter = []
monthlyPNL =[]
monthlyProfitCange = []


with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    counter = 0
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #for row in csvreader:
    # Read each row of data after the header
    # idx, 
    for row in csvreader:
            monthCounter.append(row[0])
            monthlyPNL.append(int(row[1]))

           
    for i in range(len(monthlyPNL)-1):
        # Take the difference between two months and append to monthly profit change
        monthlyProfitCange.append(monthlyPNL[i+1]-monthlyPNL[i])


#Script 4
#The greatest increase in profits (date and amount) over the entire period
# loop through the dataset in column #2.
    # subtract the subsequent index/next month data from current index data/ current month.
    # beware of the edge conditions. 
    #   for the last record exit the loop.
    # compare the values and store the maximum increase and month in two different variables for results printing.
#Greatest Increase in Profits: Feb-2012 ($1926159)
# Obtain the max increase in montly profit change
maxIncreaseInProfit = max(monthlyProfitCange)


maxIncreaseInProfitIndex = monthlyProfitCange.index(maxIncreaseInProfit)
maxIncreaseInProfitMonth = str(monthCounter[maxIncreaseInProfitIndex+1])

print(f"Greatest Increase in Profits: {maxIncreaseInProfitMonth} ({str(maxIncreaseInProfit)})")

#reportFile.write("Greatest Increase in Profits: " + str(maxIncreaseInProfit))
reportFile.write(f"Greatest Increase in Profits: {maxIncreaseInProfitMonth} ({str(maxIncreaseInProfit)})")
reportFile.write("\r\n")



# Obtain the max decrease in montly profit change
maxReductionInProfit = min(monthlyProfitCange)

maxReductionInProfitIndex = monthlyProfitCange.index(maxReductionInProfit)
maxReductionInProfitMonth = str(monthCounter[maxReductionInProfitIndex+1])


print(f"Greatest Decrease in Profits: {maxReductionInProfitMonth} ({str(maxReductionInProfit)})")


reportFile.write(f"Greatest Decrease in Profits: {maxReductionInProfitMonth} ({str(maxReductionInProfit)})")

reportFile.write("\r\n")





#Script 5
#The greatest decrease in losses (date and amount) over the entire period
# loop through the dataset in column #2.
    # subtract the subsequent index/next month data from current index data/ current month.
    # beware of the edge conditions. 
    #   for the last record exit the loop.
    # compare the values and store the minimum increase and month in two different variables for results printing 
# adding comment
#Greatest Decrease in Profits: Sep-2013 ($-2196167)










