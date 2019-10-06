import json
import urllib.request
from watsonAnalysis import getScore
from populateDb import populateDb

#Search for the comments on yt and conevert it into a Json and then into a dictionary
def searchComments(video_id, api_key):
    url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={api_key}"
    json_url = urllib.request.urlopen(url)
    data = json.loads(json_url.read())
    filterInfo(data)

#selects the information we need on our DB
def filterInfo(data):
    counter = 0
    for i in data["items"]:
        name = i["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
        comment = i["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
        link =  i["snippet"]["topLevelComment"]["snippet"]["authorChannelUrl"]
        try:
            populateDb(name, comment, link, counter, getScore(comment))
        except:
            continue

        counter +=1



