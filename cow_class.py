from animal_class import *

class Cow(Animal):
    """A simulation of a Cow"""

    #constructor
    def __init__(self,name):
        #call the parent class constructor with default values for Cow
        #growth rate = 2; food need = 5, water need = 4
        super().__init__(2,5,4,name)
        self._type = "Cow" #override the parent class attribute with new value

    #override the grow method from the parent class
    def grow(self,food,water):
        if food > self._food_need:
            self._weight += self._growth_rate * 1.1
        elif food == self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
        #increment days growing
        self._days_growing += 1
        #update the status
        self._update_status()

def main():
    #instaniate the class
    new_cow = Cow("Jim")
    #test to see whether it works or not
    manage_animal(new_cow)

if __name__ == '__main__':
    main()