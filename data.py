'''
Function   : Creates data.csv
Description: This program generates data using random and puts in a file of type csv
'''

#importing the csv, random and matplotlib
import csv
import random

#I'm going to take years from 1900- 2022 and random numbers from 0-6.0 as inflation rate.
header = ['year', 'inflation'] #declaring header list
data = []

#generating random data from range 0 to 6 using random function for everyyear from 1900 to 2022
for i in range(1900,2023):
    v=round(random.uniform(0.0,6.0),2)
    data.append([i,v]) #appending year and inflation data as a list in a data list

#print(data)

#writing the data in a list to a csv file using file handling in python
with open("data.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header) #writing the header list first to csv file
    writer.writerows(data)
