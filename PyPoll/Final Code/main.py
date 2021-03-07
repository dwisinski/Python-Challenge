import os
import csv

# import data csv file
election_data = os.path.join("..", "Resources", "election_data.csv")

# set starting variables to 0
total_votes = 0
candidate0_votes = 0
candidate1_votes = 0
candidate2_votes = 0
candidate3_votes = 0

# create list to store candidate name values
candidate_list = []

# open the csv file for reading
with open(election_data, "r", encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip header row
    csv_header = next(csvreader)

    # iterate through all rows in csv file
    for row in csvreader:
        # count number of votes in data
        total_votes +=1

        # set candidate as value of row in column 2
        candidate = (row[2])

        # add all candidate values to list
        candidate_list.append(candidate)

        # convert list to set to remove duplicate values, convert back to alphabetized list
        candidate_list = sorted(list(set(candidate_list)))

        # calculate incremental vote counts for each candidate
        if (row[2]) == candidate_list[0]:
            candidate0_votes +=1
        elif (row[2]) == candidate_list[1]:
            candidate1_votes +=1
        elif (row[2]) == candidate_list[2]:
            candidate2_votes +=1
        elif (row[2]) == candidate_list[3]:
            candidate3_votes +=1

# create dictionary of candidate and corresponding vote pairs
candidatedict = {candidate_list[0]: candidate0_votes, candidate_list[1]: candidate1_votes, candidate_list[2]: candidate2_votes, candidate_list[3]: candidate3_votes}

# calculate the percentage of total votes for each candidate and round to two decimal places
pct_c0 = "{:.2%}".format(candidate0_votes / total_votes)
pct_c1 = "{:.2%}".format(candidate1_votes / total_votes)
pct_c2 = "{:.2%}".format(candidate2_votes / total_votes)
pct_c3 = "{:.2%}".format(candidate3_votes / total_votes)

# set winner as the dictionary key with corresponding max value
winner = max(candidatedict, key=candidatedict.get)

# print output to terminal
print(f"Election Results:")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{candidate_list[0]}: {pct_c0} {candidate0_votes}")
print(f"{candidate_list[1]}: {pct_c1} {candidate1_votes}")
print(f"{candidate_list[2]}: {pct_c2} {candidate2_votes}")
print(f"{candidate_list[3]}: {pct_c3} {candidate3_votes}")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# create output txt file
output_file = os.path.join("..", "Analysis", "final_output.txt")

# print output as data to txt file
with open(output_file, "w", encoding='utf8') as textfile:
    textfile.write(f"Election Results:\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("-------------------------\n")
    textfile.write(f"{candidate_list[0]}: {pct_c0} {candidate0_votes}\n")
    textfile.write(f"{candidate_list[1]}: {pct_c1} {candidate1_votes}\n")
    textfile.write(f"{candidate_list[2]}: {pct_c2} {candidate2_votes}\n")
    textfile.write(f"{candidate_list[3]}: {pct_c3} {candidate3_votes}\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("-------------------------\n")
    textfile.close()