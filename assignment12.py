#Q.1. Write short note on Access token and generate access token.
#A token is used to make security decisions and to store tamper-proof information about some system entity.
#While a token is generally used to represent only security information,
#it is capable of holding additional free-form data that can be attached while the token is being created.
#Tokens can be duplicated without special privilege, for
#example to create a new token with lower levels of access rights to restrict the access of a launched application.
#An access token is used by Windows when a process or
#thread tries to interact with objects that have security descriptors (securable objects).




#Q.2.get the ip address of some common sites..
#ns lookup facebook.com
#ns lookup google.com
#$ nslookup google.com
#Non-authoritative answer:
#Server:  google-public-dns-a.google.com
#Address:  8.8.8.8

#Name:    google.com
#Addresses:  2404:6800:4002:807::200e
 #         172.217.24.238

#$ nslookup facebook.com
#Non-authoritative answer:
#Server:  google-public-dns-a.google.com
#Address:  8.8.8.8

#Name:    facebook.com
#Addresses:  2a03:2880:f10c:283:face:b00c:0:25de
 #         31.13.78.35




#.Q.3. Using Tweepy library try to extract tweets from Twitter.
#import tweepy
#consumer_key=''
#consumer_secret=''
#access_token=''
#access_token_secret=''
#auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
#auth.set_access_token(access_token,access_token_secret)
#api=tweepy.API(auth)
#tweets=api.search('#barcelona',lang="en",count=3,tweet_mode="extended")
#for tweet in tweets:
 #   print("sports")
  #  print(tweet.full_text)
   # print("footballer")

#Q.4.Difference Between library and API.
#objects that serves one particular purpose. you could use a library in a variety of projects. (Various specialized services in our case)
#An API is an interface for other programs to interact with your program or library  without having direct access. ( giving specifications for our need to various vendors in our case)

#The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming.
#For example : Numpy is a library of Python, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
#We can create our own APIs using Python Framework like Django and Flask which can be used in websites.
