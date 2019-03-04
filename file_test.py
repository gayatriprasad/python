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

us2010 = citizens(1990, 'us_population.csv') 
print(us2010)
# print(us2010['Alabama'])
# print(us2010['Wyoming'])