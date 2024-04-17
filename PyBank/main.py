print("Financial Analysis")
print("--------------------")

import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    month_count = 0
    total = 0
    change = 0
    changes = []
    previous_profit = 0
    change_month = []

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
    print(f'Total Months: {month_count}')
    print(f'Total: ${total}')
    average = round(sum(changes) / len(changes), 2)
    print(f'Average Change: ${average}')

    max_change = max(changes)
    min_change = min(changes)

    max_change_month = change_month[changes.index(max_change)]
    min_change_month = change_month[changes.index(min_change)]
  
    print(f'Greatest Increase in Profits: {max_change_month} (${max_change})')
    print(f'Greatest Decrease in Profits: {min_change_month} (${min_change})')