'''
Created on Nov 19, 2014

@author: rayaislam
'''

'''
You are writing software to help someone understand their very complicated family. 
Your task is to determine all aunts and uncles of a given person. An aunt or uncle of a person is defined 
as a sibling of that person's parent. Two people are siblings if they have one or more parents in common.
'''
def aulist(parents,target):
    
        plist=[]
        for name in parents:
            namelist=name.split()
            if target == namelist[2]:    #get mom and dad
                plist.append(namelist[0])
                plist.append(namelist[1])
        if len(plist)==0:
            return []
        
        pset=set(plist)
    
        glist=[]
        for name in parents:
            namelist2=name.split()
            if plist[0] == namelist2[2]:
                glist.append(namelist2[0])
                glist.append(namelist2[1])
            if plist[1] == namelist2[2]:
                glist.append(namelist2[0])
                glist.append(namelist2[1])
        #print sorted(glist)        
                
        aulist2=[]
        
        for name in parents:
            namelist3=name.split()
            for gp in glist:
                if gp in namelist3[:2]:
                    aulist2.append(namelist3[2])
        
                            
        auset=set(aulist2)
        
        ans=sorted(list(auset-pset))
        
        for ch in ans:
            if ch==target:
                ans.remove(target)
            
        return ans


print aulist(['A B C', 'B C D', 'D E F', 'E F G', 'F G H', 'G H I', 
              'H J K', 'A C M', 'B D N', 'A B P', 'D C T', 'M K W', 'X C Z'], 'A')

        