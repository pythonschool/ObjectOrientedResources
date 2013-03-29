from potato_class import *
from wheat_class import *
from cow_class import *
from sheep_class import *

class Field:
    """Simulate a field that can contain animals and crops"""

    #constructor
    def __init__(self,max_crops,max_animals):
        self._crops = []
        self._animals = []
        self._max_animals = max_animals
        self._max_crops = max_crops

    def plant_crop(self,crop):
        if len(self._crops) < self._max_crops:
            self._crops.append(crop)
            return True
        else:
            return False

    def add_animal(self,animal):
        if len(self._animals) < self._max_animals:
            self._animals.append(animal)
            return True
        else:
            return False

    def harvest_crop(self,position):
        return self._crops.pop(position)

    def remove_animal(self,position):
        return self._animals.pop(position)

def display_crops(crop_list):
    print()
    print("The following crops are in this field:")
    for pos in range(len(crop_list)):
        print("{0:>4}. {1}.".format(pos+1,crop_list[pos].report()))

def display_animals(animal_list):
    print("The following animals are in this field:")
    for pos in range(len(animal_list)):
        print("{0:>4}. {1}.".format(pos+1,animal_list[pos].report()))

def select_crop(length_list):
    selected = 0
    while selected not in range(1,length_list+1):
        selected = int(input("Please select a crop: "))
        if selected not in range(1,length_list+1):
            print("Please select a valid option")
    return selected - 1

def select_animal(length_list):
    selected = 0
    while selected not in range(1,length_list+1):
        selected = int(input("Please select an animal: "))
        if selected not in range(1,length_list+1):
            print("Please select a valid option")
    return selected - 1

def harvest_crop_from_field(new_field):
    display_crops(new_field._crops)
    selected_crop = select_crop(len(new_field._crops))
    return new_field.harvest_crop(selected_crop)

def remove_animal_from_field(new_field):
    display_animals(new_field._animals)
    selected_animal = select_animal(len(new_field._animals))
    return new_field.remove_animal(selected_animal)

def main():
    #testing
    new_field = Field(2,5)
    new_field.plant_crop(Wheat())
    new_field.plant_crop(Potato())
    new_field.add_animal(Sheep("Shaun"))
    print(new_field._crops)
    print(harvest_crop_from_field(new_field))
    print(new_field._crops)

if __name__ == '__main__':
    main()

    