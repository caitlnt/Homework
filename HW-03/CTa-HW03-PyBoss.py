
#python CTa-HW03-Pyboss.py

#C:\Users\CNT\Documents\My Docs\Data Analytics\Week 03\Homework 03

import os
import csv

#gets election data file
csvfile = os.path.join("Resources", "employee_data1.csv")

converted = {}

stateabbrv = {
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


with open(csvfile, "r") as employee_data:
	csvreader = csv.DictReader(employee_data)

	for row in csvreader:
		name = row['Name'].split()
		dob = row['DOB'].split('-')
		ssn = row['SSN'].split('-')
		state = row['State']
		
		converteddata = {'Emp ID': row['Emp ID'],
						 'First Name': name[0],
						 'Last Name': name[1],
						 'DOB': dob[1] + '/' + dob[2] + '/' + dob[0],
						 'SSN': '***-**-' + ssn[2],
						 'State': stateabbrv[state]
						 }

		coverted.append(converteddata)

print(converteddata)
