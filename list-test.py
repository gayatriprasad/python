import csv
import math 
import operator

def citizens(year,filepath):
    year = year
    out_dict = {} 
    with open(filepath, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(csv_file)
        lst = [1910,1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]
        if year not in lst:
            assert 0, 'no data available'
        else:
            i = lst.index(year)
            # print(i)
            for row in reader:    
                    out_dict[row[0]] = int(row[i+1])
    return out_dict

us2010 = citizens(1990,'F:\\Learning\\Ghent\\us_population.csv') 
# print(us2010)


def allocation(us2010, seats):
    my_dict = us2010
    my_dict = dict((k,int(v)) for k,v in my_dict.items())
    seats = seats 
    new_dict = my_dict.copy()
    new_dict = {x: 1 for x in new_dict}
    g_m = 1
    g_mean = []
    if (seats-50 <= 0):
        assert 0, 'too few representatives'
    else:
        my_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda x: x[1],reverse=True)} 
        # print(my_dict)
        while(seats-50>0):
            for key,value in my_dict.items():
                # print(key, value)
                n = 1 
                g_m = my_dict.get(key)/math.sqrt(n*(n+1))
                # print(g_m)
                g_mean.append(g_m)
                # print(g_mean)
                for k, v in new_dict.items():
                    a = g_mean.index(max(g_mean))
                    # print(a)
                    k = a
                    new_dict[a] = new_dict.get(a, 0) + 1
                    #print('mno')
            n += 1
            seats -=1 
            
    return new_dict
     
    
print(allocation(us2010, 1024)) 