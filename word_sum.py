# function to check the word sums work 

import string 

def letter_value(ch):
    new = ord(ch)
    if 65 <= new <= 90:     # Upper case letter
        return (new - 64)
    elif 97 <= new <= 122:  # Lower case letter
        return (new - 96)
    else:                    # Unrecognized character
        return 0

    return

    
def word_value(string):
    word = list(string)
    sum = 0
    for i in word:
        sum += letter_value(i)
    return sum

    
def word_sum(first, second, third):
    word1 = list(first)
    word2 = list(second)
    word3 = list(third)
    sum1 = 0
    sum2 = 0
    sum3 = 0 
    for i in word1:
        sum1 += letter_value(i)
    for j in word2:
        sum2 += letter_value(j)
    for k in word3:
        sum3 += letter_value(k)
    
    if (sum3 == (sum1+sum2)):
        return True
    return False
    
#print(word_sum('arm', 'BEND', 'elbow'))    
    
    