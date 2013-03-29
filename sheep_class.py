from animal_class import *

class Sheep(Animal):
    """A simulation of a Sheep"""

    #constructor
    def __init__(self,name):
        #call the parent class constructor with default values for Sheep
        #growth rate = 3; food need = 3, water need = 2
        super().__init__(3,3,2,name)
        self._type = "Sheep" #override the parent class attribute with new value

    #override the grow method from the parent class
    def grow(self,food,water):
        if food > self._food_need:
            self._weight += self._growth_rate * 1.2
        elif food == self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
        #increment days growing
        self._days_growing += 1
        #update the status
        self._update_status()

def main():
    #instaniate the class
    new_Sheep = Sheep("Shaun")
    #test to see whether it works or not
    manage_animal(new_Sheep)

if __name__ == '__main__':
    main()