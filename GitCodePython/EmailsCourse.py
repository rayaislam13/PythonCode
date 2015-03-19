'''
Created on Nov 10, 2014

@author: rayaislam
'''

'''
You are given a list of strings of course information, where each string is in the format 
"coursename:person:email". Your task is to determine the course with the most people and 
to return the emails of those people in the largest course. The emails should be returned 
as a string with the emails in alphabetical order. If there is more than one largest course, 
return the emails of such course that comes first in alphabetical order.

'''

from operator import itemgetter

def emailsLargest(courses):
    d={}
    for item in courses:
        itemlist=item.split(':')
        keys=itemlist[0]
        values=itemlist[2]
        if keys not in d:
            d[keys]=[]
        d[keys].append(values)
        
    
    
    lst = []
    for i in d:
        subject = i
        email=d.get(i)
        subsize = len(email)
        lst.append((subject,email,subsize))
    
    dsort1=sorted(lst, key = itemgetter(0), reverse = False) 

    dsort2=sorted(dsort1, key = itemgetter(2), reverse = True) #priority should be last

    
    answer= sorted(dsort2[0][1])
    stringans=' '.join(answer)
    return stringans
    
    
    
    

    
    
    
    
print emailsLargest(["CompSci 100:Fred Jack Smith:fjs@duke.edu", 
  "History 117:Fred Jack Smith:fjs@duke.edu", 
  "CompSci 102:Arielle Marie Johnson:amj@duke.edu", 
  "CompSci 100:Arielle Marie Johnson:amj@duke.edu", 
  "CompSci 006:Bertha White:bw@duke.edu",
  "Econ 051:Bertha White:bw@duke.edu", 
  "English 112:Harry Potter:hp@duke.edu",
  "CompSci 100:Harry Potter:hp@duke.edu"])