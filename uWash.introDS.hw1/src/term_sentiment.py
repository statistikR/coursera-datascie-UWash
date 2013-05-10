import sys
import os
import json

#path = "/Users/micha/Google Drive/WORKSPACE/travaille/side projects/Python/2013_UWash_IntroDataScience/datasci_course_materials/assignment1"
#os.chdir(path)



    
def createSentimentDict(afinnfile):
    
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # return dictionary    
    return scores


def main():
    ## open the 2 files that are added via the arguments
    #sent_file = open(sys.argv[1])
    sent_file = open("AFINN-111.txt")
    #tweet_file = open(sys.argv[2])
    tweet_file = open("/Users/micha/Google Drive/WORKSPACE/travaille/side projects/Python/2013_UWash_IntroDataScience/uWash.introDS.hw1/src/output_20.txt")
    
    ## create dictionary
    sentiDict = createSentimentDict(sent_file)
    newDict = {}
    
    ## process tweet_file
    
    sentiTweetList = [] #adds the sentiment of each tweet to list (e.g., first element, first tweet, etc
    #tweetNum = 0
    
    for line in tweet_file:
        tweet = json.loads(line).get('text',"xyxyempty").split()   #.keys() #[u"text"]
        sentCount = 0
        
        for word in tweet:
            sentCount += sentiDict.get(word,0)
            # if word not in sentiDict check if it's on new Dict
            if sentiDict.get(word) == None:
                
                
                # if word is not on newDict: add it and add sentiment score to list
                if newDict.get(word) == None:
                    newDict[word]=[]
                    
        # assign total tweet sentiment to list
        sentiTweetList.append(sentCount)
        
        

                    
                               
    # go through all tweets again from the beginning
    tweet_file.seek(0)
    tweetCounter = 0
    
    for line in tweet_file:
        
        tweet = json.loads(line).get('text',"xyxyempty").split()   #.keys() #[u"text"]
        
        # if word is newDict, add sentiment of tweet from sentiTweetList        
        for word in tweet:

            if newDict.get(word) != None:
                newDict[word].append(sentiTweetList[tweetCounter])

            
        tweetCounter += 1
            

            
        
     
    
    # go through all keys in dict and calculate the average of all values
    
    for key in newDict:
        newDict[key] = sum(newDict[key])/float(len(newDict[key]))
        
    
    # print results key-value pairs
    
    for key in newDict:
        print key.encode('ascii', 'ignore'), newDict[key]
 

    
    

    

if __name__ == '__main__':

    main()
    
    

    
