#!/usr/bin/python3


#Part A
#take this number 112345678911234566 and count the number of 2s in the string and print out the number.


#This is to take a number and count the 2s and print the number.
#Usage: python3 HW3.2.1.py

#Enter number at string 
Num = '112345678911234566'


#Print out the .count function of the number of 2's in my string
print(Num.count('2'))




#Part B


#take a sentence from user input, turn it all to lowercase letters and remove the spaces and count the length and print out the length. You choose the sentence.

#This will take a user input sentence and turn it to one lowercase string and count and print the length.

#User input statment

sentence = input("Enter a sentence: ")

#Turn to all lowercase

sentence = sentence.lower()

#Remove spaces

sentence = sentence.replace(" ", "")

#Count letters in sentence

count = len(sentence)

print(count)
