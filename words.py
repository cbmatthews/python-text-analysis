# DATA 620 Assignment 12
# Written by Carlton B. Matthews II
# Last Updated 20 April 2016
# Write a program to determine the word 
# frequencies given a text file. 

import helper #utility file
import csv #csv Writer Package

try:
	# Get the blobs of text from the below files
    blob1977 = helper.getText("BH-1977.txt")
    blob1987 = helper.getText("BH-1987.txt")
    blob1997 = helper.getText("BH-1997.txt")
    blob2007 = helper.getText("BH-2007.txt")
    blob2015 = helper.getText("BH-2015.txt")

    # Get Sorted Lists of words and their frequencies
    sort1977 = helper.getSortedList(blob1977)
    sort1987 = helper.getSortedList(blob1987)
    sort1997 = helper.getSortedList(blob1997)
    sort2007 = helper.getSortedList(blob2007)
    sort2015 = helper.getSortedList(blob2015)

    
    # Build the csv file usinf the csv.writer package 
    with open('BH-WordList.csv', 'w') as f:  
    	csvWriter = csv.writer(f, delimiter=',')
    	for s in sort1977: #Write words with counts higher than 10

    		s += ('1977',) #tag with the year
    		if int(s[0]) > 10:
    			if s[1].isdigit() == False: #remove any numbers
    				csvWriter.writerow(s)

    	for s in sort1987:
    		s += ('1987',) #tag with the year
    		if int(s[0]) > 10: #Write words with counts higher than 10
    			if s[1].isdigit() == False: #remove any numbers
    				csvWriter.writerow(s)

    	for s in sort1997:
    		s += ('1997',) #tag with the year
    		if int(s[0]) > 10: #Write words with counts higher than 10
    			if s[1].isdigit() == False: #remove any numbers
    				csvWriter.writerow(s)

    	for s in sort2007:
    		s += ('2007',) #tag with the year
    		if int(s[0]) > 10: #Write words with counts higher than 10
    			if s[1].isdigit() == False: #remove any numbers
    				csvWriter.writerow(s)

    	for s in sort2015:
    		s += ('2015',) #tag with the year
    		if int(s[0]) > 10: #Write words with counts higher than 10
    			if s[1].isdigit() == False: #remove any numbers
    				csvWriter.writerow(s)

    f.close() #close the csv file

except IOError: #File Not Found Error
    print("File Not Found")
except Exception: #Generic File Error
    print("An Error occured in File")
