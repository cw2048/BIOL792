#!/usr/bin/python3

#Create a documented python script that will open up the file “Bloom_etal_2018_Reduced_Dataset”. Read through the file and print out the taxon name and their diadromous status. Add up all of the log body sizes and print out the total log body size for all the individuals in the file.
#Usage: python3 HW3.2.3.py Bloom_etal_2018_Reduced_Dataset.csv




#Import packages

import sys
import re


#Read in file as system input
Infile = sys.argv[1]
#Open file as reading
IN = open(Infile, 'r')


#Open new file to print output
OUT = open('hui_out.txt', 'w')

#Create a blank list for log totals
tot_log = 0

#Create a loop that prints out the taxon name (column 1) and diadromous (column 4). And then add all of log size (column 2) together
for line in IN:
	#need to eliminate the first line so the numbers in the rest of the colomn will add. Gave it a header name
	if re.search("taxa", line):
		OUT.write("Taxa and Diadromous")
	else:
		#Now onto printing out the names and dias and adding together all logs
		#Remove line ending
		line = line.strip("\n")
		#Split the line into the columns by the , (csv)
		line = line.split(',')
		#add each item I want into a list (with in the loop, will change for every line)
		tax = line[0]
		dia = line[3]
		#Be sure to sepcify log as a float number so we can do math with it
		log = float(line[1])
		#Writing out all the taxa names and dias for them
		OUT.write("%s " % (tax))
		OUT.write("%s \n" % (dia))
		#Adding all the logs of each line together into the item tot_log
		tot_log += log


#now printing out the total log size at the end of the file
OUT.write("Total Log Size is: %.2f" % (tot_log))
#Print it to screen too
print(tot_log)


#close file we are writing out too
OUT.close()
