# numbers = [1,2,3]
# new_list = [item*2 for item in numbers]
# print(new_list)

# name = "Marc"
# new_list = [letter for letter in name]

# new_list = [n*2 for n in range(1,5) if n%2 == 0]

# names  = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# new_list = [name.upper() for name in names if len(name) > 5]

# print(new_list)

# dict comprehension
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

# import random
# names  = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = {name:random.randint(0,100) for name in names}
# print(students_scores)

# passed_students = {name:score for (name,score) in students_scores.items() if score > 60}
# print(passed_students)

import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56,76,98]
}
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
print("-------------------")

# Loop through a data frame

# for (key,value) in student_data_frame.items():
#     print(value)

#Loop through rows of a data frame
for(index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.student)