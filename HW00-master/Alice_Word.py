# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 07:17:27 2016

@author: z00193k
"""
import numpy as np

file=open("alice.txt","r+")
#dictionary to hold the words and their corresponding frequency
wordcount={} 
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

wordcount = sorted(wordcount.items())
print (wordcount)

np.save('alice_word.txt', wordcount) 
file.close();
