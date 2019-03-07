# solution to the excercise https://dodona.ugent.be/en/courses/71/series/1323/exercises/1394034677/

import csv
import math 

class Census:

    import csv 
    # init method or constructor  
    def __init__(self, year, filepath): 
        self.year = year
        self.filepath = filepath
        self.dic = {}
        with open(self.filepath, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            next(csv_file)
            lst = [1910,1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]
            if self.year not in lst:
                assert 0, 'no data available'
            else:
                i = lst.index(self.year)
                # print('index:', i)
                for row in reader:    
                    self.dic[row[0]] = int(row[i+1])
    
    def citizens(self, region):
        self.region = region
        # print(self.region)
        if self.region not in self.dic.keys():
            assert 0, 'no data available'
        return self.dic[self.region]
    
    def allocation(self, seats):
        self.seats = seats 
        if (seats-49 <= 0):
            assert 0, 'too few representatives'
        else:
            new_dic = self.dic.copy()
            new_dic = {x: 1 for x in new_dic}
            seats = seats-50
            while(seats > 0):
                max, g_m = 0, 1
                for key, value in self.dic.items():
                    g_m = value/math.sqrt(new_dic.get(key)*(new_dic.get(key)+1))
                    if (g_m > max):
                        max = g_m
                        state = key
                new_dic[state] = new_dic.get(state) + 1
                seats -= 1 
        return new_dic
        
us2000 = Census(2000, 'us_population.csv')       
# print(us2000)
print(us2000.citizens('Wyoming'))
# print(us2010.allocation(1024))