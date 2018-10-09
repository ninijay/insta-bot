#!/usr/bin/env python
import requests
import json
from pprint import pprint
import urllib.request
import os
import random
import time

with open('config.json') as f:
    data = json.load(f)

cats = ["cyberpunk", "coding", "cyber"]
access = data["access"]
usr = data["usr"]
pw = data["pw"]
desc = ""
name = ""
def getQuote():
	global desc
	url = "https://talaikis.com/api/quotes/random/"
	r = request.get(url)
	d = json.loads(r.text)
	desc = d["quote"]

def fetchImg(cat):
	url = "https://api.unsplash.com/photos/random?query={}&client_id={}".format(cat,access)
	r = requests.get(url)
	image = json.loads(r.text)
	imgUrl = image["urls"]["regular"]
	global name 
	name = "{}.jpg".format(image["id"])
	urllib.request.urlretrieve(imgUrl,name)
	getQuote()

def post():
	cmd = "instapy -u {} -p \"{}\" -f {} -t \"{}\"".format(usr, pw, name, desc)
	os.system(cmd)
	os.remove(name)

def exe():
	global cats
	global desc
	secure_random = random.SystemRandom()
	curr_cat = secure_random.choice(cats)
	fetchImg(curr_cat)
	desc += "\n#{}".format(curr_cat)
	post()

starttime=time.time()
hours = 2
t_pad = 60.0*60.0*hours

while True:
	exe()
	time.sleep(t_pad - ((time.time() - starttime) % t_pad))	
	
