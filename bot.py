#!/bin/python3
import praw
from random import choice

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

def main():
    reddit = init_bot('../yay_bot_auth')
    subreddit = reddit.subreddit('surferluls_tests')
    for comment in subreddit.stream.comments():
        if 'yay' == comment.body.lower():
            comment.reply(choice([
                """there is nothing to do""",
                """:: Synchronizing package databases...
 core is up to date
 extra is up to date
 community is up to date
 multilib is up to date
:: Starting full system upgrade...
resolving dependencies...
looking for conflicting packages...

Packages (1) supertuxkart-1.2-1""",
                """: Starting full system upgrade...
resolving dependencies...
looking for conflicting packages...
warning: removing 'your-dad' from target list because it conflicts with 'your-mom'
error: failed to prepare transaction (could not satisfy dependencies)""",
                ]))
        print(comment.__dict__)

if __name__ == "__main__":
    main()
