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
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate. Here we are creating a new variable: vote
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")


# Print the total votes.
print(total_votes)
# Print all the candidates names from the data. Or in other words print the candidate list 
print(candidate_options)
# Print the candidate vote dictionary. 
print(candidate_votes)



