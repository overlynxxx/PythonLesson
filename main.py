class Car:
    __gas_amount = 80
    __tank_amount = 100
    __max_power = 0
    __engine_kpd = 0.9
    __max_speed = 200
    __current_speed = 0 
    def __init__(self):
        pass
        
    @property
    def gas_amount(self):
        return self.__gas_amount    
    @gas_amount.setter
    def gas_amount(self, gas_amount):
        self.__gas_amount = gas_amount
    
    @property
    def tank_amount(self):
        return self.__tank_amount
    @tank_amount.setter
    def tank_amount(self, tank_amount):
        self.__tank_amount = tank_amount

    @property
    def engine_kpd(self):
        return self.__engine_kpd
    
    @property
    def max_power(self):
        return self.__max_power
    
    @property
    def max_speed(self):
        return self.__max_speed
    @max_speed.setter
    def max_speed(self, max_speed):
        self.__max_speed = max_speed

    @property
    def current_speed(self):
        return self.__current_speed

    __max_power = round((__gas_amount / __tank_amount) * __engine_kpd * 100, 2)
    __current_speed = round((__max_power * __max_speed) / 100)

    

f = Car()
data = f.current_speed
print(data)
