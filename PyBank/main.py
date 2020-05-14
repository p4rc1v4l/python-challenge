#Read from a budget file and create a summary of the information
import csv

# Initialize variables
totalProfitLosses = 0
monthsCount = 0
greatestIncreaseInProfits = 0
greatestDecreaseInLosses = 0
greatestIncreaseInProfitMonth = ""
greatestDecreaseInLossesMonth = ""

# Read the budget file
with open('Resources/budget_data.csv') as csv_file:

    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        #For testing - print(f'Date \t{row["Date"]} --- Amount {row["Profit/Losses"]}')
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

# Calculate average change
averageChange = totalProfitLosses/monthsCount

# Analysis information summary
txtTitle = 'Financial Analysis'
txtTitleBottomLine = '-------------------------------'
txtTotalMonths = f'Total Months: {monthsCount}'
txtAverageChange = f'Average  Change: ${averageChange:.2f}'
txtGreatesteIncreaseInProfit = f'Greatest Increase in Profits: {greatestIncreaseInProfitMonth} (${greatestIncreaseInProfits:.2f})'
txtGreatestDecreaseInLosses = f'Greatest Decrease in Profits: {greatestDecreaseInLossesMonth} (${greatestDecreaseInLosses:.2f})'
txtNewLine = '\n'

# Write analysis to a text file
analysisFile = open("analysis/Financial_Analysis.txt", "x")

analysisFile.write(txtTitle + txtNewLine)
analysisFile.write(txtTitleBottomLine + txtNewLine)
analysisFile.write(txtTotalMonths + txtNewLine)
analysisFile.write(txtAverageChange + txtNewLine)
analysisFile.write(txtGreatesteIncreaseInProfit + txtNewLine)
analysisFile.write(txtGreatestDecreaseInLosses)

analysisFile.close()

# Print analysis on console
print(txtTitle)
print(txtTitleBottomLine)
print(txtTotalMonths)
print(txtAverageChange)
print(txtGreatesteIncreaseInProfit)
print(txtGreatestDecreaseInLosses)