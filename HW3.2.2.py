#!/usr/bin/python3

#Create a documented python script that will do the following two things. For each task, first write the pseudocode, comment out the pseudocode and beneath the pseudocode write the script.

#a). Create a list of numbers (any numbers you like). Then loop through the items in the list adding 1 to every number and print those numbers.

#Create a list of number
#Create a new lsit to store changed numbers
numbers = [1, 2, 3, 4, 5]
new = []

#Loop that adds 1 to each number
# For num in numbers: do num+1 to new list

for num in numbers:
	new.append(num+1)


#print out new numbers

print(new)


#b) Create a dictionary of animals and their sizes (make up whatever you want). Print out the keys of the dictionary. Make a list of all the animals and then write an if else statement to print out the animal name and the word “big” if the weight is over 20 grams and the word “small” if the weight is less than 20 grams.

animal_dict = { 'dog':22, 'cat':18, 'rat':7,}


#Loop through to print out keys, and say big is over 20g and small if under 20g
for key, value in animal_dict.items():
	if value > 20:
		print(key, ' is big')
	else:
		print(key, ' is small')




