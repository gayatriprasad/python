# this is the python solution for excercise :

# this is the python solution for excercise :

def readKey(filepath):
	key_dict = {}
	with open(filepath, 'r') as f:
		for line in f:
			items = line.split()
			# print(items)
			key, values = items[0], items[1]
			key_dict[key] = values
	return key_dict

	
print(key = readKey('E:\Sai\key.txt'))

# Function to encrypt the string according to the cipher provided 
def encode(key, message): 
    my_dict = key 
	cipher = '' 
	message = list(message)
    for letter in message: 
        # checks for space 
        if(letter != ' '): 
            # adds the ciphertext corresponding to the  
            # plaintext from the dictionary 
            cipher += my_dict[letter] 
        else: 
            # adds space 
            cipher += ' '
  
    return cipher 
  
# Function to decrypt the string  
# according to the cipher provided 
def decode(key, message, text): 
    my_dict = key
	decipher = '' 
    i = 0
    # emulating a do-while loop 
    while True : 
        # condition to run decryption till  
        # the last set of ciphertext 
        if(i < len(message)-4): 
            # extracting a set of ciphertext 
            # from the message 
            substr = message[i:i + 5] 
            # checking for space as the first  
            # character of the substring 
            if(substr[0] != ' '): 
                ''' 
                This statement gets us the key(plaintext) using the values(ciphertext) 
                Just the reverse of what we were doing in encrypt function 
                '''
                decipher += list(my_dict.keys())[list(my_dict.values()).index(substr)] 
                i += 5 # to get the next set of ciphertext 
            else: 
                # adds space 
                decipher += ' '
                i += 1 # index next to the space 
        else: 
            break # emulating a do-while loop 
  
    return decipher 
	
message = "Geeks for Geeks"

print(encode(key, message))
