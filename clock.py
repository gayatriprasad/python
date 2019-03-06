# Solution to the exercise https://dodona.ugent.be/en/courses/71/series/1323/exercises/204555018/


class Clock:
    
    
    # init method or constructor  
    def __init__(self, hours=0, minutes=0, seconds=0): 
        self.hours = hours 
        self.minutes = minutes
        self.seconds = seconds
    
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hours, self.minutes, self.seconds) 
    
    def __repr__(self):
        return 'Clock(%r, %r, %r)' % (self.hours, self.minutes, self.seconds)
        
    # hours, minutes seconds.setter
    def set(self, hours=0, minutes=0, seconds=0):
        self.hours = hours 
        self.minutes = minutes
        self.seconds = seconds
    
    def forward(self, hours=0, minutes=0, seconds=0):
        m = (self.hours + hours)*60 + self.minutes + minutes
        s = m * 60 + self.seconds + seconds
        minutes, clock.seconds = divmod(s, 60)
        clock.hours, clock.minutes = divmod(minutes, 60)
        if (clock.hours > 23):
            clock.hours = clock.hours % 24
        
clock = Clock(9, 33, 41)
# print(clock)
clock.set(minutes=19, seconds=18, hours=12)

clock1 = Clock(minutes=11)
clock2 = Clock(hours=15, minutes=17)
print(clock1)
print(clock2)

clock1.forward(hours=9)
clock2.forward(hours=5, minutes=30)

print(clock1)
print(clock2)