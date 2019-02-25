# function to return a dictonary with the count for each character

def fill(couple_of_letters):
    my_list = list(str(couple_of_letters).upper())
    my_dict = {}
    for l in my_list:
        if (l.isalpha() or l =='_'):
            if l in my_dict:
                my_dict[l] +=1
            else:
                my_dict[l]= 1
    return my_dict
    
    
def description(bag):
    my_dict1 = bag
    new_dict = {}
    for d_key,d_val in my_dict1.items():
        if d_val in new_dict:          
            new_dict[d_val].append(d_key)
        else:
            new_dict[d_val] = [d_key]

    for k in new_dict:
        new_dict[k] = set(new_dict[k])
    return new_dict


def remove(couple_of_letters, bag_dict):
    bag_dict = bag_dict 
    couple_of_letters_dict = fill(couple_of_letters)
    for d_key, d_val in couple_of_letters_dict.items():
        if d_key in bag_dict and d_val > 0: 
            bag_dict[d_key] -= couple_of_letters_dict[d_key] 
        else:
            assert 0, "not all letters are in the bag" 
    for k, v in list(bag_dict.items()):
        if v == 0 :
            del bag_dict[k]
        elif v < 0:
            assert 0, "not all letters are in the bag"
    return bag_dict  
bag08 = {'T': 2, 'O': 3, 'C': 2, 'Y': 1, 'M': 2, 'R': 2, 'H': 1, 'P': 1, 'E': 1, 'L': 2, 'I': 2, 'A': 1}
# print(remove('ROCTPLYOI', bag08))
bag =     {    'A': 1,    'C': 1,    'E': 1,    'H': 1,    'I': 1,    'L': 1,    'M': 2,    'O': 1,    'R': 1,    'T': 1}
print(remove(['T', 'O', 'L', 'I', 'C', 'T', 'O', 'I', 'H'], bag))