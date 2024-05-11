# Modules
import csv

# File path
csvpath = "PyBank/Resources/budget_data.csv"

# Call the funtion to get the total number of rows for months using built-in methods 
def count_rows (data):
    return len(data)

# Open the CSV file
with open(csvpath, encoding= 'UTF-8') as csvfile:
# Create a CSV reader object
    csvreader = csv.reader(csvfile, delimiter=",")

    # Variables
    total_months = 0
    net_total = 0
    changes = []
    greatest_increase = 0
    greatest_decrease = 0

    # Skip the header row
    next(csvreader)

    # Loop over the data to calculate the required values
    for row in csvreader:
        total_months += 1
        net_total += int(row[1])

        # Calculate changes and find logic test greatest increase/decrease applying conditionals
        if total_months > 1:
            change = int(row[1]) - int(prev_row[1])
            changes.append(change)
            
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0]

        prev_row = row  # Store the current row for the next iteration


# Calculate the average change
average_change = sum(changes) / len(changes) 

        # Other formats to present the outcome with code explained
        # print("Financial Analysis")
        # print("----------------------------")
        # print(f"Total Months: {total_months}")
        # print(f"Total: ${net_total}")
        # print(f"Average Change: ${average_change:.2f}")
        # print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
        # print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
        # Adding spaces between outcomes with a code shown in the pypoll exercise


# Define the output variable with the formatted financial analysis results to show as requested in HW
output = f"""Financial Analysis

----------------------------

Total Months: {total_months}

Total: ${net_total}

Average Change: ${average_change:.2f}

Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})

Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})
"""
# Print the output
print(output)

# Write the output to a text file
with open("PyBank/analysis/pybank.txt", 'w') as f:
    f.write(output)