## This python script reads data from a budget file and creates
## a financial analysis summary of this data and stores it in a text file

# Import libraries
import csv
import os

# Paths to financial analysis file and budget data csv file
financialAnalysisFilePath = os.path.join("analysis", "Financial_Analysis.txt")
budgetDataFilePath = os.path.join("Resources", "budget_data.csv")

# Initialize variables
totalProfitLosses = 0
monthsCount = 0
greatestIncreaseInProfits = 0
greatestDecreaseInLosses = 0
greatestIncreaseInProfitMonth = ""
greatestDecreaseInLossesMonth = ""

# Store the header row
readHeaderOnce = False
headerRow = None

# Read the budget file
with open(budgetDataFilePath, 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	for row in csv_reader:

		# Header row
		if (not readHeaderOnce):
			headerRow = row
			readHeaderOnce = True
		
		currentMonth = row["Date"]
		currentProfitLoss = int(row["Profit/Losses"])
		
		monthsCount += 1 # count the months
		totalProfitLosses += currentProfitLoss # add all profit and losses
		
		# Keep track of the greatest increase in profit or decrease in losses 
		if (currentProfitLoss > 0 and currentProfitLoss > greatestIncreaseInProfits):
			greatestIncreaseInProfits = currentProfitLoss
			greatestIncreaseInProfitMonth = currentMonth
		elif (currentProfitLoss < 0 and currentProfitLoss < greatestDecreaseInLosses):
			greatestDecreaseInLosses = currentProfitLoss
			greatestDecreaseInLossesMonth = currentMonth

# Print header values
print(f'\nThe headers are: {", ".join(headerRow)}\n')

# Calculate average change
averageChange = totalProfitLosses/monthsCount

# Write analysis information summary
## Open the file using "write" mode. Specify the variable to hold the contents
with open(financialAnalysisFilePath, 'w') as fileWriter:
	fileWriter.write('-------------------------------\n')
	fileWriter.write('Financial Analysis\n')
	fileWriter.write('-------------------------------\n')
	fileWriter.write(f'Total Months: {monthsCount}\n')
	fileWriter.write(f'Average  Change: ${averageChange:.2f}\n')
	fileWriter.write(f'Greatest Increase in Profits: {greatestIncreaseInProfitMonth} (${greatestIncreaseInProfits:.2f})\n')
	fileWriter.write(f'Greatest Decrease in Profits: {greatestDecreaseInLossesMonth} (${greatestDecreaseInLosses:.2f})\n')

print(f'Financial Analysis file has been created:\n {financialAnalysisFilePath}\n')

# Read and print to the console the results of the financial analysis file
with open(financialAnalysisFilePath, 'r') as fileReader:
	print(fileReader.read())