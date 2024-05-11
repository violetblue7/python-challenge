# Modules
import csv

# File path
csvpath = "PyPoll/Resources/election_data.csv"

# Open the CSV file
with open(csvpath, encoding='UTF-8') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Variables (Numerical Values and Dictionary)
    total_votes = 0
    candidate_votes = {}

    # Loop over the data to calculate the required values
    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        # Count the votes for each candidate on the list
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

    # Calculate the percentage of votes each candidate won
    percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

    # Find the winner based on the popular vote
    winner = max(candidate_votes, key=candidate_votes.get)

# Define the output variable with the formatted election analysis results per assigment results

output = f"""Election Results

-------------------------

Total Votes: {total_votes}

-------------------------
"""

# Add two spaces for spacing
output += "  \n"

# Iterate over candidate votes to include in the output
for candidate, votes in candidate_votes.items():
    output += f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n"
    output += "  \n"  # Add two spaces after each candidate

# Add two spaces for spacing
output += "  \n"

output += f"""-------------------------

Winner: {winner}

-------------------------
"""

# Print the output
print(output)

# Write the output to a text file
with open("PyPoll/analysis/pypoll.txt", 'w') as f:
    f.write(output)
