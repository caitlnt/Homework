
#python CTa-HW03-Pypoll.py

#C:\Users\CNT\Documents\My Docs\Data Analytics\Week 03\Homework 03

import os
import csv

#gets election data file
csvfile = os.path.join("Resources", "election_data_2.csv")
newcsvfile = os.path.join("Resources", "election_reults.csv")

#Calculations
votecount =  0    # total votes
candlist = []   # list of candidates
candvotes = {}    # votes for each candidate


with open(csvfile, "r") as election_data:
	csvreader = csv.DictReader(election_data)

	for row in csvreader:
		votecount += 1
		if row ["Candidate"] not in candlist:
			candlist.append(row["Candidate"])
			candvotes[row["Candidate"]]=1
		elif row["Candidate"] in candlist:
			candvotes[row["Candidate"]] += 1

print(" ")
print(" ")
print("Election Results")
print("----------------")
print("Total Votes:  " + str(votecount))
print("----------------")
print(candvotes)
#print(votecount)
#print(candlist)
#print(candvotes)

