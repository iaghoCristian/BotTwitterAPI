# importing the module 
import tweepy 

# personal details 
consumer_key ="axAbsBLpzIECnQ00JdTcghxoR"
consumer_secret ="C9PLzlHVdsbRzvmIvVZTGQww9GHvCSUS3t94nr8rblvab35kJJ"
access_token ="1201934223050981376-wbmZVP6TQ3ffMctN8xB8LCaVwZf4uj"
access_token_secret ="KKirNzKNSF1HwyYn13cE9QZaviXO5lOoRAQkuT93fc9ql"

# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 

# update the status 
api.update_status(status ="Hello Everyone !") 
