'''
Created on Oct 28, 2014

@author: rayaislam
'''
'''
This code plays hangman from a provided list of words in a data files
'''

import random


def process_letter(guessed,secret,letter):    #secret is word guessing 
    for ch in range(0,len(secret)):
        if secret[ch]==letter:
            guessed[ch]=letter
    return guessed


def load_lines(filename):
    """
    read words from specified file and return a list of
    strings, each string is one line of the file
    """
    lines = []
    f = open(filename)
    for line in f.readlines():
        line = line.strip()
        lines.append(line)
    return lines
    
    
def get_words(filename, wordlength = 5):
    """
    returns a list of words having a specified length from
    the file whose name is filename.
    default length is 5 (if parameter not specified)
    """
    lines = load_lines(filename)
    wlist = [w for w in lines if len(w) == wordlength]
    return wlist

def user():
    print "what's the word length?>",
    n = int(raw_input())
    words = get_words("lowerwords.txt",n)
    print "read %d words whose length is %d" % (len(words),n)
    one = random.choice(words)
    #print "choosing at random>",one
    if len(words) < 30:
        for i,w in enumerate(words):
            print i,"\t",w
    return one

def hangman(secret):
    print "How many guesses would you like?"
    numguess = int(raw_input())
    guessline= " "
    guessed = ["_"]*len(secret)
    while numguess > 0:
        print "What letter do you want to guess:"
        let=raw_input() #input letter and put in terms of prolet
        prolet=process_letter(guessed,secret,let)  #deals with specific letter
        guessed=prolet
        print guessed
        if str(numguess) not in secret:  #account for misses left line
            print "misses left: " + str(numguess-1)
        else: 
            print "misses left: " + str(numguess)
        
        #adding to guesses so far list    
        guessline+=let
        print "Guesses so far" + guessline
        
        #if letter guessed not in secret word
        if let not in secret:
            print "no   " + str(let)
            
    #if you don't finish get outside while looping
    
    if ''.join(guessed)!=secret:
        print "You are hung. Your word is" + secret
        
        


if __name__ == "__main__":
    secret=user()
    hangman(secret)
    
    
#dictionary a for loop 


