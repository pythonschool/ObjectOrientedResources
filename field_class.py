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

    def report_contents(self):
        crop_report = []
        animal_report = []
        for crop in self._crops:
            crop_report.append(crop.report())
        for animal in self._animals:
            animal_report.append(animal.report())
        return {"crops": crop_report,"animals":animal_report}

    def report_needs(self):
        food = 0
        light = 0
        water = 0
        for crop in self._crops:
            needs = crop.needs()
            if needs["light need"] > light:
                light = needs["light need"]
            if needs["water need"] > water:
                water = needs["water need"]
        for animal in self._animals:
            needs = animal.needs()
            food += needs["food need"]
            if needs["water need"] > water:
                water = needs["water need"]
        return {"food":food,"light":light,"water":water}

    def grow(self,light,food,water):
        #grow the crops (light and water are available to all crops in same amounts)
        if len(self._crops) > 0:
            for crop in self._crops:
                crop.grow(light,water)
        if len(self._animals) > 0:
            #grow the animals (water available to all animals in same amounts but food is a total that must be shared)
            food_required = 0
            #get a total of the food needed by the animals in the field
            for animal in self._animals:
                needs = animal.needs()
                food_required += needs["food need"]
            #if we have more food available than is required work out the additional available food
            if food > food_required:
                additional_food = food - food_required
                food = food_required
            else:
                additional_food = 0
            #grow each animal
            for animal in self._animals:
                #get the animals food needs
                needs = animal.needs()
                if food >= needs["food need"]:
                    #remove food for this animal from total
                    food -= needs["food need"]
                    print(food)
                    feed = needs["food need"]
                    #see if there is any additional food to give
                    if additional_food > 0:
                        #remove some additional food for this animal
                        additional_food -= 1
                        #add this to the foot to be given to the animal
                        feed += 1
                    #grow the animal
                    animal.grow(feed,water)

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
    new_field.add_animal(Cow("Bob"))
    new_field.add_animal(Sheep("Sally"))
    print(new_field.report_contents())
    print(new_field.report_needs())
    new_field.grow(0,10,4)
    print(new_field.report_contents())

if __name__ == '__main__':
    main()

    