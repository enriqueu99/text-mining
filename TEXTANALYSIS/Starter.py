#Importing praw (REDDIT API)
#Importing request module to interact with Reddit database

import praw 
import requests
import json
import pandas as pd
import re
import csv

#Client ID and Key needed for API communication
CLIENT_ID = 'CnNahd6wkmKVY5l5vUAvgQ'
SECRET_KEY = 'yammVtkX61Y4Kf-QV3DrKNbqyb45Ow'


#"Reddit instance" is created
user_agent = 'Scraper 1.0 by /u/TerribleCherry2392'
reddit = praw.Reddit(client_id=CLIENT_ID,client_secret=SECRET_KEY,
user_agent=user_agent

)
#blank set is created to store the data




def main():
    headlines = set()
    
    for submission in reddit.subreddit('wallstreetbets').hot(limit=None):
        headlines.add(submission.title)
        
    print(len(headlines))
    
    df = pd.DataFrame(headlines)
    df.head()
    df.to_csv('headlines.csv', header=False, encoding='utf-8', index=False)





#creating the object for the CSV file where the data is stored

def filter(f):
    counter =0
    keywordlist = ['GME','gme','Gme','AMC','amc']
    
    with open('headlines.csv', 'rt') as f:
     reader = csv.reader(f, delimiter=',') 
     for row in reader:
          for field in row:
              if field == any(keywordlist):
                  counter = counter +1

    return counter




if __name__ == "__main__":
    #print(counter)
    
    filter()
   
    #main()
    
    #print(len(infor3))

    #print(infor3)
 



