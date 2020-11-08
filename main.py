import time
import requests
from bs4 import BeautifulSoup


def scrape(tweeter):
    tweets_raw = requests.get("https://mobile.twitter.com/" + tweeter).text

    soup = BeautifulSoup(tweets_raw, features="html.parser")
    tweets = [tweet.text.strip().replace("\n", " ") for tweet in soup.find_all("div", {"class": "tweet-text"})]
    tweets_line_breaks = []
    for tweet in tweets:
        tmp = ""
        while tweet:
            tmp += tweet[:100] + "|\n"
            tweet = tweet[100:]
        tweets_line_breaks.append(tmp[:-2])  # exclude last pipe & newline

    return tweets_line_breaks


tweeter = input("Who's tweets do you want to retype? (ex: richardbranson, SnoopDogg)")
tweets = scrape(tweeter)
input("\nPress enter to start the clock\n--------------------------------\n")
start_time = time.time()

i = 0
total_tweets = len(tweets)
typed_tweets = []
if total_tweets:
    while time.time() - start_time < 10:
        typed_tweets.append(input(tweets[i] + "\n"))
        if i == total_tweets - 1:
            i = 0
        else:
            i += 1

score = []
for t, typed_line in enumerate(typed_tweets):
    for c, char in enumerate(typed_line):
        if ord(char) == ord(tweets[t][c]):
            score.append(1)
        else:
            score.append(0)

print(f"\n--------------------------------\nAccuracy: {int(sum(score)/len(score) * 100)}%")


