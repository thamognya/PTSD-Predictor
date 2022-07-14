from decouple import config
import sys
import os
import json
import praw
import random
# file imports
from sanitize import *

# https://www.reddit.com/r/ptsd/

# https://praw.readthedocs.io/

# variables for reddit api
USERNAME = config('REDDIT_USERNAME')
PASSWORD = config('REDDIT_PASSWD')
CLIENT_ID = config('REDDIT_API_ID')
CLIENT_SECRET = config('REDDIT_API_SECRET')
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"

# config section for reddit api to work
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    password=PASSWORD,
    user_agent=user_agent,
    username=USERNAME,
)

# https://www.honchosearch.com/blog/seo/how-to-use-praw-and-crawl-reddit-for-subreddit-post-data/
# https://praw.readthedocs.io/en/latest/code_overview/models/submission.html
# crawl r/ptsd

# https://praw.readthedocs.io/en/latest/code_overview/models/submission.html?highlight=is_self#praw.models.Submission

# chooses the hotest ptsd subreddit posts -> becuase they are verified
def pushSubredditInfoToList(title_list, content_list, url_list, location_list, ptsd_list, ptsd, subreddit, limit_num, sticky):
    limit_num = (limit_num + sticky)
    for submission in reddit.subreddit(subreddit).hot(limit=limit_num):
        if submission.is_self == True:
            if submission.stickied:
                limit_num = limit_num + 1
                continue
            else:
                # add quotation marks here
                # sanitize = remove iconsitencies with text liek punctuation and big samll letter adn etc,
                tmp = '"{}"'.format(sanitizeText(submission.title))
                title_list.append(tmp)
                # add quotation marks here
                tmp = '"{}"'.format(sanitizeText(submission.selftext))
                content_list.append(tmp)
                # add quotation marks here
                tmp = '"{}"'.format(submission.url)
                url_list.append(tmp)
                tmp = '"{}{}"'.format("r/", subreddit)
                location_list.append(tmp)
                tmp = '"{}"'.format(ptsd)
                ptsd_list.append(tmp)
        else:
            limit_num = limit_num + 1
            continue

def pushSubredditInfoToListTrain(title_list, content_list, ptsd_list, ptsd, subreddit, limit_num, sticky):
    limit_num = (limit_num + sticky)
    for submission in reddit.subreddit(subreddit).hot(limit=limit_num):
        if submission.is_self == True:
            if submission.stickied:
                limit_num = limit_num + 1
                continue
            else:
                # add quotation marks here
                # sanitize = remove iconsitencies with text liek punctuation and big samll letter adn etc,
                tmp = '{}'.format(sanitizeText(submission.title))
                title_list.append(tmp)
                # add quotation marks here
                tmp = '{}'.format(sanitizeText(submission.selftext))
                content_list.append(tmp)
                # add quotation marks here
                tmp = '{}'.format(ptsd)
                ptsd_list.append(tmp)
        else:
            limit_num = limit_num + 1
            continue