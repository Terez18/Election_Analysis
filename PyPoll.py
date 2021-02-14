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

# Track the winning candidate, vote count and percentage
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

    # Save the results to our text file. 
    with open(file_to_save, "w") as txt_file:

        # Print the final vote count to the terminal. 
        election_results = (
            f"\nElection Results\n"
            f"----------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-----------------------------\n")

        print(election_results, end="")

        # Save the final vote count to the text file. 
        txt_file.write(election_results)

       
        # Determine the percentage of votes for each candidate by looping through the count
        # Iterate through the candidate list.
        for candidate_name in candidate_votes:
            # Retrieve vote count of a candidate. Here we are creating a new variable: vote
            votes = candidate_votes[candidate_name]
            # Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100
            # Print the candidate name and percentage of votes.
            # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Print the candidates' results to the terminal. This includes each candidate name their voter count and percentage to the terminal. 
            candidate_results = (
                f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            print(candidate_results)
            # Save the results to our text file. 
            txt_file.write(candidate_results)


            # Determine the winning vote count and candidate
            # Determine if the votes is greater than the winning count. 
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percent = 
                #vote_percentage. 
                winning_count = votes
                winning_percentage = vote_percentage
                # Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name

        # Print the winning candidates' results to the terminal.
        winning_candidate_summary = (
            f"----------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"----------------------------\n"
        )
        print(winning_candidate_summary)

        # Save the winning candidate's name to the text file. 
        txt_file.write(winning_candidate_summary)



