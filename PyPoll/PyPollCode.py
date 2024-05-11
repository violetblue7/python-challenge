# Modules
import csv

# File path
csvpath = "PyPoll/election_data.csv"

# Open the CSV file
with open(csvpath, encoding= 'UTF-8') as csvfile:
# Create a CSV reader object
    csvreader = csv.reader(csvfile, delimiter=",")

   # Skip the header row
    next(csvreader)
    
    # Initialize variables (Numerical Values and Dictionary)
    total_votes = 0
    candidate_votes = {}
    
    # Iterate over the data to calculate the required values
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        
        # Count the votes for each candidate on the List
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the percentage of votes each candidate won
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Find the winner based on the popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {percentages[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
