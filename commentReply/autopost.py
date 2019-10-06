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
    for comment in r.subreddit('testingground4bots').comments(limit=25):
        if "cat" in comment.body:
            print("comment found")
            comment.reply("thats a cat alright")
            
        if "dog" in comment.body:
            print("comment found")
            comment.reply("woof, doggo alert")

r = login()
botCore(r)
