# Python Challenge

## Third Data Analytics and Visualization boot camp homework

It consist of two mandatory projects and two extra projects. The first mandatory project is about creating a Python script that analyses the financial records of a financial institution and generates an analysis report of the findings. The second mandatory project is about creating a script that counts votes and creates a summary of the results of an election.

The first extra project needs a script that reads from a file, changes the data format, and creates a new file with the new format data. The second extra project asks for a script that can read a text file and analyse it, finding the number of words, the number of sentences, the average letters per word, the average words per sentence, and print all this information to the console.

### PyBank

This script reads through a csv file *budget_data.csv* and calculates the total number of months in the data sample, the net amount of profit and losses, the month with the greatest profits and the month with the greatest losses. Then it creates a textfile *Financial_Analysis.txt* where it summarizes all the calculated information. It prints it on the console as well.

To run the script go to the folder PyBank and then enter:
```
python main.py
```

### PyPoll

This script reads a csv file *election_data.txt* and calculates the total number of votes, the votes each candidate received and the percent of votes, and the winner of the election based on the number of votes. Then it creates a file called *Election_Analysis.txt* where it adds all the information generated. It also prints the same information on the console.

To run the script go to the folder PyPoll and then enter:
```
python main.py
```

### PyBoss

This script reads from the employee_data.csv file and converts some of the files to a new format. The name is split in first and last name. The date of birth is also change from a YYYY-MM-DD format to MM/DD/YYYY format. The social security number is stores with only the last four digits visible like this \*\*\*-\*\*-9165. Finally, a new CSV file is created using the data in the new format.

To run the script go to the folder PyBoss and then enter:
```
python main.py
```

### PyParagraph

This script automates the analysis of a text file by calculating the following metrics:
- Approximate word count
- Approximate sentence count
- Approximate letter count (per word)
- Average sentence length (in words)

It finishes by printing in the console the results of the analys.

To run the script go to the folder PyParagraph and then enter:
```
python main.py
```
