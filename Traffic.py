# Class practise 

class TrafficLight: 
  
    # init method or constructor  
    def __init__(self, col='red'): 
        self.col = col 
  
    def __str__(self):
        return self.col
    
    def __repr__(self):
        return "TrafficLight" % (self.col)
            
    def next(self):
        next_col = ''
        # print('p', next_col)
        if self.col == 'red':
            next_col = 'green'
        elif self.col == 'orange':
            next_col = 'red'
        elif self.col == 'green':
            next_col = 'orange'
        # print('r', next_col)
        return next_col

light1 = TrafficLight() 
print(light1)
light2 = TrafficLight('green')
print(light1, light2)
light1.next()
print(light1, light2)