import os
import time
import sys
f = open("test.txt", 'r');
for line in f:
    words = line.split()
    for word in words:
        try:
            os.system('clear')
        except:
            os.system('cls')
        wpm = int(sys.argv[1])
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
            wpm *= 1.5
        if len(word) > 5:
            wpm *= 0.5
        if "." in word:
            wpm *= 1.8
        if "," in word:
            wpm *= 1.5
        wpm = 60 / wpm
        time.sleep(wpm)
        
