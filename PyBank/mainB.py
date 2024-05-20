import os
import csv
#------------------------------------------------------------
#set up paths to retrieve the budget data and to export the data to a text file
#------------------------------------------------------------------------
#-------------------------------------------------------------------
pwd = os.getcwd()
cwd = os.path.abspath(__file__)
# current directory name
dir_name =os.path.dirname(cwd)
# path to Budget_data file
csvinputpath = os.path.join(dir_name,'Resources',"Budget_data.csv")
#  path to text  file with the financial analysis results
txtoutputpath = os.path.join(dir_name,'analysis',"Financial_Analysis.txt")
#--------------------------------------------------------------------
#                     INITIALIZE VARIABLES
#--------------------------------------------------------------
# initialise and define variable used to analyse PyBank 
# count_months:the total number of months included in the dataset : 
count_months = 0
# total_profit_loss: the net total amount of "Profit/Losses" over the entire period
total_profit_loss = 0

# total_interday_PL_change: the changes in "Profit/Losses" over the entire period
total_interday_PL_change = 0
interday_PL_change = 0
# prior_amount: used to check if there is a prior amount required to calculate the interday change
prior_amount = None
# max_PL:the greatest increase in profits (date and amount) 
# over the entire period
# initialise with negative infinity to find the max
# initialise the associated date for the maximum
max_PL = float('-inf')
date_max_Pl =None
# min_PL:the greatest decrease in profits 
#(date and amount) over the entire period
min_PL = 0
date_min_Pl =None
#-------------------------------------------------
#--------------------------------------------------------------
#                      FINANICAL ANALYSIS
#-------------------------------------------------------------------
#-----------------------------------------------------------------------
#Open the budget_data.csv file. 
with open(csvinputpath, encoding='UTF-8') as budget_file:
    csv_reader = csv.reader(budget_file)
    # iterate through each row in budget_data.csv file 
    # skip the title row
    next(csv_reader)
    for data_row in csv_reader:
        PL_date = data_row[0]
        #increment the counter(number_months)for each row 
        count_months += 1
           

        # obtain the profit/loss in the 2nd column 
        # convert profit/loss to a floating value
        profit_loss = float(data_row[1])
       # 
        # convert interday_PL to a floating value
        interday_PL = float(data_row[1])
        # add profit_loss to total_profit_loss
        total_profit_loss += profit_loss
        #print("total_profit_loss = "+str(total_profit_loss))

        # check if there is amount in the day before.  
        # the calculation needs the previous day amount to calculate 
        # the interday amount
        #
        if prior_amount is not None:
            # the interday profit loss change is the difference 
            # between the current value less the value of the day before
            #
            interday_PL_change = profit_loss - prior_amount
            # keep a total balance of each interday profit loss change
            total_interday_PL_change += interday_PL_change
            
        # the prior amount is the current profit_loss for the subsequent iteration

        prior_amount = profit_loss
    # obtain the date & Profit and Loss amount from the row
        PL_date = data_row[0]
#       check if the interday P&L is the max if it is --> record it as the max       
        if interday_PL_change > max_PL:
            max_PL = interday_PL_change
 #       check if the interday P&L is the min  if it is --> record it as the min               
            date_max_Pl = PL_date
        if interday_PL_change < min_PL:
            min_PL = interday_PL_change
            
            date_min_Pl = PL_date

#-------------------------------------------------
#--------------------------------------------------------------
#                     PRINT OUT TO TERMINAL AND TEXT FILE
#-------------------------------------------------------------------
#-----------------------------------------------------------------------



#  display the total number of months included in the dataset
print(f"")
print(f"----------------------------------------------------")
print(f"Financial Analysis")
print(f"----------------------------------------------------")
print(f"")
print(f"Total Months: {count_months} " )
#  display the net total amount of "Profit/Losses" over the entire period
print (f"Total: ${total_profit_loss:.2f}")
#  display the changes in "Profit/Losses" over the entire period
# the average of changes is the the total "profit/loss" 
# divided by the total count less 1 (for the first entry)
print(f"Average Change: ${total_interday_PL_change/(count_months-1):.2f}")
# display the maximum Profit/Loss and the associated date
print(f"Grestest Increase in Profits:{date_max_Pl}  {max_PL}") 
# display the minimum Profit/Loss and the associated datex
print(f"Grestest Decrease in Profits:{date_min_Pl}  {min_PL}")    

#  Specify the file to write to

print(f"----------------------------------------------------")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(txtoutputpath, 'w') as txtoutputfile:
    #print to the text file the financial analysis calculated above
    txtoutputfile.write(f"\n")
    txtoutputfile.write(f"----------------------------------------------------\n")
    txtoutputfile.write(f"Financial Analysis\n")
    txtoutputfile.write(f"----------------------------------------------------\n")
    txtoutputfile.write(f"\n")
    txtoutputfile.write(f"----------------------------------------------------\n")
    txtoutputfile.write(f"Total Months: {count_months} \n")
    txtoutputfile.write(f"Total: ${total_profit_loss:.2f} \n")
    txtoutputfile.write(f"Average Change: ${total_interday_PL_change/(count_months-1):.2f} \n")
    txtoutputfile.write(f"Grestest Increase in Profits:{date_max_Pl}  {max_PL} \n")
    txtoutputfile.write(f"Grestest Decrease in Profits:{date_min_Pl}  {min_PL} \n")
    txtoutputfile.write(f"----------------------------------------------------\n") 
    # remark that the results were printed and where they can be found
    print(f"Results have been written to {txtoutputpath}.")
print(f"----------------------------------------------------")
print(f"----------------------------------------------------")   