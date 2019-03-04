

def readKey(filepath):
    key_dict = {}
    with open(filepath, 'r') as f:
        for line in f:
            items = line.split()
            # print(items)
            key, values = items[0], items[1]
            key_dict[key] = values
    return key_dict
   
key = readKey('E:\Sai\key.txt')


# def encode(key, message, text):
    # my_dict = key
    # cipher, final_text = "", ""
    # message = list(message.upper())
    # if  (5*len(message)) > len(text):
        # print('abc')
        # text = text * int((len(text) / len(message) + 1) 
    # elif (len(text) >= 5*len(message)):
        # text = text 
        # print('def')
    # # part 1 of the encoding : converting to the binary code
    # for letter in message:
        # if(letter != ' '):
            # cipher += my_dict[letter]
        # else:
            # cipher += ' '
    # # part 2 of encoding : converting binary code to string of letters  
    # if text == text:
        # i = 0
        # new_text = text.replace(' ', '').lower()
        # # print(new_text)
        # for i in range(0,len(new_text),5):
            # substr_text = list(new_text[i:i + 5])
            # substr_cip = list(cipher[i:i + 5])
            # if 'b' in substr_cip:
                # for i in range(0,len(substr_cip)):
                    # if substr_cip[i] == 'b':
                        # substr_text[i] = substr_text[i].upper()
                        
            # else:
                # pass
            # final_text += ''.join(substr_text)
    
    # elif text == None:
        # i = 0
        # new_text = ''.join(random.choices(string.ascii_lowercase, k=len(message)*5))
        # # print(new_text)
        # for i in range(0,len(new_text),5):
            # substr_text = list(new_text[i:i + 5])
            # substr_cip = list(cipher[i:i + 5])
            # if 'b' in substr_cip:
                # for i in range(0,len(substr_cip)):
                    # if substr_cip[i] == 'b':
                        # substr_text[i] = substr_text[i].upper()
                        
            # else:
                # pass
            # final_text += ''.join(substr_text)
    
    # return str(final_text) 
        
# print(encode(key, 'ALICE', 'ora et labora'))


def decode(key, text): 
    decipher, final = '' , ''
    text = text
    my_dict = key
    # print(my_dict.keys())
    # print(my_dict.values())
    substr_cip = ['a'] * len(text)
    # print(substr_cip)
    # part 1 of decoding 
    for i in range (0, len(text),5):
        substr_text = list(text[i:i + 5]) 
        # print(substr_text)
        for j in range (0, len(substr_text)):
            if substr_text[j].isupper() == True:
                substr_cip[j] = 'b'
                print(substr_cip) 
            else:
                pass
            
    final += ''.join(substr_cip)
    print('final:',final)
    for k in range (0, len(final),5):
        substr = final[k:k + 5] 
        for key, value in my_dict.items():
            if substr == value:
                decipher += my_dict[value]
    
    print('decipher:',decipher)            
    
    return decipher  

print(decode(key, 'dracodOrMIeNsnumquAmtiTil'))