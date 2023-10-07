# Import dependencies 
import os
import csv

# Set path for file 
csv_path = os.path.join('Downloads', 'election_data.csv')

#creating variables 
candidate_vote_cnt = {}
total_votes = 0

# Open the CSV using the UTF-8 encoding
with open(csv_path, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

# Loop through looking for total votes
    for row in csvreader:
        candidate_name = row[2]
        total_votes += 1
        if candidate_name not in candidate_vote_cnt:
            candidate_vote_cnt[candidate_name]=0
        candidate_vote_cnt[candidate_name] += 1
        total_votes = sum(candidate_vote_cnt.values())
    
#total % of votes for each candidate 
    candidate_vote_cnt["Charles Casper Stockham"] = ((candidate_vote_cnt["Charles Casper Stockham"]/total_votes)*100,3)
    candidate_vote_cnt["Diana DeGette"] = ((candidate_vote_cnt["Diana DeGette"]/total_votes)*100,3)
    candidate_vote_cnt["Raymon Anthony Doane"] = ((candidate_vote_cnt["Raymon Anthony Doane"]/total_votes)*100,3)

 # Calculate which candidate won
    candidate_winner = max(candidate_vote_cnt, key=candidate_vote_cnt.get)

#Results 
print("Election Results\n")
print("----------------------------\n")
print("Total Votes:" + str(total_votes) + "\n")
print("-----------------------------\n")
print("Charles Casper Stockham: " + str(candidate_vote_cnt["Charles Casper Stockham"]) + "% " + str(candidate_vote_cnt["Charles Casper Stockham"]) + "\n") 
print("Diana DeGette: " + str(candidate_vote_cnt["Diana DeGette"]) + "% " + str(candidate_vote_cnt["Diana DeGette"]) + "\n") 
print("Raymon Anthony Doane: " + str(candidate_vote_cnt["Raymon Anthony Doane"]) + "% " + str(candidate_vote_cnt["Raymon Anthony Doane"]) + "\n") 
print("-------------------\n")
print("Winner: " + str(candidate_winner) + "\n")
print("-------------------\n")

# Print to txt file
output_result = os.path.join("Documents", "GitHub", "python-challenge", "analysis", "results.txt")

with open(output_result, "w") as txt_file:
    txt_file.write("Election Results" + "\n")
    txt_file.write("-------------------\n")
    txt_file.write("Total Vote: " + str(total_votes) + "\n")
    txt_file.write("-------------------\n")
    txt_file.write("Charles Casper Stockham: " + str(candidate_vote_cnt["Charles Casper Stockham"]) + "% " + str(candidate_vote_cnt["Charles Casper Stockham"]) + "\n") 
    txt_file.write("Diana DeGette: " + str(candidate_vote_cnt["Diana DeGette"]) + "% " + str(candidate_vote_cnt["Diana DeGette"]) + "\n")
    txt_file.write("Raymon Anthony Doane: " + str(candidate_vote_cnt["Raymon Anthony Doane"]) + "% " + str(candidate_vote_cnt["Raymon Anthony Doane"]) + "\n")
    txt_file.write("-------------------\n")
    txt_file.write("Winner: " + str(candidate_winner) + "\n")
    txt_file.write("-------------------\n")