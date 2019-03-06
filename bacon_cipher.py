# Solution to excercise https://dodona.ugent.be/en/courses/71/series/1322/exercises/1499330773/

import random, string

def readKey(filepath):
    key_dict = {}
    with open(filepath, 'r') as f:
        for line in f:
            items = line.split()
            # print(items)
            key, values = items[0], items[1]
            key_dict[key] = values
    return key_dict
   
key01 = readKey('key01.txt')

def encode(key, message, text=None):
    my_dict = key
    cipher, final_text = '', ''
    message = ''.join(e for e in message if e.isalnum())
    message = list(message.upper())
    if text == None:
        pass
    else:
        new_text = ''.join(e for e in text if e.isalnum())
        new_text = new_text.lower()
        if (len(message)*5) > len(new_text):
            new_text = (new_text * (int((len(message)*5)/len(new_text))+1))[:(len(message)*5)]
    # part 1 of the encoding : converting to the binary code
    for i in message:
        if i != '':
            cipher += my_dict[i]
        else: 
            pass
    
    # part 2 of encoding : converting binary code to string of letters  
    
    if text != None and text.isdigit() != True: 
        i = 0
        for i in range(0,len(new_text),5):
            substr_text = list(new_text[i:i + 5])
            substr_cip = list(cipher[i:i + 5])
            if 'b' in substr_cip:
                for j in range(0,len(substr_cip)):
                    if substr_cip[j] == 'b':
                        substr_text[j] = substr_text[j].upper()
                        
            else:
                pass
            final_text += ''.join(substr_text)
    
    elif text == None or text.isdigit() == True:
        i = 0
        new_text = ''.join(random.choices(string.ascii_lowercase, k=len(message)*5))
        for i in range(0,len(new_text),5):
            substr_text = list(new_text[i:i + 5])
            substr_cip = list(cipher[i:i + 5])
            if 'b' in substr_cip:
                for i in range(0,len(substr_cip)):
                    if substr_cip[i] == 'b':
                        substr_text[i] = substr_text[i].upper()
                        
            else:
                pass
            final_text += ''.join(substr_text)
    
    return final_text[:len(message)*5]
    
def decode(key, text): 
    decipher, final = '' , ''
    my_dict = key
    decip = ['a'] * len(text)

    # part 1 of decoding  : converting to binary code 
    
    for i in range (0, len(text),5):
        substr_text = list(text[i:i + 5]) 
        substr_dcip = list(decip[i:i + 5])
        for j in range (0, len(substr_text)):
            if substr_text[j].isupper() == True:
                substr_dcip[j] = 'b'

        final += ''.join(substr_dcip)

    for k in range (0, len(final),5):
        substr = final[k:k + 5] 
        for key, value in my_dict.items():
            if value == substr:
               decipher += key
            
    return decipher 


print(encode(key01, 'ALICE', '0123456789'))

