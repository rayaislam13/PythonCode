'''
Created on Sep 17, 2013

@author: rqi
'''
'''
This is the link to the assignment:
https://www.cs.duke.edu/courses/compsci101/fall14/assign/assign6/
'''
# use these variables to make your code more readable
START_CODON = 'atg'
STOP_CODONS = [ 'taa', 'tag', 'tga' ]
# these next two lists are meant to be used together,

CODONS = [
  'gct', 'gcc', 'gca', 'gcg',
  'tgt', 'tgc', 
  'gat', 'gac',
  'gaa', 'gag', 
  'ttt', 'ttc', 
  'ggt', 'ggc', 'gga', 'ggg',
  'cat', 'cac',
  'att', 'atc', 'ata',
  'aaa', 'aag',
  'ctt', 'ctc', 'cta', 'ctg', 'tta', 'ttg',
  'atg',
  'aat', 'aac',
  'cct', 'ccc', 'cca', 'ccg',
  'caa', 'cag',
  'cgt', 'cgc', 'cga', 'cgg', 'aga', 'agg',
  'agt', 'agc', 'tct', 'tcc', 'tca', 'tcg', 
  'act', 'acc', 'aca', 'acg',
  'gtt', 'gtc', 'gta', 'gtg',
  'tgg',
  'tat', 'tac',
]
AMINO_ACIDS = [ 
  'A', 'A', 'A', 'A', 
  'C', 'C',
  'D', 'D', 
  'E', 'E', 
  'F', 'F',
  'G', 'G', 'G', 'G',
  'H', 'H',
  'I', 'I', 'I',
  'K', 'K', 
  'L', 'L', 'L', 'L', 'L', 'L',
  'M', 
  'N', 'N', 
  'P', 'P', 'P', 'P',
  'Q', 'Q',
  'R', 'R', 'R', 'R', 'R', 'R',
  'S', 'S',  'S', 'S', 'S', 'S',
  'T', 'T', 'T', 'T', 
  'V', 'V', 'V', 'V', 
  'W',
  'Y', 'Y', 
]

#put dna coding region here
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


def codontoamino(dna):
    colist=[]
    for i in range(0,len(dna),3):
        match=dna[i:i+3]
        ind=CODONS.index(match)  #index where matches
        colist.append(AMINO_ACIDS[ind])
    return "".join(colist)

def prottoamino(dna):
    substring=findRegion(dna)
    if substring=="":
        return ""
    return codontoamino(substring)
    
    
def reversecomp(dna):
    complement=""
    for let in dna:
        if let=='a':
            complement+='t'
        if let=='g':
            complement+='c'  
        if let=='t':
           complement+='a'
        if let=='c':
            complement+='g'
    return complement[::-1]

 
    
    


 


def translateDNAtoProtein (dna):
    """
    given a string composed only of lowercase letters 'gcta', 
    return a string of uppercase letters that represents the 
    longest protein found first within that string or its 
    reverse complement, or the empty string if no protein can
    be found
    """
  
    revlist=reversecomp(dna)
    if len(prottoamino(dna)) > len(prottoamino(revlist)):
        return prottoamino(dna)
    else:
        return prottoamino(revlist)
    


