from itertools import combinations
import pandas as pd
import csv

def algo2(df, desired_score, min_students):
    df = pd.read_csv(df)

    #list of all quizzes
    quiz_list = df.keys().tolist()

    quiz_dict = {}

    valid_quizzes = []

    #to count the running time
    time_complexity = 0

    for each_quiz in quiz_list:
        time_complexity += 1
        valid_students = 0
        for student_score in df[each_quiz]:
            time_complexity += 1
            if student_score >= desired_score:
                valid_students += 1
        if valid_students >= min_students:
            valid_quizzes.append(each_quiz)
            quiz_dict[each_quiz] = valid_students

    possible_combos = list(combinations(valid_quizzes,4))
    possible_combos_csv = []

    for each_combo in possible_combos:
        time_complexity += 1
        each_combo = list(each_combo)
        cum_students = 0
        for each_quiz in each_combo:
            time_complexity += 1
            cum_students += int((quiz_dict[each_quiz]))
        each_combo.append(cum_students)
        possible_combos_csv.append(each_combo)

    # Write Out the CSV File
    filename = "algo2_output.csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)

        csvwriter.writerows(possible_combos_csv)

    print("CSV file 'algo2_output.csv' has been generated.")

    #count for total possible 4 quiz combos
    count_output = len(possible_combos_csv)
    print("There are a total of ", count_output, "possible outputs.")
    
    print("The running time: ", time_complexity)




R = int(input("What is the minimum score desired? "))
P = int(input("What's the minimum students you want to obtain that score? "))


algo2('raw_score_dataframe.csv', R, P)
