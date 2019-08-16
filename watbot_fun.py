import nltk
import numpy as np
import random
import string 
import pandas as pd

#whatsapp integration
import wat0

#initializing & qrcode fetching
braw = wat0.start()
wat0.getQr(braw)

#start conver
w_name = input('Enter name: ')
wat0.sNS(w_name,braw)

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def greeting(sentence):

    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize)
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you. Please contact the management"
        return robo_response
    elif req_tfidf<0.5:
        robo_response=robo_response+sent_tokens[idx]+"I'm not sure of it though!"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response

df=pd.read_csv("chatfun.csv")

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
sentences = []

#for i in 0
for s in df['Questions']:
    sentences.append(s)
    
    #sentences.append(sent_tokenize(s))
#sentences = [y for x in sentences for y in x] # flatten list

#m=len(sentences)
l=[]
o=[]
pair=[]
#for i in range (0,m):
i=0
for s in sentences:
    l.append([s,i])
    o.append([df['Answers'][i],i])
    pair.append([s,df['Answers'][i]])
    i=i+1
   # wat0.sendMsg()

q_tokens=[]
q2=len(l)
for i in range (0,q2):
    q_tokens.append(l[i][0])

para=" ".join(q_tokens)

q_words=nltk.word_tokenize(para)

punc=['.',',','?']
q_words=[i for i in q_words if i not in punc]

sent_tokens=q_tokens
word_tokens=q_words

flag=True
a=''
wat0.sendMsg("ROBO: My name is Robo. I will answer your queries about Chatbots. Greet me with a 'hi' to begin. If you want to exit, type 'bye'.You can then also access Management details.",braw)
while(flag==True):
    user_response_t = wat0.untilNew(braw,wat0.lastRcvd(braw))
    user_response = user_response_t.rstrip().split('\n')[0]
    print("ur: ",user_response)
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            wat0.sendMsg("ROBO: You are welcome..",braw)
        else:
            if(greeting(user_response)!=None):
                wat0.sendMsg("ROBO: "+greeting(user_response),braw)
            else:
                testmsg = 'ROBO: '
                #wat0.sendMsg("ROBO: ",braw)
                a=response(user_response)
                #wat0.sendMsg(a)
                for s in pair:
                    #wat0.sendMsg(s[0])
                    if s[0]==a:
                        testmsg = testmsg+s[1]
                wat0.sendMsg(testmsg,braw)
                sent_tokens.remove(user_response)
                
    else:
        flag=False
        wat0.sendMsg("ROBO: Bye! take care..",braw)
        wat0.quit(braw)
