#Importing praw (REDDIT API)
#Importing request module to interact with Reddit database

import praw 
import requests

CLIENT_ID = 'CnNahd6wkmKVY5l5vUAvgQ'
SECRET_KEY = 'yammVtkX61Y4Kf-QV3DrKNbqyb45Ow'


#Reddit API objects
user_agent = 'Scraper 1.0 by /u/TerribleCherry2392'
reddit = praw.Reddit(client_id=CLIENT_ID,client_secret=SECRET_KEY,
user_agent=user_agent

)


def main():

    for submission in reddit.subreddit('wallstreetbets').hot(limit=None):
        
        infor=list()
        
        print(submission.title)
        print(submission.id)
        print(submission.author)

        infor.add(submission.title)
        infor.add(submission.id)
    
    print(len(infor))

infor = list()





if __name__ == "__main__":
 
    print(len(infor))
 



