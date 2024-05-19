import os
import csv
pwd = os.getcwd()
cwd = os.path.abspath(__file__)
dir_name =os.path.dirname(cwd)
csvpath = os.path.join(dir_name,'Resources',"election_data.csv")
print("________print working directory_______________________")
print(pwd)
print("_____current working directory________________")
print(cwd)
print("______________current directory name__________=")
print(dir_name)
print("____________path to election_data ________________________")
print(csvpath)
#--------------------------------------------------------------
#  path to text  file with the election results results
txtoutputpath = os.path.join(dir_name,'analysis',"Election_Results.txt")

# initialise and define variable used to analyse PyBank 
# count_ballot_IDs:the total number of ballot IDs included in the dataset : 
count_ballot_IDs = 0
# count_candidatess: Initializes an empty dictionary to hold the counts of BallotIDs for each candidate.
count_candidates = {}

#--------------------------------------------------------------
#Open the election_data.csv file. 
with open(csvpath, encoding='UTF-8') as election_file:
    csv_reader = csv.reader(election_file)
    # iterate through each row in election_data.csv file 
    # skip the title row
    next(csv_reader)
    for data_column in csv_reader:
        # columns are separated by a commas
        #columns = line.strip().split(',')
        candidate = data_column[2]

        if candidate in count_candidates:
            count_candidates[candidate] += 1
        else:
            count_candidates[candidate]  =1  
# 
        total_count_ballot_IDs = sum(count_candidates.values())  
 #display Election Resulsts       
print(f"---------------------------------------------------------------")
print(f"Election Results")
print(f"---------------------------------------------------------------")

print(f"---------------------------------------------------------------")
#  display the total number ballot IDs included in the dataset
print(f"Total Ballot IDs:", total_count_ballot_IDs )
# print the dictionary--> the count of the ballots for each candidate
for candidate, count_ballots in count_candidates.items():

    print(f"{candidate}:{count_ballots/total_count_ballot_IDs} {count_ballots} ")
# Find the candidate with the most BallotIDs
candidate_most_ballots = max(count_candidates, key=count_candidates.get)
print(f"---------------------------------------------------------------")
print("Winner:", candidate_most_ballots)
print(f"---------------------------------------------------------------")
print(f"---------------------------------------------------------------")
#-------------------------------------------------------------------------------------
 # Open the file using "write" mode. Specify the variable to hold the contents
with open(txtoutputpath, 'w') as txtoutputfile:
    #print to the text file the financial analysis calculated above
    txtoutputfile.write(f"\n")
    txtoutputfile.write(f"----------------------------------------------------\n")
    txtoutputfile.write(f"Election Results \n")
    txtoutputfile.write(f"----------------------------------------------------\n")
    txtoutputfile.write(f"\n")
    txtoutputfile.write(f"----------------------------------------------------\n")
    txtoutputfile.write(f"Total Ballot IDs: {total_count_ballot_IDs} \n")
    for candidate, count_ballots in count_candidates.items():
      
        txtoutputfile.write(f"{candidate}:{count_ballots/total_count_ballot_IDs} {count_ballots} \n")

    txtoutputfile.write(f"Winner:{candidate_most_ballots} \n")
        
    print(f"Results have been written to {txtoutputpath}.")
    
