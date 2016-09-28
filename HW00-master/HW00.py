# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 09:09:27 2016

@author: z00193k
"""

# 1. Write a program that reads a string and returns a table of the letters of the alphabet in 
#    alphabetical order which occur in the string together with the number of times each letter occurs. 
#    Case should be ignored. 

sentence = 'ThiS is String with Upper and lower case Letters'
sentence = sentence.lower()

counts = {}
for char in sentence:
    if char not in counts:
        counts[char]=1
    else:
        counts[char] = counts[char] + 1
counts = sorted(counts.items())
    
for i in counts:
    print(i[0],i[1])
    
# 2. Give the Python interpreter’s response to each of the following from a continuous interpreter session:

# d = {"apples": 15, "bananas": 35, "grapes": 12}
# d["bananas"]
# d["oranges"] = 20
# len(d)
# "grapes" in d
# d["pears"]
# d.get("pears", 0)
# fruits = list(d.keys())
# fruits.sort()
# print(fruits)
# del d["apples"]
# "apples" in d
# Be sure you understand why you get each result. Then apply what you have learned to fill in the 
# body of the function below:

def add_fruit(inventory, fruit, quantity=0):
    if fruit not in inventory:
        inventory[fruit]=quantity
    else:
        inventory[fruit]+=quantity
    print inventory
    
        
    

# Make these tests work...
new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)

#3. Write a program called alice_words.py that creates a text file named alice_words.txt 
#   containing an alphabetical listing of all the words, and the number of times each occurs, 
#   in the text version of Alice’s Adventures in Wonderland. 
#!/usr/bin/python
file=open("alice.txt","r+")
#dictionary to hold the words and their corresponding frequency
wordcount={} 
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1      
#4. What is the longest word in Alice in Wonderland? How many characters does it have?
listWords = list(wordcount.keys())
wordLen = 0
for word in listWords:
    if len(word)>wordLen:
        wordLen=len(word)
        wordLong=word
        
print wordLong, wordLen
file.close();
