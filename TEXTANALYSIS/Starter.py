#Importing praw (REDDIT API)
#Importing request module to interact with Reddit database
import nltk
import praw 
import requests
import json
import pandas as pd
import re
import csv


# variables for :Results for the sentiment analysis and SIA (utilzied)


#Client ID and Key needed for API communication
CLIENT_ID = 'CnNahd6wkmKVY5l5vUAvgQ'
SECRET_KEY = 'yammVtkX61Y4Kf-QV3DrKNbqyb45Ow'


#"Reddit instance" is created
user_agent = 'Scraper 1.0 by /u/TerribleCherry2392'
reddit = praw.Reddit(client_id=CLIENT_ID,client_secret=SECRET_KEY,
user_agent=user_agent

)


#checks if main file (SAFETY VALVE)
if __name__ == "__main__":

    def main():
        #sentiment analysis module
        nltk.download('vader_lexicon')
        from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
        headlines = set()
        sia = SIA()
        results = []
        #iterating through the subreddits user commments (.hot is a time based category)
        for submission in reddit.subreddit('wallstreetbets').hot(limit=None):
            headlines.add(submission.title)
    #use to check if the data is being recorded into the set    
        #print(len(headlines))** Used to check if data was being stored
        #create a dataframe for "headlines" using pandas repository
        df = pd.DataFrame(headlines)
        df.head()
        df.to_csv('headlines.csv', header=False, encoding='utf-8', index=False)







        #iterating through the lines of our CSV file 
        for line in headlines:
            #utilizing sia to assess the sentiment for given text data 
            pol_score = sia.polarity_scores(line)
            pol_score['headline'] = line
            #appending the pol-scores to 'results'
            results.append(pol_score)
        
        print(results[:])
        df = pd.DataFrame.from_records(results)
        df.head()
        df['label'] = 0
        #creating thresholds for values in our data-set to determine compounded sentiment analysis
        df.loc[df['compound'] > .2, 'label'] = 1
        df.loc[df['compound'] < -.2, 'label'] = -1
        df.head()
        df2 = df[['headline','label']]
        df2.to_csv('reddit_headlines_labels.csv',encoding ='utf-8', index = False)
        df2.label.value_counts()
        df.label.value_counts(normalize=True) *100
        #acquires percentages of value distributions
        #metric we wanted for aggregate sentiment analysis
        print(df.label.value_counts(normalize=True) *100)
        return df.label.value_counts(normalize=True) *100
    #calling Function
    
    main()
          
        
           
   
   



