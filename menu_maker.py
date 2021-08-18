import math
import random 

#Add names of all familys participating and change following variables to match menu plan 
FAMILY_NAMES = ["Name1", "Name2"] 

NUMBER_OF_DAYS = 3
MEALS_PER_DAY = 2
FAMILYS_PER_MEAL = 2




class Family:
    name = ""
    number_of_meals = 0
    extra_meal = False

    def __init__(self, name):
        self.name = name

    def checkForMeal(self, menu):
        if self.number_of_meals < menu.meals_per_fam:
            return True
        elif self.number_of_meals == menu.meals_per_fam and menu.extra_meals > 0 and self.number_of_meals != (menu.meals_per_fam + 1):
            menu.extra_meals -=1
            self.extra_meal = True
            return True
        else:
            return False

    def addMeal(self):
        self.number_of_meals +=1
        self.extra_meal = False

class Menu:
    total_meals = NUMBER_OF_DAYS * MEALS_PER_DAY
    meals_per_fam = math.floor(total_meals*FAMILYS_PER_MEAL/len(FAMILY_NAMES))
    extra_meals = total_meals * FAMILYS_PER_MEAL % meals_per_fam
    making_menu = True
    menu = []

    def addToMenu(self, selected_families, familys):
        output = ""
        for family in selected_families:
            if family == selected_families[0]:
                output+= familys[family].name
            else:
                output += " & {}".format(familys[family].name)

        self.menu.append(output)
        self.checkComplete()   
    
    def checkComplete(self):
        if len(self.menu) == self.total_meals:
            self.making_menu = False
        else:
            self.making_menu = True
    
    def printMenu(self):
        day = 0
        meal_index = 0
        while day < NUMBER_OF_DAYS:
            print("Day: {}".format(day+1))
            meal = 0
            while meal < MEALS_PER_DAY:
                print("Meal {}: {}".format(meal+1, self.menu[meal_index]))
                meal +=1
                meal_index +=1
            day+=1


def getChoiceIndex():
    choice = random.choice(FAMILY_NAMES)
    counter = 0
    for family in FAMILY_NAMES:
        if choice == family:
            return(counter)
        else:
            counter += 1    

def getSelectedFamilies():
    selected_families = []
    family_meal_count = []
    needs_meal = []

    for family_index in range(0, len(familys)):
        family_meal_count.append(familys[family_index].number_of_meals)
    family_meal_count.sort()

    if (family_meal_count[len(family_meal_count) -1] - family_meal_count[0]) > 0:
        for family_index in range(0, len(FAMILY_NAMES)):
            if familys[family_index].number_of_meals == family_meal_count[0]:
                needs_meal.append(family_index)

        if len(needs_meal) > FAMILYS_PER_MEAL:
            random.shuffle(needs_meal)
            for family_index in range(0, FAMILYS_PER_MEAL):
                selected_families.append(needs_meal[family_index])
        else:
            random_selections = FAMILYS_PER_MEAL - len(needs_meal)
            for selected in needs_meal:
                selected_families.append(selected) 
            for select in range(0, random_selections):
                selected_families.append(getChoiceIndex())               
    else:
        for family in range(0, FAMILYS_PER_MEAL):
            selected_families.append(getChoiceIndex())
    
    return selected_families
    


created_menu = Menu()
familys = []    
random.seed()

for family_index in range(0, len(FAMILY_NAMES)):
    familys.append(Family(FAMILY_NAMES[family_index]))

while created_menu.making_menu:
    
    selected_families = getSelectedFamilies()    
    
    if len(selected_families) == len(list(dict.fromkeys(selected_families))):
        add_to_menu = True
        for family_index in selected_families:
            if familys[family_index].checkForMeal(created_menu) == False:
                add_to_menu = False
        
        if add_to_menu:
            for family_index in selected_families:
                familys[family_index].addMeal()
            created_menu.addToMenu(selected_families, familys)
        else:
            for family_index in selected_families:
                if familys[family_index].extra_meal:
                    familys[family_index].extra_meal = False
                    created_menu.extra_meals +=1


print("Menu")
created_menu.printMenu()
print ("\nTotals:")
for family_index in range(0, len(FAMILY_NAMES)):
    print("{}: {}".format(familys[family_index].name, familys[family_index].number_of_meals))