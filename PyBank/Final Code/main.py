import os
import csv

# import data csv file
budget_data = os.path.join("..", "Resources", "budget_data.csv")

# set starting variables to 0
total_months = 0
total_profits = 0
prev_profits = 0
max_change = 0
min_change = 0

# create list to store change values
change = []

# open the csv file for reading
with open(budget_data, "r", encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip header row
    csv_header = next(csvreader)

    # iterate through all rows in csv file
    for row in csvreader:
        # count number of months in data
        total_months +=1

        # set profits as integer value of row in column[1]
        profits = int(row[1])

        # calculate and set total profits as incremental total of profits
        total_profits = total_profits + profits

        # calculate and set change in profits as profits less previous row's profits
        profits_change = profits - prev_profits

        # add change values to list
        change.append(profits_change)

        # reset as previous row's profits for next iteration
        prev_profits = int(row[1])

        # calculate and set greatest increase in profits (month and amount)
        if profits_change > max_change:
            max_change = profits_change
            max_month = row[0]

        # calculate and set greatest decrease in profits (month and amount)
        if profits_change < min_change:
            min_change = profits_change
            min_month = row[0]

    # remove first object from change list (no change)
    change.pop(0)

    # calculate sum total of change list values
    sum = sum(change)

    # calculate the mean of the total change in profits and round to two decimal places
    avg_change = round(sum / (total_months - 1),2)

    # print output to terminal
    print(f"Financial Analysis:")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Profits: $ {total_profits}")
    print(f"Average Change: $ {avg_change}")
    print(f"Greatest Increase in Profits: {max_month} $ {max_change}")
    print(f"Greatest Decrease in Profits: {min_month} $ {min_change}")

# create output txt file
output_file = os.path.join("..", "Analysis", "final_output.txt")

# print output as data to txt file
with open(output_file, "w", encoding='utf8') as textfile:
    textfile.write(f"Financial Analysis:\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total Profits: $ {total_profits}\n")
    textfile.write(f"Average Change: $ {avg_change}\n")
    textfile.write(f"Greatest Increase in Profits: {max_month} $ {max_change}\n")
    textfile.write(f"Greatest Decrease in Profits: {min_month} $ {min_change}\n")
    textfile.close()