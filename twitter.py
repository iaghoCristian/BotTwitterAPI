import tweepy
import sys
import time
import request

def tweetar():
	consumer_key = "axAbsBLpzIECnQ00JdTcghxoR"
	consumer_secret = "C9PLzlHVdsbRzvmIvVZTGQww9GHvCSUS3t94nr8rblvab35kJJ"
	acess_key = "1201934223050981376-wbmZVP6TQ3ffMctN8xB8LCaVwZf4uj"
	acess_secret = "KKirNzKNSF1HwyYn13cE9QZaviXO5lOoRAQkuT93fc9ql"
	
	auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
	auth.set_acess_token(acess_key,acess_secret)
	api = tweepy.API(auth)
	
	responseData = request.get("http://api.icndb.com/jokes/random/?escape=javascript")
	mystatustext = str(responseData.json()['value']['joke'])
	api.update_status(status=mystatustext)

def main():
	print("Bem vindo ao sistema de Publicacao")

while True:
	tweetar()
time.sleep(60)

if __name__ == "__main__":
	main()
