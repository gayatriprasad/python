# solution to the excercise https://dodona.ugent.be/en/courses/71/series/1323/exercises/1394034677/


class Census:

        
    # init method or constructor  
    def __init__(self, year, filepath): 
        self.year = year
        self.filepath = filepath
        self.dic = {}
        with open(self.filepath, 'r') as csv_file:
        self.reader = csv.reader(csv_file, delimiter=',')
        next(csv_file)
        self.lst = [1910,1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]
        if year not in self.lst:
            assert 0, 'no data available'
        else:
            i = self.lst.index(year)
            # print(i)
            for row in reader:    
                    self.dic[row[0]] = int(row[i+1])
    
    def citizens(self, region):
        self.region = region 
        