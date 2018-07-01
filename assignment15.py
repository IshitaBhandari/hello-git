#ASSIGNMENT ON REGULAR EXPRESSIONS:

#Question 1: Extract user id,domain name and suffix from the given email addresses.
emails="zuck@facebook.com page33@google.com jeff42@amazon.com"
import re
pattern=r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})'
print("Output:")
print(re.findall(pattern,emails,re.IGNORECASE))

#Question 2: Retrieve all words starting with 'b' or 'B' from the given text.
text = 'Betty bought a bit of butter, But the butter was so bitter , So she bought some better butter, To make the bitter butter better.'
#print(text)
import re
print(re.findall(r'\bB\w+',text,flags=re.IGNORECASE))

#Question 3: Split the given irregular sentence into words.
import re
sentence='"A,very very;irregular_sentence"'
num=re.sub(r'[_,;]'," ",sentence)
print("Output_Sentence :",num)

#Question 4: Clean up the given tweet so that it contains only user's message. Remove all URLs,hashtags,mentions,punctuations,RTs and CCs.
tweet="'Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'"
import re
def clean_tweets(tweet):
    #remove URLs
    tweet=re.sub('http\S+\s*',' ',tweet)
    #remove RT and cc
    tweet = re.sub('RT|cc', ' ', tweet)
    #remove hashtags
    tweet = re.sub('#\S+', ' ', tweet)
    #remove mentions
    tweet = re.sub('@\S+', ' ', tweet)
    #remove punctuations
    tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_'{|}~"""), ' ', tweet)
    #remove extra whitespace
    tweet=re.sub('\s+',' ',tweet)
    return tweet

print(clean_tweets(tweet))