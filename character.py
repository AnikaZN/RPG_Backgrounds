import random
from .traits import traits
from .ideals import ideals
from .bonds import bonds
from .flaws import flaws
from .why import why


# Charlatan only
scams = ['I cheat at games of chance.',
'I shave coins or forge documents.',
'I insert myself into the lives of others to prey on their weaknesses and secure their fortunes.',
'I put on new identities like clothes.',
'I run sleight-of-hand cons on street corners.',
'I convince people that worthless junk is worth their hard-earned money.']

# Criminal only
specialties = ['Blackmailer',
'Burglar',
'Enforcer',
'Fence',
'Highway Robber',
'Hired Killer',
'Pickpocket',
'Smuggler']

# Entertainer only
routines = ['Actor',
'Dancer',
'Fire-eater',
'Jester',
'Juggler',
'Instrumentalist',
'Poet',
'Singer',
'Storyteller',
'Tumbler']

# Folk Hero only
events = ['I stood up to a tyrant.',
'I saved people during a natural disaster.',
'I stood alone against a terrible monster.',
'I stole from a corrupt merchant to help the poor.',
'I led a militia to fight off an invading army.',
'I broke into the castle of a tyrant and stole weapons to arm the people.',
'I trained the peasantry to use farm implements as weapons against invading soldiers.',
'A lord rescinded an unpopular decree after I led a symbolic act of protest against it.',
'A celestial, fey, or similar creature gave me a blessing or revealed my secret origin.',
'I was recruited into an army, rose to eladership, and was commended for my heroism.']



class Character():
    def __init__(name, age, race, class, subclass, background):
        self.name = name
        self.age = age
        self.race = race
        self.class = class
        self.subclass = subclass
        self.background = background

    def bg_personality(self):
        if self.background == "Acolyte":
            trait = traits[random.randint(0, 8)]
            ideal = ideals[random.randint(0, 6)]
            bond = bonds[random.randint(0, 6)]
            flaw = flaws[random.randint(0, 6)]
            why =
            return(trait, ideal, bond, flaw, why)

        elif self.background == "Charlatan":
            scam = scams[random.randint(0, 6)]
            trait = traits[random.randint(8, 16)]
            ideal = ideals[random.randint(6, 12)]
            bond = bonds[random.randint(6, 12)]
            flaw = flaws[random.randint(6, 12)]
            why =
            return(scam, trait, ideal, bond, flaw, why)

        elif self.background == "Criminal":
            specialty = specialties[random.randint(0, 8)]
            trait = traits[random.randint(16, 24)]
            ideal = ideals[random.randint(12, 18)]
            bond = bonds[random.randint(12, 18)]
            flaw = flaws[random.randint(12, 18)]
            why =
            return(specialty, trait, ideal, bond, flaw, why)

        elif self.background == "Entertainer":
            routine = routines[random.randint(0, 10)]
            trait = traits[random.randint(24, 32)]
            ideal = ideals[random.randint(18, 24)]
            bond = bonds[random.randint(18, 24)]
            flaw = flaws[random.randint(18, 24)]
            why =
            return(routine, trait, ideal, bond, flaw, why)

        elif self.background == "Folk Hero":
            event = events[random.randint(0, 10)]
            trait = traits[random.randint(32, 40)]
            ideal = ideals[random.randint(24, 30)]
            bond = bonds[random.randint(24, 30)]
            flaw = flaws[random.randint(24, 30)]
            why =
            return(event, trait, ideal, bond, flaw, why)


        elif self.background == "Guild Artisan":

        elif self.background == "Hermit":

        elif self.background == "Noble":

        elif self.background == "Outlander":

        elif self.background == "Sage":

        elif self.background == "Sailor":

        elif self.background == "Soldier":

        else: # Urchin
