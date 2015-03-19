'''
Created on Sep 22, 2014

@author: rayaislam
'''
'''
This code turns strings into pig latin
'''

def convert(s):
    vowel="a e i o u A E I O U"
    if s.startswith("qu"): 
        return s[2:]+"-qu"+"ay"
    for letter in vowel:
        if s.startswith(letter):
            return s+"-way"
    #save index of where vowel is 
    for let in s:
        if let in vowel:
            word=s.index(let)
            return s[word:] +"-" + s[:word] + "ay" 



