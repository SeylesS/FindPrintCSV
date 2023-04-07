import os
import csv

# Get a list of all CSV files in the current directory
csv_files = [filename for filename in os.listdir() if filename.endswith('.csv')]
# Create a selection menu for the CSV files
print('Select a CSV file to run:')
for i, filename in enumerate(csv_files):
    print(f'{i+1}: {filename}')

# Get user input for the selected file
selection = input('Enter the number of the file to run: ')

# Load and process the selected CSV file and print it out
if selection.isdigit() and int(selection) in range(1, len(csv_files)+1):
    filename = csv_files[int(selection)-1]
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            # Print each row of the CSV file
            print(row)
else:
    print('Invalid selection.')
