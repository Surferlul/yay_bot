#!/bin/python3
import praw
from random import choice
from datetime import datetime, timedelta

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
    f = open('replies', 'r+')
    replies = f.read().split('\n')
    reddit = init_bot('../yay_bot_auth')
    subreddit = reddit.subreddit('surferluls_tests')
    for comment in subreddit.stream.comments():
        if 'yay' == comment.body.lower() and comment.permalink not in replies:
            replies.append(comment.permalink)
            f.write('\n' + comment.permalink)
            comment.reply(choice([
                """there is nothing to do""",
                """:: Synchronizing package databases...\n
 core is up to date\n
 extra is up to date\n
 community is up to date\n
 multilib is up to date\n
:: Starting full system upgrade...\n
resolving dependencies...\n
looking for conflicting packages...\n
\n
Packages (1) supertuxkart-1.2-1""",
                """: Starting full system upgrade...\n
resolving dependencies...\n
looking for conflicting packages...\n
warning: removing 'your-dad' from target list because it conflicts with 'your-mom'\n
error: failed to prepare transaction (could not satisfy dependencies)\n""",
                ]))
    f.close()

if __name__ == "__main__":
    main()
