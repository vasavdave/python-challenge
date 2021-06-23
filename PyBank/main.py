import os
import csv

Total_Months = 0 
Net_Total = 0
Monthly_Change_List = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

#Defie the input/output path
Input_File = os.path.join("Resources", "budget_data.csv")
Output_File = os.path.join("Analysis", "data_analysis.txt")

with open(Input_File) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    #Read & PrintHeader Row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    first_row = next(csvreader)
    Previous_Net = int(first_row[1])
    Total_Months += 1
    Net_Total += int(first_row[1])


    for row in csvreader:
       #Calculate Total Months and Nnet Total
        Total_Months += 1
        Net_Total += int(row[1])

        #Calculate Monthly changes and put them in a list
        Monthly_Change = int(row[1]) - Previous_Net
        Previous_Net = int(row[1])
        Monthly_Change_List += [Monthly_Change]
      

        # Calculate the greatest increase
        if Monthly_Change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = Monthly_Change

        # Calculate the greatest decrease
        if Monthly_Change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = Monthly_Change



#Calculate Average Monthly Changes
Average_Changes = sum(Monthly_Change_List)/len(Monthly_Change_List)

output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {Total_Months}\n"
    f"Total: ${Net_Total}\n"
    f"Average  Change: ${Average_Changes:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )
    
# Print the output to terminal
print(output)

# Export the results to text file
with open(Output_File, "w") as txt_file:
    txt_file.write(output)
