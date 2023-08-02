class Car: 
    __rate = 12 
    def __init__(self, gas_amount): 
        self.__gas_amount = gas_amount 
 
    @property 
    def rate(self): 
        return self.__rate 
     
    @rate.setter 
    def rate(self, rate): 
        self.__rate = rate 
 
    def way_calc(self): 
            f = round(self.__gas_amount / self.__rate, 2) 
            print(f'Бензина хватит на {f} км.') 
f = Car(70) 
f.way_calc() 
f.rate = 15 
f.way_calc() 
 
