import sys
import os
import json

#path = "/Users/micha/Google Drive/WORKSPACE/travaille/side projects/Python/2013_UWash_IntroDataScience/datasci_course_materials/assignment1"
#os.chdir(path)


def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
    
def createSentimentDict(afinnfile):
    
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # return dictionary    
    return scores


def main():
    ## open the 2 files that are added via the arguments
    sent_file = open(sys.argv[1])
    #sent_file = open("AFINN-111.txt")
    tweet_file = open(sys.argv[2])
    #tweet_file = open("/Users/micha/Google Drive/WORKSPACE/travaille/side projects/Python/2013_UWash_IntroDataScience/uWash.introDS.hw1/src/output_20.txt")
    
    ## create dictionary
    sentiDict = createSentimentDict(sent_file)
    
    ## process tweet_file
    
    for line in tweet_file:
        tweet = json.loads(line).get('text',"xyxyempty").split()   #.keys() #[u"text"]
        sentCount = 0
        
        for word in tweet:
            sentCount += sentiDict.get(word,0)
           
        print sentCount

    
    

    

if __name__ == '__main__':

    main()
    
    

    
