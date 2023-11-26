import webbrowser
import praw 
import json
import time 

CLIENT_ID = #
CLIENT_SECRET = #
USER_AGENT = #
USERNAME = #
PASSWORD = #

reddit = praw.Reddit(client_id = CLIENT_ID, client_secret = CLIENT_SECRET, user_agent = USER_AGENT, username = USERNAME, password = PASSWORD)

f = open('./names.txt', 'w')
s = set()
n = 2000
subreddit_name = #

sub = reddit.subreddit(subreddit_name)

newsub = sub.new(limit=n)
for i in newsub:  
    for comment in i.comments:
        if hasattr(comment,"body") and comment.author!="AutoModerator":
            if i.author not in s:
                s.add(i.author)
                f.write(f'u/{i.author}\n')
