import csv
import os
import re
import datetime 

# Function that uses as input the full name of a state and returns its abbreviated name
def abbreviateStateName(statefFullme):
	us_state_abbrev = {
		'Alabama': 'AL',
		'Alaska': 'AK',
		'Arizona': 'AZ',
		'Arkansas': 'AR',
		'California': 'CA',
		'Colorado': 'CO',
		'Connecticut': 'CT',
		'Delaware': 'DE',
		'Florida': 'FL',
		'Georgia': 'GA',
		'Hawaii': 'HI',
		'Idaho': 'ID',
		'Illinois': 'IL',
		'Indiana': 'IN',
		'Iowa': 'IA',
		'Kansas': 'KS',
		'Kentucky': 'KY',
		'Louisiana': 'LA',
		'Maine': 'ME',
		'Maryland': 'MD',
		'Massachusetts': 'MA',
		'Michigan': 'MI',
		'Minnesota': 'MN',
		'Mississippi': 'MS',
		'Missouri': 'MO',
		'Montana': 'MT',
		'Nebraska': 'NE',
		'Nevada': 'NV',
		'New Hampshire': 'NH',
		'New Jersey': 'NJ',
		'New Mexico': 'NM',
		'New York': 'NY',
		'North Carolina': 'NC',
		'North Dakota': 'ND',
		'Ohio': 'OH',
		'Oklahoma': 'OK',
		'Oregon': 'OR',
		'Pennsylvania': 'PA',
		'Rhode Island': 'RI',
		'South Carolina': 'SC',
		'South Dakota': 'SD',
		'Tennessee': 'TN',
		'Texas': 'TX',
		'Utah': 'UT',
		'Vermont': 'VT',
		'Virginia': 'VA',
		'Washington': 'WA',
		'West Virginia': 'WV',
		'Wisconsin': 'WI',
		'Wyoming': 'WY',
    }

	return us_state_abbrev[statefFullme]

# Path to input file and output file.
employee_data_file_path = os.path.join('Resources','employee_data.csv')
new_employee_data_file_path = os.path.join('Output','employee_data_new_format.csv')

# Formats to be use to read the date from the input file and convert the date in the output file
input_date_format = '%Y-%m-%d'
output_date_format = '%m/%d/%Y'

# List to keep all the new converted data
new_format_employee_data_list = []

# Read the input file and convert the date to the requeste format
with open(employee_data_file_path) as csv_file:
	csv_reader = csv.DictReader(csv_file)

	for row in csv_reader:
		
		# Split name in first and last name
		full_name_as_list = row["Name"].split()
		first_name = full_name_as_list[0]
		last_name = full_name_as_list[1]
		
		# Read current date of birth date and convert it to the new format MM/DD/YYYY
		date_of_birth = row["DOB"]
		new_date_of_birth =datetime.datetime.strptime(date_of_birth,input_date_format).strftime(output_date_format)
		
		# Read SSN and hide the first 5 numbers
		ssn = row["SSN"]
		hidden_first_five_ssn = re.sub("[0-9]", "*", ssn, 5)
		
		# Get the abbreviation for the state name
		stateAbbreviation = abbreviateStateName(row["State"])
		
		new_employee_data = {
			"Emp ID" : row["Emp ID"],
			"First Name" : first_name,
			"Last Name" : last_name,
			"DOB" : new_date_of_birth,
			"SSN" : hidden_first_five_ssn,
			"State" : stateAbbreviation
		}
		
		new_format_employee_data_list.append(new_employee_data)

# Write new file with the data in the new appropriate format
with open(new_employee_data_file_path, mode='w') as csv_file:
    header_row = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]
    writer = csv.DictWriter(csv_file, fieldnames=header_row)
    
    writer.writeheader()
    for employee in new_format_employee_data_list:
    	writer.writerow(employee)