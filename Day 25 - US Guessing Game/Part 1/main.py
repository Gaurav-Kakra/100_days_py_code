##Reading the data
# with open("C:/Users/gk38371/Desktop/All Notes GK/Udemy Python/Day 25/weather_data.csv") as file:
#     lines = file.readlines()
#     print(lines)

# import csv

# with open("C:/Users/gk38371/Desktop/All Notes GK/Udemy Python/Day 25/weather_data.csv") as file:
#     lines = csv.reader(file)
#     temperatures = []
#     for row in lines:
#         if row[1] != "temp":
#             temp = int(row[1])
#             temperatures.append(temp)
#     print(temperatures)

import pandas

# data = pandas.read_csv("C:/Users/gk38371/Desktop/All Notes GK/Udemy Python/Day 25/weather_data.csv")
#print(data['temp'])

## Getting the data series and finding the mean
# temp_list = data['temp'].to_list()
# print(sum(temp_list)/len(temp_list))

##Finding the max of some column
# print(data['temp'].max())

## Get data from conditions
#print(data[data['temp'] == data['temp'].max()])

##Get data in row
# monday = data[data.day == 'Monday']
# print(monday.temp[0]*9/5+32)

##  Create a dataframe from scratch
# data_dict = {
#     "students": ["GK","MK","DK"],
#     "scores": [98,76,87]
# }

# data = pandas.DataFrame(data_dict)
# print(data)
#data.to_csv("C:/Users/gk38371/Desktop/All Notes GK/Udemy Python/Day 25/new_data.csv")

data = pandas.read_csv("squirrel_data.csv")

gray_count = len(data[data['Primary Fur Color']=='Gray'])
red_count = len(data[data['Primary Fur Color']=='Cinnamon'])
black_count = len(data[data['Primary Fur Color']=='Black'])

data_dict = {
    "Fur Color": ["Gray","Red","Black"],
    "Count": [gray_count, red_count, black_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
