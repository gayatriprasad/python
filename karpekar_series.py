# print(kaprekarSeries(6152402648604)) 
# function: 
# 1. Take the number 
# 2. Store the number as num
# 3. Calculate the largest possible number with the digits 
# 4. Calculate the largest possible number with the digits
# 5. Calculate the difference
# 6. Return the difference as new number 
 
# 1. Take a number as input 
# 2. Create a new list
# 3. Store the number in the list 
# 4. For every new number in the list (exit if the number exists)  call the function declared 
# 5. Append the number returned by the function to the list 
# 6. Print the list and check


def Karpekar(num):
    karpekar_num = num
    # print(karpekar_num)
    ascend = int("".join(sorted(str(karpekar_num), reverse=False)))
    # print(ascend)
    descend = int("".join(sorted(str(karpekar_num), reverse=True)))
    # print(descend)
    diff = descend - ascend
    # print(diff)
    return diff

def kaprekarSeries(num):
    number = num
    # print(number)
    out_list = [number]
    # out_list.append(Karpekar(number))
    # print(out_list)
    for number in out_list:
        if(Karpekar(number) in out_list):
            pass
            # print('def')
        else:
            if number != 0:
                kar_num = Karpekar(number)
                # print('abc')
                new_kar_num = kar_num
                # print(new_kar_num)
                out_list.append(new_kar_num)
            # print(out_list) 
                        
    return out_list


# print(Karpekar(646732000455316678))
print(kaprekarSeries(646732000455316678))    
