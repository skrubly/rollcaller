# Data import script
# Provide the name of a csv file as an argument and your data will be imported into the rollcall database
# The CSV should contain three fields:
# Participant ID or group number
# Participant Name
# Day of the week designation
#
# This is tailored towards different workshops that meet during the week coming together at the end of the month to discuss business. So, for example, participant John Sample runs a Monday night workshop and has an ID number of '01'. 

from sys import argv

import csv
import sqlite3

conn = sqlite3.connect('rollcall.db')
c = conn.cursor()

if len(argv) < 2:
    print "Please provide a name of a csv file. ex: python import_csv.py myfile.csv"
    exit(1)
else:
    csvfile = argv[1]

# Initialize the table

c.execute("CREATE TABLE meeting ( id INTEGER PRIMARY KEY, name TEXT, day TEXT, number INTEGER, present INTEGER, notes TEXT )")

meetings = csv.reader(open(csvfile, 'rb'), delimiter=',', quotechar='"')

index = 0
for row in meetings:
    index = index + 1
    print "%s %s" % (index, row)
    c.execute("INSERT INTO meeting VALUES (?, ?, ?, ?, ?, ?)", (index, row[1], row[2], row[0], 0, "No report"))

    
conn.commit()
conn.close()
exit()
