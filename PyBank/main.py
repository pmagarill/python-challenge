# Print output header
print("Financial Analysis")
print("--------------------")

# Import dependencies
import os
import csv

# Establish filepath for CSV input file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open and read CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)

    # Define variables
    month_count = 0
    total = 0
    change = 0
    changes = []
    previous_profit = 0
    change_month = []
    
    # Calculate total months, total profit, and average change in profit
    for row in csvreader:
        profit = int(row[1])
        month = row[0]
        month_count += 1
        total += profit
        change = profit - previous_profit
        
        if previous_profit != 0:
            changes.append(change)
            change_month.append(str(month))

        previous_profit = profit
    
    average = round(sum(changes) / len(changes), 2)

    # Print results of total months, total profit, and average change in profit
    print(f'Total Months: {month_count}')
    print(f'Total: ${total}')
    print(f'Average Change: ${average}')

    # Define change variables
    max_change = max(changes)
    min_change = min(changes)

    # Calculate min and max monthly changes
    max_change_month = change_month[changes.index(max_change)]
    min_change_month = change_month[changes.index(min_change)]
  
    # Print results of min and max montly changes
    print(f'Greatest Increase in Profits: {max_change_month} (${max_change})')
    print(f'Greatest Decrease in Profits: {min_change_month} (${min_change})')

# Establish filepath for txt output file
output_path = os.path.join("Analysis", "PyBank_results.txt")

# Open txt file in "write" mode
with open(output_path, 'w') as txtfile:

    # Write results into txt file
    txtfile.write("Financial Analysis"'\n')
    txtfile.write("--------------------"'\n')
    txtfile.write(f'Total Months: {month_count}''\n')
    txtfile.write(f'Total: ${total}''\n')
    txtfile.write(f'Average Change: ${average}''\n')
    txtfile.write(f'Greatest Increase in Profits: {max_change_month} (${max_change})''\n')
    txtfile.write(f'Greatest Decrease in Profits: {min_change_month} (${min_change})')