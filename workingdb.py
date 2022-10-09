import os

# diet can be 'veg', 'vegan', 'dairy'
diet = 'vegan'

# These paths need to be changed to point to your own txt files
againstVeg = open(".\Working fragments\\databases\\vegdb.txt", "r").read().lower().split(',')
againstVegan = open(".\Working fragments\\databases\\vegandb.txt", "r").read().lower().split(',')
againstDairy = open(".\Working fragments\\databases\\dairydb.txt", "r").read().lower().split(',')

DietDict = {'vegan':againstVegan,'veg':againstVeg,'dairy':againstDairy}
ingList = 'wheat,water,orange,mango,beef'

against = False
for i in ingList.split(','):
    if i in DietDict[diet]:
        against = True

print(against)

# Program works as long as the items against diet are in the DB