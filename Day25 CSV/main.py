# with open(".\\Day25 CSV\\weather_data.csv","r") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv

# with open(".\\Day25 CSV\\weather_data.csv","r") as weather_data:
#     data = csv.reader(weather_data)
#     # print(data)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

#     print(temperatures)

import pandas 

# data = pandas.read_csv(".\\Day25 CSV\\weather_data.csv")
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# avg = sum(temp_list) / len(temp_list)
# print(avg)

# print(data["temp"].mean())
# print(data["temp"].max())

# print(data["condition"])
# print(data.condition)

# print(data[data["day"] == "Monday"])
# print(data[data.day == "Monday"])

# max = data.temp.max()
# day_max = data[data.temp == max]
# print(day_max)

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = monday.temp[0]
# monday_temp = monday_temp * (9/5) + 32
# print(f"{monday_temp:.2f}")

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv(".\\Day25 CSV\\new_data.csv")

# data = pandas.read_csv("Day25 CSV\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241023.csv")
# fur_color = data["Primary Fur Color"]
# color_dict = {
#     "Fur Color" : {

#     },
#     "Count": {

#     }
# }
# for row in fur_color:
#     # print(type(row))
#     if isinstance(row,str):
#         color_dict["Fur Color"][row] = color_dict["Fur Color"].get(row, 0) +1

# print(color_dict)
# data = pandas.DataFrame(color_dict,)
# data.to_csv(".\\Day25 CSV\\squirrel_count.csv")

data = pandas.read_csv("Day25 CSV\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241023.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv(".\\Day25 CSV\\squirrel_count.csv")