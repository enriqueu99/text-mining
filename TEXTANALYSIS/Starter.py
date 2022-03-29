#Importing praw (REDDIT API)
#Importing request module to interact with Reddit database

import praw 
import requests
import json
#Client ID and Key needed for API communication
CLIENT_ID = 'CnNahd6wkmKVY5l5vUAvgQ'
SECRET_KEY = 'yammVtkX61Y4Kf-QV3DrKNbqyb45Ow'


#"Reddit instance" is created
user_agent = 'Scraper 1.0 by /u/TerribleCherry2392'
reddit = praw.Reddit(client_id=CLIENT_ID,client_secret=SECRET_KEY,
user_agent=user_agent

)
infor = set()
infor2 = set()
infor3 = set()
usernames= set()


def main():

    for submission in reddit.subreddit('wallstreetbets').hot(limit=None):
    
        infor3.add(submission.title)
        
    print(len(infor3))
    
    
    for i in usernames:
         requests.get(r'http://www.reddit.com/user/[username]/comments/.json')

    
    



if __name__ == "__main__":
    
    main()
    
    print(len(infor3))

    print(infor3)
 



