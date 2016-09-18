#!/usr/bin/env python3
#! python
import os, sys
 
def wc(infile):
 
    """Count lines, words and characters in a file"""
 
    a = b = c = 0 #lines, words, characters
 
    for line in infile: 
        a += 1
        for word in line.split(' '):
            b += 1
            for char in word:
                c += 1
         
    return a, b, c 

def getfiles():

    files = []

    curDir = os.getcwd()
    for (param1, param2, param3) in os.walk(curDir):
        files.append(param3)
    return files[0]


if __name__ == '__main__':

    cmd = sys.argv[1]        
    if cmd == '*':
        file_list = getfiles()
        for f in file_list:
            count = wc(open(f, 'r'))
            print (count[0], count[1], count[2], f)

    elif cmd == '*.py':
        file_list = getfiles()
        for f in file_list:
            if f.endswith(".py"):
                count = wc(open(f, 'r'))
                print (count[0], count[1], count[2], f)

    else: 
        count = wc(open(cmd, 'r'))
        print (count[0], count[1], count[2], cmd)
    