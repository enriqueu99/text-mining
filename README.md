# text-mining

Please read the [instructions](instructions.md).


Project Overview:
My project attempted to extract data from a reddit API(for a specific subreddit'wallstreet bets') and create meaningful sentiment analysis that may indicate aggregate interest. I extracted data from the reddit subreddit and stored the user inputs in a CSV file. I then refferenced that CSV file and utilized a natural language tool kit(NLTK) to help assess what the inputs meant via the Vader package. The Vader package accounts for emojis, grammar/punctuation, and word choice when determining the status of the data point(string). It aims to determine if the points are negative, neutral, or positive and then compounds these measurements to produce estimates for population distributions.

My code at a highlevel could be divided into three main groups. Firstly, I had to gain access to the Reddit API by retrieving a key and a secret phrase for my client. After that, I had to create an instance that allowed me to interact with their database. Once the data pathway   was establshed(and opened). I proceeded to incorporate the extraction(API calls) methods.I also had to import SIA, or the sentiment intensity analyzer. I created the first main function which would iterate through subreddit posts and add the data points to a blank set.To extract the data I had to output test the API calls I was utilziing (to better understand the formatting).I ended up utilizing the piece of information which I found most valuable (the "title" of the user comment). I then merely reformatted that data with pandas dataframe and stored it as a local CSV file.

Second came the data analysis. I chose to iterate through the 'headlines' variable wich was a proxy for our data-list.Then I utilized the SIA tool to determine a "poll score" for each individual instance within the list. Those scores were then appended to our 'results' variable, which was later utilized to append these scores to our original string values.

Lastly, I implemented the 'results' variable to create a new data frame. I then reformatted the data frame to include both a headline and a label, [headline,label], the label in this case was the pol score. With our new dataframe, we proceeded to count the instances of each value type(the pol scores). I chose to extract the percentage distributions for each value type.

I had to decide wether to refference the information locally (via a saved csv file) or on the computers functional memory and chose to save it locally instead to allow for transparency (with regards to the data formatting). I also had to choose between utilizing the pandas data frame or designing my own for the allocation of the extracted data. I ended up utilizing Pandas because I thought it more efficient ( and the syntax was simpler)

Results:
Results indicated a positive sentiment overall. The SIA tool expressed a higher percentage based occurance for positive and neutral value types.
The output  the SIA tool produced ...

0    54.545455  %
 1    30.367505 %
-1    15.087041 %
...
Name: label, dtype: float64



Those were the actual percentage distributions for each value type for my extracted data set.  Interestingly, I noted that the market preformed well, moreso a specific subset of stocks called "meme stocks". So the results were arguabbly "useful" or at least coorelated to a notable degree with these equities. In order to continue to refine the data produced and ultimatley allow for consistant, equity insights, we would need to explore the underlying assumptions for the SIA tool and continue to run the program over time with a much larger data set.
I did some research with regards to SIA tool and its structure and found dictionaries of data points and outputs. It was after this anslysis that I confirmed that the tool worked with an acceptable level of accuracy (with regards to sentiment analysis : however vague that metric may be).

Reflection:
Overall, I felt my visualization of the informational flow was my best attribute during the planning phases for the project. High level, I understood the order of operations to produce the output I wanted. Additionally, I was pleasantly surprised that API's, although unique from another, do resemble one another in terms of command formats. So I found the process of understanding the commands for the Rreddit API quite easy. As for estimating the scope of preperation for this project, I did understimate the amount of output testing that was required. Data formats can make data extraction very difficult and thus, undertanding how the information was packaged was by far the most challenging aspect of the project.