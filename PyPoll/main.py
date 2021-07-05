#Create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

import os
import csv

csvpath=os.path.join('.','Resources','election_data.csv')

# The total number of votes cast

voterArray = []
countyArray=[]
candidateArray=[]

with open (csvpath) as csvfile:
    csvreader= csv.reader(csvfile,delimiter=',')
    #electorDict = {}
    
    csv_header=next(csvreader)
    for electionRecord in csvreader:
        voterArray.append(electionRecord[0])
        countyArray.append(electionRecord[1])
        candidateArray.append(electionRecord[2])
        #electorDict.items.  

totalVotesCasted=len(voterArray)
txtpath = os.path.join('.', 'analysis', 'PyPollReport.txt')

reportFile= open(txtpath,"w+")

print("Election Results")
reportFile.write("Election Results")

reportFile.write("\r\n")

print("----------------------------")
reportFile.write("----------------------------")

reportFile.write("\r\n")


print(f"Total Votes: {totalVotesCasted}")
reportFile.write(f"Total Votes: {totalVotesCasted}")

reportFile.write("\r\n")

print("----------------------------")
reportFile.write("----------------------------")

reportFile.write("\r\n")

 # A complete list of candidates who received votes
    

candidateSet = list(set(candidateArray))

candiateVotes=[]

for candidate in candidateSet:
    candiateVotes.append(candidateArray.count(candidate))

    
for i in range(len(candidateSet)):

    print(f"{candidateSet[i]}: {'{:.3%}'.format(candiateVotes[i]/totalVotesCasted)} ({candiateVotes[i]})")
    reportFile.write(f"{candidateSet[i]}: {'{:.3%}'.format(candiateVotes[i]/totalVotesCasted)} ({candiateVotes[i]})")
    
    reportFile.write("\r\n")

print("-------------------------\n")
reportFile.write("----------------------------")
reportFile.write("\r\n")

print(f"Winner: {candidateSet[candiateVotes.index(max(candiateVotes))]}")
reportFile.write(f"Winner: {candidateSet[candiateVotes.index(max(candiateVotes))]}")
reportFile.write("\r\n")

print("-------------------------\n")
reportFile.write("----------------------------")





