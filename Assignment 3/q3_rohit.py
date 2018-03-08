# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 18:19:59 2018

@author: rabhishe
"""
#Importing the libraries
from nltk.corpus import wordnet as w

from nltk.stem import LancasterStemmer , WordNetLemmatizer
from nltk import pos_tag,ne_chunk, ngrams
from collections import Counter
import urllib.request
from bs4 import BeautifulSoup
from urllib import request
import requests
import pandas as pd
import os
import nltk
import collections 
import matplotlib.pyplot as plt
nltk.download('gutenberg')
nltk.download('genesis')
nltk.download('inaugural')
nltk.download('nps_chat')
nltk.download('webtext')
nltk.download('treebank')
nltk.download('punkt')
from nltk.book import *

from nltk.tokenize import word_tokenize,sent_tokenize,wordpunct_tokenize


#Input file
raw = open('ebook.txt')
f=raw.read()# Reading the file

#Applying Lemmatization on the words
words=[]
with open('ebook.txt','r') as f:
    for line in f:
        for word in line.split():
           words.append(str(word))  

print ("Applying Lemmatization")  
l=WordNetLemmatizer()
lemmatize=map(l.lemmatize,words)
for i in lemmatize:
    print (i)

#Applying bigram to text
token = nltk.word_tokenize(f)

#Calculating the word frequency (bi-gram frequency) of the words(bi-grams)
print ("Calculating the word frequency (bi-gram frequency) of the words(bi-grams)")
bigrams = ngrams(token,2)
print (Counter(bigrams))

#Choosing top five bi-gramsthat has been repeated most
print ("Choosing top five bi-gramsthat has been repeated most")
a=Counter(ngrams(token,2)).most_common(5)
bigrams.plot(10)
print (a)

b=[]
for i in range(len(a)):
    b.append(a[i][0])
print (b)
c=[]
for j in range(len(b)):
    #print(b[j][0]+" "+b[j][1])
    c.append(b[j][0]+" "+b[j][1])
#print (c)
new_line=""
print ("printing all the lines which has the most repeated bi-grams")
for line in raw:
    #print (line)
    for bgrm in c:
        if bgrm in line:
            print (line) #printing all the lines which has the most repeated bi-grams
            new_line=new_line+line #Concatenating the lines which has the most repeated bi-grams
            
print ("printing the concatenated lines with most repeated bi-grams")
print(new_line) #printing the concatenated lines with most repeated bi-grams
