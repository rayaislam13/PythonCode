'''
Created on Oct 22, 2014

@author: rayaislam
'''
'''
You just bought a very delicious chocolate bar from a local store. This chocolate bar consists of N squares, 
numbered 0 through N-1. All the squares are arranged in a single row. There is a letter carved on each square. 
You are given a string parameter letters. The i-th character of letters denotes the letter carved on the i-th 
square (both indices are 0-based).


Return the maximum possible length of the remaining chocolate bar that contains no repeated letters.
'''
    
def maxLength(letters):
    biggest=0
    for itr in range(0,len(letters)):
        str=""
        for ind in range(itr,len(letters)): 
            if letters[ind] not in str:
                str+=letters[ind]     
                if len(str)>biggest:
                    biggest=len(str)
                else:
                    biggest=biggest
            else: 
                break
    return biggest
                    
            