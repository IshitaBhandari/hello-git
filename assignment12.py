# ASSIGNMENT ON CONCEPTS OF API.
# question 1: What is an access token? Generate your access token for any API(example: Twitter,Spotify,etc)

"""
An access token is a unique string of letters and numbers that you pass with every API call.")
Each access token is associated with:
                Your API application,
                The user you are acting on behalf of
    and         the permissions your app has for that user"
It can be any type of token(such as opaque string or JWT).
Its purpose is to inform the API that the bearer of this token has been authorized to access the API and perform specific actions.
"""
# twitter(access_token)='z00Xy9AkHwp8vSTJ04L0'

# question 2: Get the IP address of some common sites like Google,Facebook by using DNS lookup.

import socket

addr1 = socket.gethostbyname("www.google.com")
addr2 = socket.gethostbyname("www.facebook.com")

print("IP of google:", addr1)
print("IP of facebook:", addr2)

"""Google :172.217.9.164
   Facebook:157.240.18.35"""

# question 3: Using Tweepy library try to extract tweets from Twitter.

import tweepy
import json

# Consumer keys and access tokens, used for OAuth
consumer_key = '7EyzTcAkINVS3T2pb165'
consumer_secret = 'a44R7WvbMW7L8I656Y4l'
access_token = 'z00Xy9AkHwp8vSTJ04L0'
access_token_secret = 'A1cK98w2NXXaCWMqMW6p'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)


def get_tweet():
    hash_tag = input("\nEnter the word without the hashtag")
    hash_tag = "#" + hash_tag
    tweets = api.search(hash_tag)
    return tweets


# question 4: What is the difference between library and API. Figure it out with examples.
""" API:  An API is really no more than a set of method signatures and other information necessary to use a class or set of classes.
          The API is totally distinct from the implementation.
          For example, a number of vendors have implemented the servlet API, each in a different way.
          The API by itself has no implementation.
          An API is a description (documentation or list) of methods and data.
          API is a part of library which is exposed to the user.
          So whatever documentation we have regarding a library, we call it an API Documentation because it contains only those classes and functions to which we have access.

    LIBRARY:A library is pre-compiled code (dll or lib) and will contain classes of coded functionality.
            Library is a set of all classes and functions that can be used from our code to do our task easily.
            But the library can contain some of its private functions for its usage which it does not want to expose.
            Library is a unit of deployment of one, many or part of API.
            For example, a Bitmap Processing library will provide facilities for loading and manipulating bitmap images, saving you having to write all that code for yourself.
            Typically a library will only offer one area of functionality (processing images or operating on zip files)"""

# question 5: Try to access spotify API. Find out some library for it and play some music.
import pprint
import sys
import os
import subprocess
import spotipy
import spotipy.util as util

if len(sys.argv) > 2:
    username = sys.argv[1]
    playlist_name = sys.argv[2]
    playlist_description = sys.argv[3]
else:
    print("Usage: %s username playlist-name playlist-description" % (sys.argv[0],))
    sys.exit()
token = util.prompt_for_user_token(username)
if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    playlists = sp.user_playlist_create(username, playlist_name, playlist_description)
    pprint.pprint(playlists)
else:
    print("cant get token for", username)