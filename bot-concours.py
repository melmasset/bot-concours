import tweepy


consumer_key='CONSUMER_KEY'
consumer_secret='CONSUMER_SECRET'
access_token='ACCESS_TOKEN'
access_token_secret='ACCESS_TOKEN_SECRET'

msg = str(input("Which message do you want to send ?"))
nb = int(input("How many times (be careful you can be restricted)"))
twee = int(input("Tweet ID to answer"))

client = tweepy.Client(consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret, wait_on_rate_limit=True)


for i in range(nb):
	response = client.create_tweet(text=msg, in_reply_to_tweet_id = twee)

print(response)
