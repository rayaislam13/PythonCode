'''
Created on Nov 11, 2014

@author: rayaislam
'''
'''
You will be given a string list names, containing a list of customer names extracted from a database. 
Your task is to report the customers that occur more than once in this list, and the number of 
occurrences for each of the repeated customers.
'''
def reportDuplicates(names):
    d={}
    ans=[]
    anslst=[]
    for person in names:
        keys=person
        print keys
        if keys not in d:
            d[keys]=0
        d[keys] += 1
    

    for i in d:
        lol=d.get(i)
        ans.append((i,lol))
        ans=sorted(ans)
        #anslst=''.join(t for t in ans)
        if lol >1:
            anslst.append(str(i+ " "+ str(lol)))
    return sorted(anslst)

        
    



print reportDuplicates(["YETTI", "YETTI", "YETTI", "BIGFOOT", "BIGFOOT"])
        