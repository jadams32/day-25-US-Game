import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = 0
black = 0
cinnamon = 0
for item in data["Primary Fur Color"]:
    if item == "Gray":
        gray += 1
    if item == "Black":
        black += 1
    if item == "Cinnamon":
        cinnamon += 1

dict = {"Fur Color": ["Gray", "Red", "Black"], "Count": [gray, cinnamon, black]}

colors = pandas.DataFrame(data=dict)
print(colors)
