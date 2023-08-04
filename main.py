class Car:
    __gas_amount = 80
    __tank_amount = 100
    __max_power = 0
    __engine_kpd = 0.9
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
    @engine_kpd.setter
    def engine_kpd(self, engine_kpd):
        self.__engine_kpd = engine_kpd

    def calc_power(self):
        self.__max_power = (self.__gas_amount / self.__tank_amount) * self.__engine_kpd * 100
        print(f'Максимальная мощность двигателя - {round(self.__max_power, 2)}%.')
        
    

f = Car()
f.calc_power()
