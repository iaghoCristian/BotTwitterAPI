import tweepy,sys,time
import request

def tweetar():
	consumer_key = "xxx"
	consumer_secret = "xxx"
	acess_key = "xxxx"
	acess_secret = "xxxx"
	
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
