#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 13:19:20 2019

@author: harshsharda
"""

#Importing a text file initially to have a first look

initial_data = open('../data/SMSSpamCollection.tsv').read()
initial_data[0:500]

# Things to look for, \t and \n\
# Replacing the \t with \n and splitting them into lists

replaced_data = initial_data.replace('\t','\n').split('\n')

# Separating the Labels and the Text from the list above

labellist = replaced_data[0::2]
textlist = replaced_data[1::2]

# Creating a dataframe with the labellist and the textlist as columns
# Before that, checking the lengths of the 2 lists

len(labellist)
# Has 5571

len(textlist)
# Has 5570

# Checking why there is a mismatch in the labellist

print(labellist[-5:])
# So there is a missing value at the end

# Now creating a dataframe

import pandas as pd

completedata = pd.DataFrame({
        'label': labellist[:-1],
        'text': textlist})

# Now there is an easier way to do this. Since we have \t in the file, it means that it is tab delimited

completedata_pd = pd.read_csv('../data/SMSSpamCollection.tsv', sep = "\t", header = None)
completedata_pd.columns = ['label','text']



# DATA EXPLORATION

print(f'''The data has {len(completedata_pd)} rows and {len(completedata_pd.columns)} columns''')

## Checking how many ham/spam are there

ham_spam = completedata_pd.groupby(completedata_pd.label).count()

## How much missing data there is

print(completedata_pd.isnull().sum())


## Using Regular Expression examples to get a hang of how it works

import re


# Test examples: When
## Case1: Dealing with characters which split a word
re_test = 'This is a made up string to test 2 different regex methods'
re_test_messy = 'This      is a made up     string to test 2    different regex methods'
re_test_messy1 = 'This-is-a-made/up.string*to>>>>test----2""""""different~regex-methods'

# Splitting the sentence into a list of words

# When dealing with single spaced
re.split("\s",re_test)

# When dealing with more than just one space
re.split("\s+",re_test_messy)

# When dealing with punctuation marks
re.split("\W+",re_test_messy1)

## Case2: Finding characters which we don't need

# When dealing with a single spaced or more
re.findall("\S+",re_test)
re.findall("\S+",re_test_messy)

# When dealing with punctuation marks
re.findall("\w+",re_test_messy1)


# Test examples: Replacing the string

pep8_test = 'I try to follow PEP8 guidelines'
pep7_test = 'I try to follow PEP7 guidelines'
peep8_test = 'I try to follow PEEP8 guidelines'

