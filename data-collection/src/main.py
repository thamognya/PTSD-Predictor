from write import *

csv_location = "../../data.csv"

def getData(num, sticky, csv_location):
    header(csv_location)
    redditToCsv(num, sticky, csv_location)

getData(1000, 2, "../../data.csv")

"""
getData(5, 2, "../.././machine-learning/src/training.csv")
"""

