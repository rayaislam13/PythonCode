'''
Created on Nov 10, 2014

@author: rayaislam
'''
'''
You are given several donors and the amount of their charity donations. 
A donor may give more than one time. Your task is to figure out the name of the 
donor who has given the largest total amount to charity. If there is more than one donor 
with the largest amount, return the name that comes first in alphabetical order
'''


from operator import itemgetter

def nameDonor(contributions):

    d={}
    answer=[]
    for item in contributions:
        itemlist=item.split(':')
        keys=itemlist[0]  #list
        values=itemlist[1]
        if keys not in d:
            d[keys]= 0
        d[keys] += float(values)
        #dictionary above
            
    lst = []
    for i in d:
        name = i
        number = d.get(i)
        lst.append((name, number))
    
    
    dsort1=sorted(lst, key = itemgetter(0), reverse = False) 
    dsort2=sorted(dsort1, key = itemgetter(1), reverse = True) #priority should be last
    
    print dsort2
    
    return dsort2[0][0]
       
        
print nameDonor(['Sun:70.00', 'Blue:60.00', 'Zebra:80.00', 'Edwards:80.00'])