#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 23:13:08 2019

@author: harshsharda
"""

# The aim is to understand what goes under the hood of pre-processing text data

import pandas as pd
import string # To remove punctuations
import re # For tokenization
import nltk # For removing stopwords 

# Reading csv and creating variable names
completedata_pd = pd.read_csv('../data/SMSSpamCollection.tsv', sep = "\t", header = None)
completedata_pd.columns = ['label','text']

# Building a function to remove punctuations

def remove(text):
    for c in string.punctuation:
        text=text.replace(c,"")
    return text

completedata_pd['clean_text']= completedata_pd['text'].apply(remove)

# Building a function to tokenize

def tokenize(clean_text):
    return re.split('\W+',clean_text)

completedata_pd['clean_text_tokens']= completedata_pd['clean_text'].apply(lambda x: tokenize(x.lower()))

# Building a function to remove stopwords

stopwords = nltk.corpus.stopwords.words('english')

def remove_stopwords(tokenize_col):
    stop = [words for words in tokenize_col if words not in stopwords]
    return stop

completedata_pd['final_clean_text']= completedata_pd['clean_text_tokens'].apply(lambda x: remove_stopwords(x))