# The data we need to retrieve
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Percentage of votes per candidate
# 4. Total votes per candidate 
# 5. Determine the winner of the election based on popular vote

#Assign a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'
#open the election results and read the file.
with open(file_to_load) as election_data:
#to do: perform analysis.
    print(election_data)

import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#open the election results and read the file.
with open(file_to_load) as election_data:
    # Print the file object.
    print(election_data)
#create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")
#using the open()function with the "w" mode we will write data to the file.
open(file_to_save, "w")

#create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
#using the with statement open the file as a text file. 
with open(file_to_save, "w") as txt_file:
    #write some data to the file.
    txt_file.write("Hello World\n")
    txt_file.write("Arapahoe, ")
    txt_file.write("Denver, ")
    txt_file.write("Jefferson. ")
    txt_file.write("Arapahoe, Denver, Jefferson\n")
    txt_file.write("Arapahoe\nDenver\nJefferson\n\n")
    txt_file.write("Counties in the Election\n")
    txt_file.write("--------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")


