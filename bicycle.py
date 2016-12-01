# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This class is used to define a bicycle object

class Bicycle:
    # this class defines a bicycle

    # class variable shared by all instances
    

    def __init__(self):
        # private fields
        
        self.__cadence = 0
        self.__speed = 0
        self.__gear = 1

        # public properties
        self.some_property = None

    # properties
    def get_cadence(self):
        # get the cadence property
        return self.__cadence
    
    def set_cadence(self, new_cadence):
        # set the cadence property
        if new_cadence < 0:
            #this is illegal, so do nothing
            pass
        else:
            self.__cadence_speed_recalculation(new_cadence)
            self.__cadence = new_cadence
    
    def get_speed(self):
        # get the speed property
        return self.__speed
    
    def get_gear(self):
        # get the gear property
        return self.__gear
    
    def set_gear(self, new_gear):
        # set the gear property
        if new_gear < 0 or new_gear > 10:
            # do nothing, this is illegal
            pass
        else:
            self.__gear_speed_recalculation(new_gear)
            self.__gear = new_gear
    
    
    # private methods
    def __gear_speed_recalculation(self, new_gear):
        # if you change the gear on a bike, the speed will change
        old_gear = self.__gear
        
        if old_gear > new_gear:
            self.__speed = self.__speed - 5
        elif old_gear < new_gear:
            self.__speed = self.__speed + 5
        else:
            # same gear!
            pass
    
    def __cadence_speed_recalculation(self, new_cadence):
        # if you change the cadence on a bike, the speed will change
        old_cadence = self.__cadence
        
        if old_cadence > new_cadence:
            self.__speed = self.__speed + (1 + (new_cadence-old_cadence)/20)
        elif old_cadence < new_cadence:
            self.__speed = self.__speed + (1 + (new_cadence-old_cadence)/20)
        else:
            # same cadence!
            pass
    
    # public methods
    
    def apply_brakes(self, speed_decrease):
        # decrease the current speed by value passed in
        
        self.__speed = self.__speed - speed_decrease
        if self.__speed < 0:
            self.__speed = 0
