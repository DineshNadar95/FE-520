#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Notice: do not change these function name 
class MovingAverage:

    # count  = 0;

    def __init__(self, size):
        """
        Initialize your data structure here.
        """
        self.size = size;
        self.arr = [0]*size;
        self.count = 0
        
    
    def next(self, val):
        # add your code here 
        self.count  = self.count + 1
        self.arr.pop(0)
        self.arr.append(val)
        if(self.count <= self.size):
            return(sum(self.arr)/self.count) 
        else:
            return(sum(self.arr)/self.size)
        
    
    
    
class subway:

    def __init__(self):
        self.checkIns = {}
        self.checkOuts = {}
        
        
    def checkIn(self, id, stationName, t):
        # add your code here    
        self.checkIns[id] = [stationName,t]

    
    def checkOut(self, id, stationName, t):
        # add your code here 
        startEnd = self.checkIns[id][0]+ "-" + stationName
        if startEnd not in self.checkOuts:
            self.checkOuts[startEnd] = [t-self.checkIns[id][1]]
        else:
            self.checkOuts[startEnd].append(t-self.checkIns[id][1])
            
    def getAverageTime(self, startStation, endStation):
        # add your code here 
        startEnd =  startStation + "-" + endStation
        return sum(self.checkOuts[startEnd])/len(self.checkOuts[startEnd])

    

class Linear_regression:

    def __init__(self, x, y, m, c, epochs, L):
       self.x = x
       self.y = y
       self.m = m
       self.c = c
       self.epochs = epochs
       self.L = L
        
        
    def gradient_descent(self) :
        for a in range(self.epochs):
            Dm=[]
            Dc=[]
            for i in range(len(self.x)):
                ypredi = (self.x[i][0] *self.m) + self.c
                Dm.append(self.x[i][0]*(ypredi-self.y[i]))
                Dc.append(ypredi-self.y[i])
            dm = sum(Dm)/len(Dm)
            dc = sum(Dc)/len(Dc)
            self.m = self.m - self.L * dm
            self.c = self.c - self.L * dc
        return(self.m,self.c)
    
    def predict(self,x_new):
       # add your code here 
        arr = []   
        for i in (x_new):
            ypredi = (i *self.m) + self.c
            arr.append(ypredi)
        return(arr)

    
    
class LCG:

    def __init__(self, seed, multiplier, increment, modulus):  
        # add your code here    
        pass
        
    def get_seed(self):   
        # add your code here    
        pass
         
    def set_seed(self,new_seed):   
        # add your code here    
        pass
    
    def initialize(self):
       # add your code here    
        pass
    
    def gen(self):
        # add your code here    
        pass
        
    def seq(self, num):  
        # add your code here    
        pass

#


if __name__ == "__main__":  

    x = [[0.18], [1.0], [0.92], [0.07], [0.85], [0.99], [0.87]]
    y = [109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77]
    x_new = [0.9,0.8,0.40,0.7]

    
    # Test Question 1
    print("\nQ1")    
    windowsize = 3 
    moving_average = MovingAverage(windowsize)
    step1 = moving_average.next(1)  
    print("my answer: ", step1)    
    print("right answer: 1.0")    
    print("--------------")
    step2 = moving_average.next(10) 
    print("my answer: ", step2)    
    print("right answer: 5.5")    
    print("--------------")  
    step3 = moving_average.next(3) 
    print("my answer: ", step3)    
    print("right answer: 4.66667")    
    print("--------------") 
    step4 = moving_average.next(5) 
    print("my answer: ", step4)    
    print("right answer: 6.0")    
    print("--------------") 
    
    
    
    
    # Test Question 2
    print("\nQ2") 
    s = subway()
    s.checkIn(10,'Leyton',3)
    s.checkOut(10,'Paradise',8)
    print("my answer: ",s.getAverageTime('Leyton','Paradise'))
    print("right answer: 5.0")    
    print("--------------") 
    s.checkIn(10,'Leyton',10)
    s.checkOut(10,'Paradise',16)
    print("my answer: ",s.getAverageTime('Leyton','Paradise'))
    print("right answer: 5.5")    
    print("--------------") 
    s.checkIn(10,'Leyton',21)
    s.checkOut(10,'Paradise',30)
    print("my answer: ",s.getAverageTime('Leyton','Paradise'))
    print("right answer: 6.667")    
    print("--------------") 
    
    
    # Test Question 3
    print("\nQ3") 
    Linear_model = Linear_regression(x,y,0,0,500,0.001)
    print("I use m=0, c=0, epochs=500, L=0.001")
    print("my m and c: ",Linear_model.gradient_descent())
    print("right m and c:(35.97890301691016, 46.54235227399102)")    
    print("--------------") 
    print("my predict: ", Linear_model.predict(x_new))
    print(" right predict: [78.92336498921017, 75.32547468751915, 60.93391348075509, 71.72758438582812]")
    
    
    # Bonus Question 
    print("\nBonus") 
    print("set seed = 1, multiplier = 1103515245, increment = 12345, modulus = 2**32")
    lcg = LCG(1,1103515245,12345, 2**32 )
    print("my seed is: ", lcg.get_seed())
    print("right seed is: 1")
    print("the seed is setted with: ", lcg.set_seed(5))
    print("right seed is setted with 5")
    print("the LCG is initialized with seed: ",lcg.initialize())
    print("the LCG is initialized with seed 5")
    print("the next random number is: ", lcg.gen())
    print("right next random number is: 0.2846636981703341")
    print("the first ten sequence is: ", lcg.seq(10))
    print("the first ten sequence is: ", [0.6290451611857861, 0.16200014390051365, 0.4864134492818266, 0.655532845761627, 0.8961918593849987, 0.2762452410534024, 0.8611323081422597, 0.9970241007395089, 0.798466683132574, 0.46138259768486023])


