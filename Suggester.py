
import csv

def Suggesters(input):
 # Take user input
 user_input = input

 # Open the CSV file with proper encoding
 with open('Remedies.csv', 'r', encoding='utf-8', errors='ignore') as file:
    # Create a CSV reader
    reader = csv.reader(file)
    rows = list(reader)
    
    # Search for the input value and retrieve the corresponding output
    output_value = None
    for row in rows:
        if row[0] == user_input:
            # Each cell is separated by \n\n\n
            output_value = '\n\n\n'.join(row)
            break

    return output_value

