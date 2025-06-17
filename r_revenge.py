import praw
import time
import textwrap

# replace with your own API credentials
reddit = praw.Reddit(client_id = "xxxxxxxxxxxxxxxxxx", client_secret = "xxxxxxxxxxxxxxxxx", user_agent = "xxxxxxxxxxxxx")

# Choose a subreddit
choose_subreddit = str(input("Enter the exact name of the subreddit: r/"))
keyword = str(input("Enter the keyword for search: "))

subreddit = reddit.subreddit(choose_subreddit)    # input the exact subreddit name to retrieve posts from

# Search for posts with a keyword
for post in subreddit.search(keyword, limit = 2):    # limit = the num of posts retrieved
    print("---" * 40)
    print(f"Title: {post.title}")

    # print modified content
    wrapped_text = textwrap.fill(post.selftext, width=100)    # (the target text, width = number of characters pe line)
    print(f"Content: \n{wrapped_text}\n")

    # print comments
    post.comments.replace_more(limit=0)   # limit=5 leaving some collapsed, limit = None expand all (slow)
    for comment in post.comments[:5]:
        print(f"Comments: {comment.body}")
        for reply in comment.replies:
            print(f"    Replies to the comment: {reply.body}")

    print(f"\nURL: {post.url}")
    print(reddit.auth.limits)

    time.sleep(3)   # 3 seconds delay between requests to prevent blockage

