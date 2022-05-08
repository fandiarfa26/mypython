import random
import pandas as pd

count_questions = 20
count_users = 20
r_table = 0.444
min_valid = 12

count_try = 1
highest_valid = 0
while True:
    matrix = []
    for i in range(count_users):
        row = []
        for j in range(count_questions):
            v = random.randint(0,4)
            row.append(5 if v > 0 else 0)
        matrix.append(row)

    df = pd.DataFrame(matrix)
    sum_df = df.sum(axis='columns')

    corr_arr = []
    count_valid = 0

    for k in range(count_questions):
        c = df[k].corr(sum_df)
        if c > r_table:
            count_valid += 1
        corr_arr.append(c)

    if count_valid > highest_valid:
        highest_valid = count_valid
    
    print('Try #',count_try,'; Count Valid =',count_valid,'; Highest Valid =',highest_valid)
    count_try += 1

    if count_valid >= min_valid:
        print(df)
        print(sum_df)
        break