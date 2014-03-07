"""
wordlength | bestletter
         1 | 0
         2 | 1
         3 | 1
         4 | 1
         5 | 1
         6 | 2
         7 | 2
         8 | 2
         9 | 2
        10 | 3
        11 | 3
        12 | 3
        13 | 3
       >13 | 4
"""
import os
import time
import sys
f = open("test.txt", 'r');
for line in f:
    words = line.split()
    for word in words:
        os.system('clear')
        wpm = 250
        print "-----|---------"
        if len(word) == 1:
            print "     " + word
        if len(word) >= 2 and len(word) < 6:
            print "    " + word
        if len(word) >= 6 and len(word) < 10:
            print "   " + word
        if len(word) >= 10 and len(word) < 14:
            print "  " + word
        if len(word) > 13:
            print " " + word
        print "-----|---------"
        if len(word) <= 5:
            wpm *= 1.1
        if len(word) > 5:
            wpm *= 0.9
        if "." in word:
            wpm *= 1.2
        if "," in word:
            wpm *= 1.1
        wpm = 60 / wpm
        time.sleep(wpm)
        
