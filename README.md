# Election_Analysis

## Overview of Election Audit

A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election:

1. Calculate the voter turnout for each county
2. Calculate the percentage of votes from each county out of the total count.
3. Name the county with the highest turnout in this election. 
4. Calculate the total number of votes cast.
5. Get a complete list of candidates who received votes.
6. Calculate the total number of votes each candidate received. 
7. Calculate the percentage of votes each candidate won.
8. Determine the winner of the election based on popular vote.

---

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.53.1

---

## Link to Complete Code
![PyPoll_Challenge.py](PyPoll_Challenge.py)

---

## Election-Audit Results

Below are the congressional election outcomes including a description of how they were retrieved and calculated:

- There were 369,711 total number of votes cast in this congressional election. 
  
	- To calculate the total votes "total_votes" variable was initialized and started at zero:
 		```
		# Initialize a total vote counter.
		total_votes = 0
		```
	- The election_data file was opened to extract the data from it. "with open" command was used to eliminate the need to close the file and to make the code clean and concise:
		```
		# Read the csv
		with open(file_to_load) as election_data:
    			reader = csv.reader(election_data)
		```
    	
	- The header row was skipped using "next" so it was not counted in the total number of votes:	
		``````
			# Read the header
    			header = next(reader)
		``````

	- A for loop was created to iterate over the csv file and count the number of votes:
			
			```
			# For each row in the CSV file.
    			for row in reader:
			```
       - Votes counted to reach at the total number of 369,711. It is possible to use also another shorter version for this total_votes += 1.
				
				```
				# Add to the total vote count
        			total_votes = total_votes + 1
				```
- The county results were:
  - Jefferson county received 10.5% of the votes and 38,855 number of votes.
  - Denver county received 82.8% of the votes and 306,055 number of votes.
  - Arapahoe county received 6.7% of the votes and 24,801 number of votes.

	- To calculate the data by county, a list[] and a dictionary{} were created. 
		```
		# 1: Create a county list and county votes dictionary.
		county_options = []
		county_votes = {}
		```
	- Inside the for loop that was reading through all the rows, county names were extracted from the second column:
		 	```
			# 3: Extract the county name from each row.
        		county_name = row[1]
			```
	- If county name was not already on the list, it was added to the list of counties using if statement and then append. 
			```
			# 4a: Write an if statement that checks that the
        		# county does not match any existing county in the county list.
        		if county_name not in county_options:

            			# 4b: Add the existing county to the list of counties.
            			county_options.append(county_name)
			```
	- Number of votes per county is set to zero so that counting of votes per county can begin. This information was taken from the dictionary county_votes, therefore the format is as below to extract the value which is the number of votes from the key which is the name of the county:
				```
            			# 4c: Begin tracking the county's vote count.
            			county_votes[county_name] = 0
				```
	- Votes counted per county:
			```
        		# 5: Add a vote to that county's vote count.
        		county_votes[county_name] += 1
			```
	- To calculate the county vote percentage a for loop was created to get the county names, and the county vote count (cvotes) from the county dictionary:
			```
			# 6a: Write a for loop to get the county from the county dictionary.
    			for county_name in county_votes:
        			# 6b: Retrieve the county vote count.
        			cvotes = county_votes[county_name]
			```
	- A formula for calculating the percentage was created, the cvotes and total_votes was changed from integers to decimal point numbers using "float":
				```
        			# 6c: Calculate the percentage of votes for the county.
        			county_vote_percentage = float(cvotes) / float(total_votes) * 100
				```

	- When the numbers were printed out, an f-string was used and the number of digits after the decimal point was limited using :.1f
				```
				# 6d: Print the county results to the terminal.
        			county_results = (f"{county_name}: {county_vote_percentage:.1f}% ({cvotes:,})\n")
        			print(county_results)
				```

- Denver was the county with the largest number of votes

	- To determine which county had the largest number of votes, new variables were initialized and started at zero:
		```
		# 2: Track the largest county and county voter turnout.
		largest_turnout_county = ""
		largest_turnout_count = 0
		largest_turnout_count_percentage = 0
		```
 				
	- Then an if statement was created to compare vote counts and also to compare vote percentages. The county with the largest number of votes and highest percentage of votes was determined and named. 
				```
				# 6f: Write an if statement to determine the winning county and get its vote count.
        			if (cvotes > largest_turnout_count) and (county_vote_percentage > largest_turnout_count_percentage ):
            				largest_turnout_count = cvotes
            				largest_turnout_count_percentage = county_vote_percentage
            				largest_turnout_county = county_name
				```
- The candidates were: 
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doanevote

- The candidate results were:
  - Charles Casper Stockham received 23.0% of the votes and 85,213 number of votes. 
  - Diana DeGette received 73.8% of the votes and 272,892 number of votes. 
  - Raymon Anthony Doane received 3.1% of the votes and 11,606 number of votes. 


	- To determine the names of the candidates, the number of votes each candidate received and the percentage of votes each candidate received, a similar code was used to the one described above for the county names, number of votes and percentages. 
  


- The winner of the election was:
  - Diana DeGette who received 73.8% of the vote and 272,892 number of votes. 
  
	- To determine the winner of the election: name, number of votes and percentage of votes, a similar code was used to the code that was used for finding the largest turnout county's name, number of votes and percentage of votes. 


---

## Election-Audit Summary: 
A business proposal to the election commission:
This code proved to be very useful for determining the results of this specific congressional election in Colorado. The data was quickly analyzed and the output was clearly presented in a separate document. However, this code has a general format and should not be limited for one time use only. 
This code is uniquely qualified to provide election data from any election with some simple modifications. With a small investment of time and effort, the return can be very significant if this code is used multiple times. 
A couple of items that can easily be changed to analyze results of another election:
- The path to the files:
  - Since the code is giving instructions to open the election results file, it could theoretically open any file. It may be necessary to change the path instructions to make sure the correct file is accessed. 
  	```
	# Add a variable to load a file from a path.
	file_to_load = os.path.join("Resources", "election_results.csv")
	```
  - The path to the text file where the results of the analysis will be writen may also need to change. 
	```
	# Add a variable to save the file to a path.
	file_to_save = os.path.join("analysis", "election_analysis.txt")
	```
- Inside the election results file, the location of the information may be different. For example, in this analysis the location of candidate name was [2] and county was [1] but in another election, the columns may be filled differently. 
	```
	# Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
	```

- In this analysis the focus was on analyzing the data by candidate and by county. Depending on the information provided in other elections, these names could easily be replaced in the code to analyze for example by age, by zip code or any other category of interest. 
	This change would require a more significant change to the code since larger parts of it have the variables names that would need to change but still this would be an easy change compared to having to go through all the data manually. Also, the names of the variables would change but the code itself would stay the same so the changes would still be simple. 


In summary, this code provides a useful template for analysis of any election results and in order to make the most of it, it should be utilized multiple times. 



