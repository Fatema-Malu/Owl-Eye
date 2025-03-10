from bs4 import BeautifulSoup
import requests
import json
url = 'http://ethans_fake_twitter_site.surge.sh/'
#url= 'http://ethans_fake_twitter_site.surge.sh/'
response=requests.get(url,timeout=5)
content= BeautifulSoup(response.content,"html.parser")
print(content)

#tweet = content.findAll('p', attrs={"class": "content"}).text
#print (tweet)

#for tweet in content.findAll('p', attrs={"class": "content"}):
    #print (tweet.text.encode('utf-8'))
tweetArr = []
for tweet in content.findAll('div', attrs={"class": "tweetcontainer"}):
    tweetObject = {
        "author": tweet.find('h2', attrs={"class": "author"}).text.encode('utf-8'),
        "date": tweet.find('h5', attrs={"class": "dateTime"}).text.encode('utf-8'),
        "tweet": tweet.find('p', attrs={"class": "content"}).text.encode('utf-8'),
        "likes": tweet.find('p', attrs={"class": "likes"}).text.encode('utf-8'),
        "shares": tweet.find('p', attrs={"class": "shares"}).text.encode('utf-8')
    }
    tweetArr.append(tweetObject)
with open('twitterData.json', 'w') as outfile:
    json.dump(tweetArr, outfile)
