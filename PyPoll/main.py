print("Financial Analysis")
print("--------------------")

import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    total_vote_count = 0
    candidates = []
    candidate_votes = {}

    for row in csvreader:
        total_vote_count += 1

        candidate = row[2]

        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1
    
    print(f'Total Votes: {total_vote_count}')
    print("--------------------")

    for candidate in candidates:
        percentage = round(candidate_votes[candidate] / total_vote_count * 100, 2)
        print(f"{candidate}: {percentage}% ({candidate_votes[candidate]})")

    print("--------------------")

    max_votes = max(candidate_votes.values())

    for candidate, candidate_votes in candidate_votes.items():
        if candidate_votes == max_votes:
            winning_candidate = candidate
    
    print(f'Winner: {winning_candidate}')