class TrafficLight: 
  
    # init method or constructor  
    def __init__(self, col='red'): 
        self.col = col 
  
    def __str__(self):
        return ('%s') % self.col
    
    def __repr__(self):
        return "TrafficLight(%r)" % self.col
            
    def next(self):
        # next_col = ''
        # print('p', next_col)
        if self.col == 'red':
            self.col = 'green'
        elif self.col == 'orange':
            self.col = 'red'
        elif self.col == 'green':
            self.col = 'orange'
        # print('r', next_col)


light1 = TrafficLight() 
print(light1)
light2 = TrafficLight('green')
print(light1, light2)
light1.next()
print(light1, light2)

light1.next()
light1.next()
light2.next()
print(light1, light2)




