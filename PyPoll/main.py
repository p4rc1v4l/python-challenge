## This python script reads data of an election results file and creates
## a summary of the candidates and their votes

# Libraries imports
import csv
import os

# Data file
electionDataFilePath = os.path.join("Resources", "election_data.txt")
# Summary file
electionAnalysisFilePath = os.path.join("analysis", "Election_Analysis.txt")

# Variables initialization
totalNumberOfVotes = 0
listOfCandidates = []
votesPerCandidate = []
winner = ""
mostVotesCandidate = -1
mostVotesNumber = 0

#  Open CVS file and read data about election
with open(electionDataFilePath, 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	
	for row in csv_reader:
		totalNumberOfVotes = totalNumberOfVotes + 1
		candidateName = row["Candidate"]
		
		# Keep track of each candidate that exist and count the votes for each candiate
		if candidateName in listOfCandidates:
			candidateIndex = listOfCandidates.index(candidateName)
			votesPerCandidate[candidateIndex] += 1
		else: # Add the candidate to the list of candidate for the first time
			listOfCandidates.append(candidateName)
			votesPerCandidate.append(1)

# Prepare summary information to write to file
with open(electionAnalysisFilePath, 'w') as fileWriter:
	fileWriter.write('\nElection Results\n')
	fileWriter.write('-------------------------------\n')
	fileWriter.write(f'Total Votes: {totalNumberOfVotes}\n')
	fileWriter.write('-------------------------------\n')

	# calculate percentages and look up the election winner
	for candidateIndex, candidateName in enumerate(listOfCandidates):
		totalCandidateVotes = votesPerCandidate[candidateIndex]
		votesPerentage = (totalCandidateVotes / totalNumberOfVotes) * 100

		fileWriter.write(f'{candidateName} : {votesPerentage:.3f}% ({totalCandidateVotes})\n')

		if totalCandidateVotes > mostVotesNumber:
			mostVotesNumber = totalCandidateVotes
			mostVotesCandidate = candidateIndex

	fileWriter.write('-------------------------------\n')
	fileWriter.write(f'Winner : {listOfCandidates[mostVotesCandidate]}\n')
	fileWriter.write('-------------------------------\n')	

# Read created file and print text into the console
with open(electionAnalysisFilePath, 'r') as fileReader:
	print(fileReader.read())