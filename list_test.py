

my_list = [33333333, 1133110, '77777777', '12211221']

def serialNumber(num):
    ser_num = str(num)
    assert (num != 0 and ser_num.isdigit() == True and ser_num != '00000000'), 'invalid serial number'
    ser_num = ser_num.zfill(8)
    return ser_num

for i in range(len(my_list)):
    print(i)
    print(my_list[i])
    print(serialNumber(my_list[i]) != True)


    
    
lambda x : set(str(x)) <= {'0', '1', '2'}