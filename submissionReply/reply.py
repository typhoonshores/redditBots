#praw is required to connect with reddit API
import praw
import config

def login():
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "HQ: Silverfin113")
    return r

def botCore(r):
    for submission in r.subreddit('testingground4bots').hot(limit=25):
        if "meow" in submission.title:
            print("submission found")
            submission.reply("wow what a cat")

r = login()
botCore(r)