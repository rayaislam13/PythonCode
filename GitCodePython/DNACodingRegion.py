'''
Created on Nov 4, 2014

@author: rayaislam
'''


'''
This code finds characteristics of DNA condon inputs
'''
def findRegion(dna):
    
    startcodon = 'atg'
    stopcodons = [ 'taa', 'tag', 'tga' ]
    answer=""

    i=dna.find(startcodon)  #index of a in atg
    var=i+3
    varon=dna[var:]
    if i==-1:
        return ""

        
    for k in range(0,len(varon),3):
        if varon[k:k+3] in stopcodons:
            return varon[:k]
    return ""
        



