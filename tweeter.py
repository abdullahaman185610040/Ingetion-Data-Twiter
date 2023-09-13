import tweepy
import csv

acces_token = "1345645991379124225-5bV3urzmPE9AZ8q3Dlsdj9tFZkDs32"
acces_token_secret = "TrKiF9PVtV7ioKN5diOvFqI3iaQxSSBtjBnu5LfiwPZHh"
consumer_key = "XVlsJ2xG2c0MbEmunLrFEgb5R"
consumer_key_secret = "G2KIMrFh3Jei0tEClt8d93U0eze2ZaenqU5Dm7s4xGsxyjh8CX"

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
api = tweepy.API(auth)

csvFile = open('twitter.csv', 'w', newline='', encoding='utf-8')

csvWriter = csv.writer(csvFile)
for tweets in api.search_tweets(q="Jokowi", lang="id", count=200):
    text = tweets.text
    user = tweets.user.name
    created = tweets.created_at
    csvWriter.writerow([created, text.encode('utf-8'), user])

csvFile.close()