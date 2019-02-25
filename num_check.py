# function to return a customised list 

def serialNumber(num):
    ser_num = str(num)
    assert (num != 0 and ser_num.isdigit() == True and ser_num != '00000000'), 'invalid serial number'
    ser_num = ser_num.zfill(8)
    return ser_num
 
def solid(num):
    ser_num = serialNumber(num)
    for i in range(1, len(ser_num)):
        if ser_num[i] != ser_num[0]: 
            return False
    return True

def radar(num):
    ser_num = serialNumber(num)
    firstpart, secondpart = ser_num[:len(ser_num)//2], ser_num[len(ser_num)//2:]       # split into two strings
    if (firstpart != secondpart[::-1] or solid(num) == True):     # check if they are palindrome
        return False        
    return True

def repeater(num):
    ser_num = serialNumber(num)
    firstpart, secondpart = ser_num[:len(ser_num)//2], ser_num[len(ser_num)//2:]       # split into two strings
    if (firstpart != secondpart or solid(num) == True):     # check if they are repeated
        return False 
    return True

def radarRepeater(num): 
    ser_num = serialNumber(num)
    if (radar(ser_num) == True and repeater(ser_num) == True and solid(ser_num) != True):
        return True
    return False
    
def numismatist(num_list, kind=solid):
    out_list = list()
    kind = kind
    number = list(num_list)
    for i in range(len(number)):
        assert serialNumber(number[i]) != True, 'invalid serial number'
        if kind == radar and radar(number[i]) == True:
            # print('abc')
            out_list.append(number[i])
        elif kind == repeater and repeater(number[i]) == True: 
            # print('def')
            out_list.append(number[i])
        elif kind == radarRepeater and radarRepeater(number[i]) == True: 
            # print('def')
            out_list.append(number[i])
        elif kind(number[i]) == True:
            # print('def')
            out_list.append(number[i])
        elif kind == solid and solid(number[i]) == True:
            # print('ghi')
            out_list.append(number[i])
    return out_list
    
    
print(numismatist(['8781077', 57115233, 32108135, '07298011', '309155', 51251575, '3400', '33434717', 27149035, 97659976, 37966066, 17452690, 94485512, '04', '530', '577', '55', 27426236, '60039', '929'], lambda x : int(x) % 2 == 0))