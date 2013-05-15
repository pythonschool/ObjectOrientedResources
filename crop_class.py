import random

class Crop:
    """A generic food crop"""

    #constructor
    def __init__(self,growth_rate,light_need,water_need):
        #set the attributes with an initial value

        self._growth       = 0
        self._days_growing = 0
        self._growth_rate  = growth_rate
        self._light_need   = light_need
        self._water_need   = water_need
        self._status       = "Seed"
        self._type         = "Generic"

        #the above attributes are prefixed with an underscore to indicate that they should not be
        #accessed directly from outwith the class

    #method to indicate the needs of the crop
    def needs(self):
        #return a dictionary containing the light and water needs
        return {'light need':self._light_need,'water need':self._water_need}

    #method to report the provide information about the current state of the crop
    def report(self):
        #return a dictionary containing type,status,growth and days growing
        return {'type':self._type,'status':self._status,'growth':self._growth,'days growing':self._days_growing}

    #the underscore indicates that this method should not be called from outwith the class
    def _update_status(self):
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Seedling"
        elif self._growth == 0:
            self._status = "Seed"

    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
        #increment days growing
        self._days_growing += 1
        #update the status
        self._update_status()

def manual_grow(self):
    #get the light and water values from the user
    valid = False
    while not valid:
        try:
            light = int(input("Please enter a light value (1-10): "))
            if 1 <= light <= 10:
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
    #grow the crop
    self.grow(light,water)

def auto_grow(self,days):
    #grow the crop automatically over 30 days
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        self.grow(light,water)

def display_menu():
    print('1. Grow manually over 1 day')
    print('2. Grow automatically over 30 days')
    print('3. Report status')
    print('0. Exit test program')
    print()
    print('Please select an option from the above menu')

def get_menu_choice():
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

def manage_crop(self):
    print('This is crop management program')
    print()
    exit = False
    while not exit:
        display_menu()
        option = get_menu_choice()
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
            exit = True
            print()
    print('Thank you for using the crop management program')

def main():
    #instaniate the class
    new_crop = Crop(1,4,3)
    #test to see whether it works or not
    manage_crop(new_crop)

if __name__ == '__main__':
    main()