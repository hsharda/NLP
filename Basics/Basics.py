#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 13:19:20 2019

@author: harshsharda
"""

#Importing a text file initially to have a first look

initial_data = open('SMSSpamCollection.tsv').read()
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

completedata_pd = pd.read_csv('SMSSpamCollection.tsv', sep = "\t", header = None)

