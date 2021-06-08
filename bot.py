#!/bin/python3
import praw
from random import choice
from datetime import datetime, timedelta
from glob import glob

def init_bot(auth_file: str) -> praw.Reddit:
    with open(auth_file, 'r') as f:
        auth_info = f.read().split('\n')
        return praw.Reddit(
            client_id     = auth_info[0],
            client_secret = auth_info[1],
            user_agent    = auth_info[2],
            username      = auth_info[3],
            password      = auth_info[4],
        )

def get_replies(path: str) -> list:
    replies = []
    files = glob(path)
    for file in files:
        with open(file, 'r') as f:
            replies.append(f.read())
    return replies

def main():
    f = open('replied', 'r+')
    replied = f.read().split('\n')
    replies = get_replies('./replies/*')
    reddit = init_bot('../yay_bot_auth')
    subreddit = reddit.subreddit('surferluls_tests')
    for comment in subreddit.stream.comments():
        if 'yay' == comment.body.lower() and comment.permalink not in replied:
            replied.append(comment.permalink)
            f.write('\n' + comment.permalink)
            comment.reply(choice(replies))
            print(f'replied to {comment.permalink}')
    f.close()

if __name__ == "__main__":
    main()
