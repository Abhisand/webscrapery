import builtins
from fileinput import filename
import os
import requests
from PIL import Image
from bs4 import BeautifulSoup
from  io import BytesIO
import re

def start_search():

	search = input("Search for:")
	params = {"q" : search}

	dir_name = search.replace(" ","_").lower()

	if not os.path.isdir(dir_name):
		os.makedirs(dir_name)
	r = requests.get("http://www.bing.com/images/search",params=params)
	soup = BeautifulSoup(r.text,"html.parser")
	links = soup.findAll("a",{"class":"thumb"})

	for item in links:

		try:
			print("Getting", item.attrs["href"])
			img_obj = requests.get(item.attrs["href"])
			title = item.attrs["href"].split("/")[-1]
			img = Image.open(BytesIO(img_obj.content))
			img.save("./"+dir_name + "/"  + title,img.format)
		except:
			print("Could not saved")

	start_search()
start_search()