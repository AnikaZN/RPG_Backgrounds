import random
import os
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
'I was recruited into an army, rose to leadership, and was commended for my heroism.']

# Guild Artisan only
guilds = ['Alchemists and apothecaries',
'Armorers, locksmiths, and finesmiths',
'Brewers, distillers, and vintners',
'Calligraphers, scribes, and scriveners',
'Carpenters, roofers, and plasterers',
'Cartographers, surveyors, and chart-makers',
'Cobblers and shoemakers',
'Cooks and bakers',
'Glassblowers and glaziers',
'Jewelers and gemcutters',
'Leatherworkers, skinners, and tanners',
'Masons and stonecutters',
'Painters, limners, and sign-makers',
'Potters and tile-makers',
'Shipwrights and sailmakers',
'Smiths and metal-forgers',
'Tinkers, pewterers, and casters',
'Wagon-makers and wheelwrights',
'Weavers and dyers',
'Woodcarvers, coopers, and bowyers']

# Hermit only
reasons = ['I was searching for spiritual enlightenment.',
'I was partaking of communal living in accordance with the dictates of a religious order.',
'I was exiled for a crime I did not commit.',
'I retreated from society after a life-altering event.',
'I needed a quiet place to work on my art, literature, music, or manifesto.',
'I needed to commune with nature, far from civilization.',
'I was the caretaker of an ancient ruin or relic.',
'I was a pilgrim in search of a person, place, or relic of spiritual significance.']


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
            guild = guilds[random.randint(0, 20)]
            trait = traits[random.randint(40, 48)]
            ideal = ideals[random.randint(30, 36)]
            bond = bonds[random.randint(30, 36)]
            flaw = flaws[random.randint(30, 36)]
            why =
            return(guild, trait, ideal, bond, flaw, why)

        elif self.background == "Hermit":
            reason = reasons[random.randint(0, 8)]
            trait = traits[random.randint(48, 56)]
            ideal = ideals[random.randint(36, 42)]
            bond = bonds[random.randint(36, 42)]
            flaw = flaws[random.randint(36, 42)]
            why =
            return(reason, trait, ideal, bond, flaw, why)

        elif self.background == "Noble":

        elif self.background == "Outlander":

        elif self.background == "Sage":

        elif self.background == "Sailor":

        elif self.background == "Soldier":

        else: # Urchin
