#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 23:13:08 2019

@author: harshsharda
"""

# The aim is to understand what goes under the hood of pre-processing text data

import pandas as pd

completedata_pd = pd.read_csv('../data/SMSSpamCollection.tsv', sep = "\t", header = None)
completedata_pd.columns = ['label','text']

import string # To remove punctuations
import re # For tokenization

# Building a function to remove punctuations

def remove(x):
    for c in string.punctuation:
        x=x.replace(c,"")
    return x

completedata_pd['clean_text']= completedata_pd['text'].apply(remove)

# Building a function to tokenize

def tokenize(x):
    return re.split('\W+',x)

completedata_pd['clean_text_tokens']= completedata_pd['clean_text'].apply(lambda x: tokenize(x.lower()))