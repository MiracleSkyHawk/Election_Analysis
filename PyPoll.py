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

# Open the election results and read the file.
# election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:
    
    # To do: perform analysis
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

    # # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)

    # How to print out any row
    # csvFileArray = []
    # for row in file_reader:
    #     csvFileArray.append(row)
    # print(csvFileArray[0])


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, 'w') as txt_file:
    # Write three counties to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
