import os

import csv

csvpath = os.path.join("Resources", "election_data.csv")

#Create dictionary for candidates:
candidates = {}

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next (csvreader)

#Set variables:
    total_votes=0

#Create loop through rows:
    for row in csvreader:

        #Calculate Total Votes (the number of rows):
        total_votes = total_votes + 1

        #Use dictionary to find/store candidates:
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
    

#Print Summary Analysis:
print('Election Results')
print('--------------------------')
print(f'Total Votes: {total_votes}')
print('--------------------------')

#Use dictionary to loop through and find vote counts and winner:
winner = 0
winner_candidate = ''
for key, value in candidates.items():
    print(f'{key}: {round(value/total_votes*100,3)}% ({value})')
    
    print('--------------------------')
    if value > winner:
        winner = value
        winner_candidate = key
print(f'Winner: {winner_candidate}')
print('--------------------------')

#Output to text file:
output_path = os.path.join("Analysis", "results.txt")

with open(output_path, 'w') as f:
    f.write("Election Results\n")
    f.write("-------------------------------------\n")
    f.write(f'Total Votes: {total_votes}\n')
    f.write("-------------------------------------\n")
    for key, value in candidates.items():
        f.write(f'{key}: {round(value/total_votes*100,3)}% ({value})\n')
    f.write("-------------------------------------\n")
    f.write(f'Winner: {winner_candidate}\n')
    f.write("-------------------------------------\n")