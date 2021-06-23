import os
import csv

total_votes = 0
candidate_list = []
candidate_votes = {}
winning_count = 0
winning_candidate = ""


#Defie the input/output path
Input_File = os.path.join("Resources", "election_data.csv")
Output_File = os.path.join("Analysis", "election_analysis.txt")


with open(Input_File) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    #Read & Print Header Row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    for row in csvreader:

     # Count total votes
        total_votes = total_votes + 1


        candidate_name = row[2]
        #If the candidate name is not in list thenn append the name
        if candidate_name not in candidate_list:
             candidate_list.append(candidate_name)
             #If the name is new vote cout has not started yet
             candidate_votes[candidate_name] = 0

        #Count the vote for every canndidate
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
      
    

with open(Output_File, "w") as txt_file:

    # Print the output to terminal
    election_results = (
    f"\n\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)


    for candidate in candidate_votes:

        votes = candidate_votes.get(candidate)
        vote_percentage = (votes) / (total_votes) * 100

        #Condition for Winninng
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(output, end="")
        txt_file.write(output)


    # Print the winning candidate
    winning_candidate_output = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_output)    
    txt_file.write(winning_candidate_output)


   
