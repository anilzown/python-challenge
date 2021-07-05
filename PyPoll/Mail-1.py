
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

import os
import csv

csvpath=os.path.join('.','Resources','election_data.csv')

#Script 1
#The total number of months included in the dataset the data set is in the resources folder, 
# the month are in the first column
# open the file 
# loop for each row
# increament the counter to count the number of months.
# print the total count.
electionMonths = []
with open (csvpath) as csvfile:
    csvreader= csv.reader(csvfile,delimiter=',')
    
    csv_header=next(csvreader)
    for electionRecord in csvreader:
        electionMonthArr.append(relectionRecord[])

#Script 2
#The net total amount of "Profit/Losses" over the entire period
# loop through the dataset and add the profit/Loss values from column #2.
# print the net total profit/loss value over the entire period.



#Script 3
# The average of the changes in "Profit/Losses" over the entire period
# loop through the dataset and add the profit/Loss values from column #2.
# Solution 
    # Option #1 : divide the total of profit/loss value with the number of rows/records.
    # Optino #2 : is there any python library for csv function to get the average.

#Script 4
#The greatest increase in profits (date and amount) over the entire period
# loop through the dataset in column #2.
    # subtract the subsequent index/next month data from current index data/ current month.
    # beware of the edge conditions. 
    #   for the last record exit the loop.
    # compare the values and store the maximum increase and month in two different variables for results printing.

#Script 5
#The greatest decrease in losses (date and amount) over the entire period
# loop through the dataset in column #2.
    # subtract the subsequent index/next month data from current index data/ current month.
    # beware of the edge conditions. 
    #   for the last record exit the loop.
    # compare the values and store the minimum increase and month in two different variables for results printing 
# adding comment






