import sys
import os
import json


def main():
    ## open the tweetfile
    tweet_file = open(sys.argv[1])
    #tweet_file = open("/Users/micha/Google Drive/WORKSPACE/travaille/side projects/Python/2013_UWash_IntroDataScience/uWash.introDS.hw1/src/output_20.txt")
    
    ## create dictionary and counter for total tokens

    freqDict = {}
    sumOfTokens = 0.0
    
    ## process tweet_file, add all words to dictionary and count them
    
    for line in tweet_file:
        tweet = json.loads(line).get('text',"xyxyempty").split()   #.keys() #[u"text"]
        
        for word in tweet:
            sumOfTokens += 1
            if freqDict.get(word) == None:
                freqDict[word] = 1
            else:
                freqDict[word]+= 1
    
    ## divide all counts in dict by total
    
    for key in freqDict:
        freqDict[key] = freqDict[key] / sumOfTokens
                

    ## output relative frequency
    
    for key in freqDict:
        
        print key, freqDict[key]
                
    
     

if __name__ == '__main__':

    main()
    
    

    
