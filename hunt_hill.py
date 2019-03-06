# solution to the excercise https://dodona.ugent.be/en/courses/71/series/1321/exercises/1973187951/

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

def allocation(my_dict, seats):
    g_m, a = 1, 0
    if (seats-49 <= 0):
        assert 0, 'too few representatives'
    else:
        new_dict = my_dict.copy()
        new_dict = {x: 1 for x in new_dict}
        seats = seats-50
        while(seats > 0):
            max = 0
            for key, value in my_dict.items():
                g_m = value/math.sqrt(new_dict.get(key)*(new_dict.get(key)+1))
                if (g_m > max):
                    max = g_m
                    state = key
                    
            new_dict[state] = new_dict.get(state) + 1
            seats -= 1 
    return new_dict
     
us2010 = citizens(1990,'us_population.csv') 
# print(us2010)
print(allocation(us2010, 50))
