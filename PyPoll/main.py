# Print output header
print("Election Results")
print("--------------------")

#Import dependencies
import os
import csv

# Establish filepath for CSV input file
csvpath = os.path.join("Resources", "election_data.csv")

# Open and read CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first
    csv_header = next(csvreader)

    #Define variables
    total_vote_count = 0
    candidates = []
    candidate_votes = {}

    # Calculate total votes
    for row in csvreader:
        total_vote_count += 1

        candidate = row[2]

        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1
    
    # Print total votes
    print(f'Total Votes: {total_vote_count}')
    print("--------------------")

    # Calculate votes and percentages by candidate
    for candidate in candidates:
        percentage = round(candidate_votes[candidate] / total_vote_count * 100, 3)
        
        # Print votes and percentages by candidate
        print(f'{candidate}: {percentage}% ({candidate_votes[candidate]})')

    print("--------------------")

    # Define max vote variable
    max_votes = max(candidate_votes.values())

    # Determine winner
    for candidate, winning_candidate_votes in candidate_votes.items():
        if winning_candidate_votes == max_votes:
            winner = candidate
    
    # Print winner
    print(f'Winner: {winner}')

# Establish filepath for txt output file
output_path = os.path.join("Analysis", "PyPoll_results.txt")

# Open txt file in "write" mode
with open(output_path, 'w') as txtfile:

    # Write results into txt file
    txtfile.write("Election Results"'\n')
    txtfile.write("--------------------"'\n')
    txtfile.write(f'Total Votes: {total_vote_count}''\n')
    txtfile.write("--------------------"'\n')
    for candidate in candidates:
        percentage = round(candidate_votes[candidate] / total_vote_count * 100, 3)
        txtfile.write(f'{candidate}: {percentage}% ({candidate_votes[candidate]})''\n')
    txtfile.write("--------------------"'\n')
    txtfile.write(f'Winner: {winner}')