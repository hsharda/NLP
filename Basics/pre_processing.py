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

