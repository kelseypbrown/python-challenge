import os

import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next (csvreader)
    
    #Set Variables:
    total_profit_losses = 0

    total_months = 0

    sum_profit_losses = 0

    greatest_increase = 0
    greatest_increase_month = ""

    greatest_decrease = 999999999
    greatest_decrease_month= ""

    #Create Loop through rows:
    for row in csvreader:
       
       profit_losses = row[1]

        #Calculate total profit losses:
       total_profit_losses = total_profit_losses + int(profit_losses)
        
        #Calculate total months (the number of rows):
       total_months = total_months + 1
       
       #Calculate sum profit losses for average change:
       if total_months > 1:
           change = int(profit_losses) - int(last_profit_losses)

           sum_profit_losses = sum_profit_losses + change

           #Calculate greatest increase:
           if change > greatest_increase:
               greatest_increase = change
               greatest_increase_month = row[0]

            #Calculate greatest decrease:
           if change < greatest_decrease:
               greatest_decrease = change
               greatest_decrease_month = row[0]

        #Reset last profit loss each loop for accurate calculation of change
       last_profit_losses = row[1]

    #Print Summary Analysis:
    print("Financial Analysis")
    print("-------------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_profit_losses}')
    average_change = round((sum_profit_losses / (total_months -1)),2)
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')

    #Output to text file:
    output_path = os.path.join("Analysis", "results.txt")

    lines = [f'Total Months: {total_months}', 
         f'Total: ${total_profit_losses}', 
         f'Average Change: ${average_change}', 
         f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})', 
         f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})']

    with open(output_path, 'w') as f:
        f.write("Financial Analysis\n")
        f.write("-------------------------------------\n")
            
        for line in lines:
            f.write(line)
            f.write('\n')