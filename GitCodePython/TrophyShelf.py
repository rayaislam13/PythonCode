'''
Created on Oct 21, 2014

@author: rayaislam
'''

'''
You have several trophies sitting on a shelf in a straight line. Their heights are given in a list 
of int values, trophies, from left to right. The shelf is positioned so that whenever people enter 
your room, they see it directly from the left side. In other words, the leftmost trophy is completely 
visible to the viewer, the next trophy in line is directly behind it, and so on.
Unfortunately, tall trophies near the left side of the shelf might block the view of other trophies. 
A trophy is visible only if every trophy in front of it (from the viewer's perspective) is strictly 
shorter than it is. You wonder if rotating the shelf 180 degrees would increase the number of visible trophies.

Return a int list containing exactly two elements. The first element should be the number of trophies 
visible when viewing the shelf directly from the left side, and the second element should be the number 
of trophies visible when viewing the shelf directly from the right side.
'''

#count until nextone is shorter than the one before it
#return tally,max?
#count from one side
#count from another side

def countVisible(trophies):
    lefthigh=0
    righthigh=0
    count=0
    count2=0
    for i in trophies:
        if i > righthigh:
            count+=1
            righthigh=i
    
    backtrophies=reversed(trophies)
    for j in backtrophies:
        if j > lefthigh:
            count2+=1
            lefthigh=j
            
    return[count,count2]
    