import pandas as pd
import sys
import os
# file imports
from redditScraper import *


def header(csv_location):
    data = {
        'PTSD': [],
        'Title': [],
        'Content': [],
    }
    df = pd.DataFrame(data)
    df.to_csv(csv_location, mode='a', index=False, header=True)

def redditToCsv(num, sticky, csv_location):
    # lists for title, content and url
    title = []
    content = []
    ptsd_list = []
    # this fills the title, content and url lists
    # uses func in scraper.py to to get sub reddit info
    pushSubredditInfoToListTrain(title, content, ptsd_list, "YES", "ptsd", num, sticky)
    pushSubredditInfoToListTrain(title, content, ptsd_list, "YES", "CPTSD", num, sticky)

    pushSubredditInfoToListTrain(title, content, ptsd_list, "NO", "AskReddit", (num * 2) / 16, sticky)
    pushSubredditInfoToListTrain(title, content, ptsd_list, "NO", "bicycling", (num * 2) / 16, sticky)
    pushSubredditInfoToListTrain(title, content, ptsd_list, "NO", "funny", (num * 2) / 16, sticky)
    pushSubredditInfoToListTrain(title, content, ptsd_list, "NO", "catpictures", (num * 2) / 16, sticky)
    pushSubredditInfoToListTrain(title, content, ptsd_list, "NO", "gay", (num * 2) / 16, sticky)
    pushSubredditInfoToListTrain(title, content, ptsd_list, "NO", "horror", (num * 2) / 16, sticky)
    pushSubredditInfoToListTrain(title, content, ptsd_list, "NO", "RelayForReddit", (num * 2) / 16, sticky)
    pushSubredditInfoToListTrain(title, content, ptsd_list, "NO", "tennis", (num * 2) / 16, sticky)
    pushSubredditInfoToListTrain(title, content, ptsd_list, "NO", "RedditLaqueristas", (num * 2) / 16, sticky)
    pushSubredditInfoToListTrain(title, content, ptsd_list, "NO", "ImaginaryMindscapes", (num * 2) / 16, sticky)
    pushSubredditInfoToListTrain(title, content, ptsd_list, "NO", "flying", (num * 2) / 16, sticky)
    pushSubredditInfoToListTrain(title, content, ptsd_list, "NO", "bois", (num * 2) / 16, sticky)
    pushSubredditInfoToListTrain(title, content, ptsd_list, "NO", "likeus", (num * 2) / 16, sticky)
    pushSubredditInfoToListTrain(title, content, ptsd_list, "NO", "Entrepeneur", (num * 2) / 16, sticky)
    pushSubredditInfoToListTrain(title, content, ptsd_list, "NO", "CasualConversation", (num * 2) / 16, sticky)
    pushSubredditInfoToListTrain(title, content, ptsd_list, "NO", "writing", (num * 2) / 16, sticky)
    pushSubredditInfoToListTrain(title, content, ptsd_list, "NO", "howyoudoin", (num * 2) / 16, sticky)
    data = {
        'PTSD': ptsd_list,
        'Title': title,
        'Content': content,
    }
    # pushes it into ../data.csv
    df = pd.DataFrame(data)
    df.to_csv(csv_location, mode='a', index=False, header=False)

### REDDIT TO CSV - END ###