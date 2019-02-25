# Function to check if a part of the DNA sequence is a palindrome 

alt_map = {'org':'inv'}
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

def reverseComplement(seq):
    
    bases = list(seq)       # convert sequence to list 
    bases = reversed([complement.get(base,base) for base in bases])     # reverse the list 
    bases = ''.join(bases)      # concatenate the string with empty separators 
    for k,v in alt_map.items():
       bases = bases.replace(v,k)
    return bases
   
def reversePalindrome(seq): 
    rev_seq = reverseComplement(seq)       
  
    if (seq == rev_seq): 
        return True
    return False

def restrictionSites(seq, minLength = 4, maxLength = 12):
    sites = []
    seq = str(seq)
    dna = seq.zfill(len(seq)+1)
    min_length = minLength
    max_length = maxLength
    left, right = 1, len(dna)
    j = right
    while left < right-1:
        temp = dna[left:j] 
        if reversePalindrome(temp) == True and len(temp) >= min_length and len(temp) <= max_length:
            sites.append((left, temp))
        j -= 1
        if j < left + 2:
            left += 1
            j = right
    sites = sorted(sites, key=lambda x: (x[0], len(x[1])))
    return sites 
    
# print(restrictionSites('TCAATGCATGCGGGTCTATATGCAT'))    
# print(restrictionSites('AAGTCATAGCTATCGATCAGATCAC'))
print(restrictionSites('CTGCCTCCAATTAATTGGAGGACCATTATAGACGAAAGGGCGGTG', minLength=2, maxLength=5))    
