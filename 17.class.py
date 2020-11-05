# -----------------------------
# Program by Samodelkin
# -----------------------------

class Hero():
    """Class to create hero for our game"""
    def __init__(self, name, level, race):
        """Initiate of our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100
    def show_hero(self):
        """print parametrs of this hero"""
        discription = (self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " Health is: " + str(self.health)).title()
        print(discription)

    def level_up(self):
        """Upgrade level of a hero"""
        self.level +=1

    def move(self):
        """start moving a hero"""
        print("Hero " + self.name + " statr moving...")

    def set_health(self, new_health):
        self.health = new_health

class SuperHero(Hero):
    """class to create SuperHero"""
    def __init__(self, name, level, race, magiclevel):
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.magic = 100

    def makemagic(self):
        """Use magic"""
        self.magic -= 10

    def show_hero(self):
        discription = (self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " Health is: " + str(
            self.health) + "Magic is: " +str(self.magic)).title()
        print(discription)


#--------------MAIN----------------


myhero1 = Hero("Vurdalak", 5, "Ork")
myhero2 = Hero("Alex", 4, "Human")

myhero1.show_hero()
myhero2.move()
myhero1.level_up()
myhero1.show_hero()
myhero1.set_health(60)
myhero1.show_hero()

