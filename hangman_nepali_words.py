# -*- coding: utf-8 -*-
"""Hangman Nepali words.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_ZKLxjmZ_ULTnNLirIi_rHFFw9jSfeTs
"""

import random
import pandas as pd
import math
import string

def get_words(choice):
  choice=int(choice)
  if choice==1:
    df=pd.read_csv("districts.csv")
    word=df.sample(axis=0,n=1)
    word=word.iloc[0]['District']
    return word
  if choice==2:
    df=pd.read_csv("Actors.csv")
    word=df.sample(axis=0,n=1)
    word=word.iloc[0]['Actors']
    return word
  if choice==3:
    df=pd.read_csv("Singers.csv")
    word=df.sample(axis=0,n=1)
    word=word.iloc[0]['Singers']
    return word
  
  if choice==4:
    df=pd.read_csv("Movies.csv")
    word=df.sample(axis=0,n=1)
    word=word.iloc[0]['Movies']
    return word

def play():
  n=0
  f=0
  s=0
  str=""
  print("Choose your choices of words to pick from \n 1.Nepali District Names \n 2.Nepali Actor names \n 3.Nepali singer name \n 4.Nepali Movies Name \n ")
  choice = input()
  word=get_words(choice)
  word=word.upper()
  jumbled_words="-" * len(word)
  jumbled_words=list(jumbled_words)
  new_word=[]
  
  for i in range(len(word)):
    if word[i] == " ":
      jumbled_words[i] = " "

      f=f+1
      if i % 5 == 0:
        jumbled_words[i]=word[i]
        continue
    if i % 5 == 0:
      jumbled_words[i]=word[i]
      if word.count(jumbled_words[i]) > 1:
        for m in range(len(word)):
          if word[m] == word[i]:
            jumbled_words[m]=word[i]
      f=f + word.count(jumbled_words[i])
  print(str.join(jumbled_words))
   
  while n < 6 and f < len(word) :
    guessed_words = []
    
    guessed_words = input()
    guessed_words=guessed_words.upper()
    if guessed_words == str:
      print("Please type a letter")
      continue
    j = word.find(guessed_words)
    number_of_occurences=word.count(guessed_words)
    if j is not -1:
      k=j
      f= f + number_of_occurences
      for cou in range(number_of_occurences):
        jumbled_words[k] = guessed_words
        word=list(word)
        word[k] = "+"
        
        word = str.join(word) 
        k = word.find(guessed_words)
        
      print(str.join(jumbled_words))
    else:
      print("sorry try again")
      print("Chances remaining:", 5-n)
      n=n+1
      
      print(str.join(jumbled_words))
  if f == len(word):
    print("You Won")
  else: 
    print("You Lose")
  print("\n")
  print("Do you Want to Try Again? /n Press Y for Yes and N for No")
  try_again=input()
  if try_again.upper() == "Y":
     play()
  else:
    print("THANKS FOR PLAYING")

print(play())



