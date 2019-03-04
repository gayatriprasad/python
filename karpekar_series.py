# The following is the python code for the following question 

# Question: https://dodona.ugent.be/en/courses/71/series/999/exercises/558415663/

def Karpekar(num):
    karpekar_num = num
    ascend = int("".join(sorted(str(karpekar_num), reverse=False)))
    descend = int("".join(sorted(str(karpekar_num), reverse=True)))
    diff = descend - ascend
    return diff

def kaprekarSeries(num):
    number = num
    out_list = [number]
    for number in out_list:
        if(Karpekar(number) in out_list):
            pass
        else:
            if number != 0:
                kar_num = Karpekar(number)
                new_kar_num = kar_num
                out_list.append(new_kar_num)
                        
    return out_list

