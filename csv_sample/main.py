# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperature = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperature.append(int(row[1]))
# #     print(temperature)
#
import pandas as pd
#
# data = pd.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
#
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data[data.temp == data["temp"].max()])

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data1 = data.groupby(data['Primary Fur Color'])
print(data1)