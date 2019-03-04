# Function to read a file and return a dictionary 

def readKey(filepath):
	key_dict = {}
	with open(filepath, 'r') as f:
		for line in f:
			items = line.split()
			# print(items)
			key, values = items[0], items[1]
			key_dict[key] = values
	return key_dict
	
key = readKey('F:\Learning\Ghent\key.txt')
print(key)
# Function to encrypt the string according to the cipher provided 

def encode(key, message, text=None): 
    my_dict = key 
    cipher = ""
    message = list(message)
    # print(message)
    # print (my_dict)
    # part 1 of the encoding : converting to the binary code 
    if text == None:
        for letter in message: 
            if(letter != ' '): 
                cipher += my_dict[letter] 
            else: 
                cipher += ' '
    # part 2 of encoding : converting binary code to string of letters
    else:
        i, j = 0, 0
        text = text.replace(' ', '')
        for letter in text:
            if(i < len(text)-4): 
                substr_text = text[i:i + 5]
                substr_cip = cipher[i:i + 5]
                # print('abc')
                for j in substr_cip:    
                    if(substr_cip[j] == 'b'):
                        substr_text[j] = substr_text[j].upper()
                    
    print()    
    return 0 
  
# Function to decrypt the string according to the cipher provided 

# def decode(key, message, text=None): 
    # my_dict = key
	# decipher = '' 
    # i = 0
    # while True : 
        # if(i < len(message)-4): 
            # substr = message[i:i + 5] 
            # if(substr[0] != ' '): 
                # decipher += list(my_dict.keys())[list(my_dict.values()).index(substr)] 
                # i += 5  
            # else: 
                # decipher += ' '
                # i += 1  
                # break
    # return decipher 
    
    
print(encode(key, 'ALICE', 'Draco Dormiens Numquam Titillandus'))
