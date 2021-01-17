# The data we need to retieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received botes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import datetime as dt
import random as rd
# import numpy as np
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
# election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:
    
    # To do: perform analysis
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    # print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    # How to print out any row
    # csvFileArray = []
    # for row in file_reader:
    #     csvFileArray.append(row)
    # print(csvFileArray[0])

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes)/float(total_votes) * 100
    print(f"{candidate_name}: received {vote_percentage:.1f}% ({votes:,})\n")
    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

# # Print the candidate list.
# print(candidate_options)

# # Print the total votes.
# print(total_votes)

# # Print the candidate vote dictionary.
# print(candidate_votes)

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, 'w') as txt_file:
    # Write three counties to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
