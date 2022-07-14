from write import *

csv_location = "../../data.csv"

def getData(num, sticky, csv_location):
    header(csv_location)
    redditToCsv(num, sticky, csv_location)

print("Starting Data collection")
getData(2000, 2, "../../data/data.csv")
print("Starting Training collection")
getData(2000, 2, "../../data/training.csv")

