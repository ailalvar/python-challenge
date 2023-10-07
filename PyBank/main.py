# Import dependencies 
import os
import csv

# Set path for file 
csv_path = os.path.join('Downloads', 'budget_data.csv')


# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
greatest_increase_in_profits = ["", 0]
greatest_decrease_in_profits = ["", 0]

# Read the CSV file
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Skip the header row
    header = next(csv_reader)
    
    for row in csv_reader:
        date = row[0]
        profit_loss = int(row[1])
        
        # Calculate total months and net total
        total_months += 1
        net_total += profit_loss
        
        # Calculate change in profit/loss
        change = profit_loss - previous_profit_loss
        changes.append(change)
        
        # Update the previous profit/loss for the next iteration
        previous_profit_loss = profit_loss
        
        # Check for greatest increase and decrease
        if change > greatest_increase_in_profits[1]:
            greatest_increase_in_profits = [date, change]
        elif change < greatest_decrease_in_profits[1]:
            greatest_decrease = [date, change]

# Calculate the average change
average_change = round(sum(changes) / len(changes), 2)

# Generate the analysis report
analysis_report = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase_in_profits[0]} (${greatest_increase_in_profits[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_in_profits[0]} (${greatest_decrease_in_profits[1]})\n"
)

# Print the analysis to the terminal
print(analysis_report)

# Path to the output text file
output_path = os.path.join(".", "Documents", "GitHub", "python-challenge", "analysis", "financial_analysis.txt")

# Export the results to a text file
with open(output_path, 'w') as output_file:
    output_file.write(analysis_report)
