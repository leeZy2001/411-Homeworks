import csv
import random

def create_data(m, n):
    # Generate random data
    data = [['S' + str(i)] + [random.randint(0, 10) for _ in range(n)] for i in range(1, m + 1)]

    # Define the header
    header = ['Q' + str(i) for i in range(1, n + 1)]

    # Write data to a CSV file
    with open('raw_score_dataframe.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # Write the header
        csvwriter.writerow(header)
        
        # Write the data rows
        csvwriter.writerows(data)

    print("CSV file 'raw_score_dataframe.csv' has been generated.")

# Define the number of rows and columns
m = int(input("What is the row of students?"))
n = int(input("what is the column of quizzes?"))

create_data(m, n)