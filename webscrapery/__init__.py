from bs4 import BeautifulSoup
import requests

search = input("Enter Search for:")
params = {"q":search}

r = requests.get("https://www.bing.com/search",params=params)
soup = BeautifulSoup(r.text , "html.parser")
results = soup.find("ol",{"id":"b_results"})
links = results.findAll("li",{"class":"b_algo"})
#abhi = results.find("div",{"class":"b_caption"})
for item in links:
	item_text = item.find("a").text
	item_href = item.find("a").attrs["href"]
	#item_abhi = item.find("a").text

	if item_text and item_href:
		print(item_href)
		print(item_text)
		print("Summary:",item.find("a").parent.parent.find("a").text)
		#print("Abhishek",item_abhi)