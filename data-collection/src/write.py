import pandas as pd
import sys
import os
# file imports
from redditScraper import *


def header(csv_location):
    data = {
        'Location': [],
        'PTSD': [],
        'Title': [],
        'Content': [],
        'Url': [],
    }
    df = pd.DataFrame(data)
    df.to_csv(csv_location, mode='a', index=False, header=True)

# REDDIT TO CSV - START ###


def redditToCsv(num, sticky, csv_location):
    # lists for title, content and url
    title = []
    content = []
    url = []
    location = []
    ptsd_list = []
    # this fills the title, content and url lists
    # uses func in scraper.py to to get sub reddit info
    pushSubredditInfoToList(title, content, url, location, ptsd_list, "YES", "ptsd", num, sticky)
    pushSubredditInfoToList(title, content, url, location, ptsd_list, "YES", "CPTSD", num, sticky)
    # tmp random reddits => https://www.generatormix.com/random-subreddits
    pushSubredditInfoToList(title, content, url, location, ptsd_list, "NO", "AskReddit", (num * 2) / 16, sticky)
    pushSubredditInfoToList(title, content, url, location, ptsd_list, "NO", "bicycling", (num * 2) / 16, sticky)
    pushSubredditInfoToList(title, content, url, location, ptsd_list, "NO", "funny", (num * 2) / 16, sticky)
    pushSubredditInfoToList(title, content, url, location, ptsd_list, "NO", "catpictures", (num * 2) / 16, sticky)
    pushSubredditInfoToList(title, content, url, location, ptsd_list, "NO", "gay", (num * 2) / 16, sticky)
    pushSubredditInfoToList(title, content, url, location, ptsd_list, "NO", "horror", (num * 2) / 16, sticky)
    pushSubredditInfoToList(title, content, url, location, ptsd_list, "NO", "RelayForReddit", (num * 2) / 16, sticky)
    pushSubredditInfoToList(title, content, url, location, ptsd_list, "NO", "tennis", (num * 2) / 16, sticky)
    pushSubredditInfoToList(title, content, url, location, ptsd_list, "NO", "RedditLaqueristas", (num * 2) / 16, sticky)
    pushSubredditInfoToList(title, content, url, location, ptsd_list, "NO", "ImaginaryMindscapes", (num * 2) / 16, sticky)
    pushSubredditInfoToList(title, content, url, location, ptsd_list, "NO", "flying", (num * 2) / 16, sticky)
    pushSubredditInfoToList(title, content, url, location, ptsd_list, "NO", "bois", (num * 2) / 16, sticky)
    pushSubredditInfoToList(title, content, url, location, ptsd_list, "NO", "likeus", (num * 2) / 16, sticky)
    pushSubredditInfoToList(title, content, url, location, ptsd_list, "NO", "Entrepeneur", (num * 2) / 16, sticky)
    pushSubredditInfoToList(title, content, url, location, ptsd_list, "NO", "CasualConversation", (num * 2) / 16, sticky)
    pushSubredditInfoToList(title, content, url, location, ptsd_list, "NO", "writing", (num * 2) / 16, sticky)
    pushSubredditInfoToList(title, content, url, location, ptsd_list, "NO", "howyoudoin", (num * 2) / 16, sticky)
    #pushSubredditInfoToList(title, content, url, location, "CPTSD", num, sticky)
    # def pushSubredditInfoToList(title_list, content_list, url_list, location_list, ptsd_list, ptsd, subreddit, limit_num, sticky):
    # pushSubredditInfoToListNoSanitize(title, content, url, "ptsd", num, sticky)
    # data for pandas
    data = {
        'Location': location,
        'PTSD': ptsd_list,
        'Title': title,
        'Content': content,
        'Url': url,
    }
    # pushes it into ../data.csv
    df = pd.DataFrame(data)
    df.to_csv(csv_location, mode='a', index=False, header=False)
    #print("Data appended successfully.")

### REDDIT TO CSV - END ###

### TWITTER TO CSV - START ###
### TWITTER TO CSV - END ###

### INSTA TO CSV - START ###
### INSTA TO CSV - END ###