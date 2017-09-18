'''
Connie Lei & Lisa Eng
SoftDev pd8
Work #03--Files Occupy Space
2017-09-14
'''

# allows us to import and read a file
import csv
import random

# creation of our dictionary
dic = {}

with open('occupations.csv') as csvfile:
    
    rows = csv.reader(csvfile, delimiter = "\n")
    # separating the file with "\n" instead of " " or "," makes it simpler because each
    # occupation and its corresponding percentage are connected together
    # ex. " " creates [["Transportation", "and", "material", "moving,6.5"],["row2"],["row3"]
    # ex. "," creates "'Arts, design, entertainment, sports and media, 1.7' turns into ['Arts"," design"," entertainment"," sports and media','1.7']
   
    # rows are in format [["Transportation and material moving,6.5"],["row2"],["row3"]
    for row in rows:
        # by separating with "\n" means we only need to split it at the last occurrance of "," which is addressed using rsplit(",",1)
        # tempRow is in the format ['Transportation and material moving', '6.5']
        tempRow = row[0].rsplit(',',1)

        # litte annoyance because one of the keys is not a float value
        if(tempRow[1] != "Percentage"):
            # adding keys to the dictionary
            dic[tempRow[0]] = float(tempRow[1])

# creating weighted randomizer







