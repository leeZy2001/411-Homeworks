from itertools import combinations
import pandas as pd
import csv

def algo1(dataframe, p, r):
    dataframe = pd.read_csv(dataframe)

    #list of all quizzes
    quiz_list = dataframe.keys().tolist()

    #list of all possible combinations
    combinations_list = list(combinations(quiz_list, 4))

    #list of possible 4 quiz combos which meet the conditions
    output_list = []

    #to count the running time
    time_complexity = 0

    for each_combo in combinations_list:
        time_complexity += 1
        valid_quiz = 0
        for each_quiz in each_combo:
            time_complexity += 1
            valid_students= 0
            for student_score in dataframe[each_quiz]:
                time_complexity += 1
                if (student_score >= r):
                    valid_students += 1
            if (valid_students >= p):
                valid_quiz += 1
        if (valid_quiz == 4):
            output_list.append(each_combo)

    # Write Out the CSV File
    filename = "algo1_output.csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)

        csvwriter.writerows(output_list)

    print("CSV file 'algo1_output.csv' has been generated.")

    #count for total possible 4 quiz combos
    count_output = len(output_list)
    print("There are a total of ", count_output, "possible outputs.")
    
    print("The running time: ", time_complexity)




p = int(input("What is the minimum amount of students you want to obtain for score r? "))
r = int(input("What is the minimum score desired? "))

algo1('raw_score_dataframe.csv', p, r)