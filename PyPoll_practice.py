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


#Add our dependencies.
import csv
import os
#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Declare a new list. This is in order to make a list of the candidates from the data:
candidate_options = []

# Declare a new dictionary so that we can count the votes separately for each candidate. 
candidate_votes = {}

# Winning candidate and winning count tracker:
# Declare a variable winning candidate
winning_candidate = ""

# Declare the winning count variable as zero
winning_count = 0

# Declare the winning percentage variable as zero
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row. We want to skip the header row when reading the data.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count. 
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]
            
        # Check if a candidate's name is not in the list. if its not, add it to the list. 
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
       
        # Add a vote to that candidate's count. This is the format for adding the number of times a certain key (a specific candidate name) appears in the candidate_votes dictionary. or in other words checking the value of that key. 
        candidate_votes[candidate_name] +=1

        
# Determine the percentage of votes for each candidate by looping through the count
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate. Here we are creating a new variable: vote
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print the candidate name and percentage of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine the winning vote count and candidate
    # Determine if the votes is greater than the winning count. 
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent = 
        #vote_percentage. 
        winning_count = votes
        winning_percentage = vote_percentage
        # Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name


# Print the total votes.
print(total_votes)
# Print all the candidates names from the data. Or in other words print the candidate list 
print(candidate_options)
# Print the candidate vote dictionary. 
print(candidate_votes)

winning_candidate_summary = (
    f"----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"----------------------------\n"
)
print(winning_candidate_summary)


