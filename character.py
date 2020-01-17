import random

class Character():
    def __init__(name, age, race, class, subclass, background):
        self.name = name
        self.age = age
        self.race = race
        self.class = class
        self.subclass = subclass
        self.background = background

traits = ['I idolize a particular hero of my faith, and constantly refer to their deeds and example.',
]

    def bg_personality(self):
        if self.background == "Acolyte":
            trait = traits[random.randint(1, 9)]
            ideal =
            bond =
            flaw =
            why =
            return
        elif self.background == "Charlatan":
            trait = traits[random.randint(9, 17)]
        elif self.background == "Criminal":
        elif self.background == "Entertainer":
        elif self.background == "Folk Hero":
        elif self.background == "Guild Artisan":
        elif self.background == "Hermit":
        elif self.background == "Noble":
        elif self.background == "Outlander":
        elif self.background == "Sage":
        elif self.background == "Sailor":
        elif self.background == "Soldier":
        else: # Urchin
