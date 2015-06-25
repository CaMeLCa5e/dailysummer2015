#! usr/bin/python

filename = "linuxManPages.txt"
newNameList = []

with open(filename) as myfh:
    listOfLines = myfh.readlines()
    newstring = filename.rstrip()

for line in open('linuxManPages.txt'):
    line = line.rstrip()
    line = line.split('(')
    # line = line.split('')
    for item in line:
        print item
        raw_input()
