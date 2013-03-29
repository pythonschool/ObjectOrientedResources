import random

class Animal:
    """a generic animal"""

    #constructor
    def __init__(self,growth_rate,food_need,water_need,name):
        #set the attributes with an initial value

        self._weight = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "Baby"
        self._type = "Generic"
        self.name = name

        #the above attributes are prefixed with an underscore to indicate that they should not be
        #accessed directly from outwith the class except for name which can be changed freely

    #method to indicate the needs of the animal
    def needs(self):
        #return a dictionary containing the food and water needs
        return {'food need':self._food_need,'water need':self._water_need}

    #method to provide information about the current state of the animal
    def report(self):
        #return a dictionary containing name,type,status, weight and days growing
        return {'name':self.name,'type':self._type,'status':self._status,'weight':self._weight,'days growing':self._days_growing}

    #the underscore indicates that this method should not be called from outwith the class
    def _update_status(self):
        if self._weight > 30:
            self._status = "Prime"
        elif self._weight > 15:
            self._status = "Fine"
        elif self._weight > 10:
            self._status = "Poor"
        elif self._weight >= 0:
            self._status = "Baby"

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
        #increment days growing
        self._days_growing += 1
        #update the status
        self._update_status()

def manual_grow(self):
    #get the food and water values from the user
    valid = False
    while not valid:
        try:
            food = int(input("Please enter a food value (1-10): "))
            if 1 <= food <= 10:
                valid = True
            else:
                print("Value entered not valid - please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not valid - please enter a value between 1 and 10")
    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value (1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered not valid - please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not valid - please enter a value between 1 and 10")
    #grow the animal
    self.grow(food,water)

def auto_grow(self,days):
    #grow the animal automatically over 30 days
    for day in range(days):
        food = random.randint(1,10)
        water = random.randint(1,10)
        self.grow(food,water)

def displayMenu():
    print('1. Grow manually over 1 day')
    print('2. Grow automatically over 30 days')
    print('3. Report status')
    print('0. Exit test program')
    print()
    print('Please select an option from the above menu')

def getMenuChoice():
    optionValid = False
    while optionValid == False:
        try:
            choice = int(input('Option Selected: '))
            if (choice >= 0) and (choice <= 4):
                optionValid = True
            else:
                print('Please enter a valid option')
        except ValueError:
            print('Please enter a valid option')
    return choice

def manage_animal(self):
    print('This is animal management program')
    print()
    noexit = True
    while noexit:
        displayMenu()
        option = getMenuChoice()
        print()
        if option == 1:
            manual_grow(self)
            print()
        elif option == 2:
            auto_grow(self,30)
            print()
        elif option == 3:
            print(self.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print('Thank you for using the animal management program')

def main():
    #instaniate the class
    new_animal = Animal(1,4,5,"Sally")
    #test to see whether it works or not
    manage_animal(new_animal)

if __name__ == '__main__':
    main()