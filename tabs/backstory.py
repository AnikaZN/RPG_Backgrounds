import random
import os
from .traits import Traits
from .ideals import Ideals
from .bonds import Bonds
from .flaws import Flaws
from .why import Motivations
from .unique import Scams, Specialties, Routines, Events, Guilds, Reasons, Focuses, Ranks

class Character():
    def __init__(self, background):
        self.background = background

    def personality(self):
        if self.background == "Acolyte":
            trait = Traits[random.randint(0, 7)]
            ideal = Ideals[random.randint(0, 5)]
            bond = Bonds[random.randint(0, 5)]
            flaw = Flaws[random.randint(0, 5)]
            why = Motivations[random.randint(0, 5)]
            return(trait, ' ', ideal, ' ', bond, ' ', flaw, ' ', why)

        elif self.background == "Charlatan":
            scam = Scams[random.randint(0, 5)]
            trait = Traits[random.randint(8, 15)]
            ideal = Ideals[random.randint(6, 11)]
            bond = Bonds[random.randint(6, 11)]
            flaw = Flaws[random.randint(6, 11)]
            why = Motivations[random.randint(6, 11)]
            return('My favorite scame is ', scam, ' ', trait, ' ', ideal, ' ', bond, ' ', flaw, ' ', why)

        elif self.background == "Criminal":
            specialty = Specialties[random.randint(0, 7)]
            trait = Traits[random.randint(16, 23)]
            ideal = Ideals[random.randint(12, 17)]
            bond = Bonds[random.randint(12, 17)]
            flaw = Flaws[random.randint(12, 17)]
            why = Motivations[random.randint(12, 17)]
            return('My speciality is ', specialty, ' ',  trait, ' ', ideal, ' ', bond, ' ', flaw, ' ', why)

        elif self.background == "Entertainer":
            routine = Routines[random.randint(0, 9)]
            trait = Traits[random.randint(24, 31)]
            ideal = Ideals[random.randint(18, 23)]
            bond = Bonds[random.randint(18, 23)]
            flaw = Flaws[random.randint(18, 23)]
            why = Motivations[random.randint(18, 23)]
            return('I am mainly a ', routine, ' ', trait, ' ', ideal, ' ', bond, ' ', flaw, ' ', why)

        elif self.background == "Folk Hero":
            event = Events[random.randint(0, 9)]
            trait = Traits[random.randint(32, 39)]
            ideal = Ideals[random.randint(24, 29)]
            bond = Bonds[random.randint(24, 29)]
            flaw = Flaws[random.randint(24, 29)]
            why = Motivations[random.randint(24, 29)]
            return(event, ' ', trait, ' ', ideal, ' ', bond, ' ', flaw, ' ', why)

        elif self.background == "Guild Artisan":
            guild = Guilds[random.randint(0, 19)]
            trait = Traits[random.randint(40, 47)]
            ideal = Ideals[random.randint(30, 35)]
            bond = Bonds[random.randint(30, 35)]
            flaw = Flaws[random.randint(30, 35)]
            why = Motivations[random.randint(30, 35)]
            return('I belong to the guild of ', guild, ' ', trait, ' ', ideal, ' ', bond, ' ', flaw, ' ', why)

        elif self.background == "Hermit":
            reason = Reasons[random.randint(0, 7)]
            trait = Traits[random.randint(48, 55)]
            ideal = Ideals[random.randint(36, 41)]
            bond = Bonds[random.randint(36, 41)]
            flaw = Flaws[random.randint(36, 41)]
            why = Motivations[random.randint(36, 41)]
            return(reason, ' ', trait, ' ', ideal, ' ', bond, ' ', flaw, ' ', why)

        elif self.background == "Noble":
            trait = Traits[random.randint(56, 63)]
            ideal = Ideals[random.randint(42, 47)]
            bond = Bonds[random.randint(42, 47)]
            flaw = Flaws[random.randint(42, 47)]
            why = Motivations[random.randint(42, 47)]
            return(trait, ' ', ideal, ' ', bond, ' ', flaw, ' ', why)

        elif self.background == "Outlander":
            trait = Traits[random.randint(64, 71)]
            ideal = Ideals[random.randint(48, 53)]
            bond = Bonds[random.randint(48, 53)]
            flaw = Flaws[random.randint(48, 53)]
            why = Motivations[random.randint(48, 53)]
            return(trait, ' ', ideal, ' ', bond, ' ', flaw, ' ', why)

        elif self.background == "Sage":
            focus = Focuses[random.randint(0, 7)]
            trait = Traits[random.randint(72, 79)]
            ideal = Ideals[random.randint(54, 59)]
            bond = Bonds[random.randint(54, 59)]
            flaw = Flaws[random.randint(54, 59)]
            why = Motivations[random.randint(54, 59)]
            return('My focus is as a ', focus, ' ', trait, ' ', ideal, ' ', bond, ' ', flaw, ' ', why)

        elif self.background == "Sailor":
            trait = Traits[random.randint(80, 87)]
            ideal = Ideals[random.randint(60, 65)]
            bond = Bonds[random.randint(60, 65)]
            flaw = Flaws[random.randint(60, 65)]
            why = Motivations[random.randint(60, 65)]
            return(trait, ' ', ideal, ' ', bond, ' ', flaw, ' ', why)

        elif self.background == "Soldier":
            rank = Ranks[random.randint(0, 7)]
            trait = Traits[random.randint(88, 95)]
            ideal = Ideals[random.randint(66, 71)]
            bond = Bonds[random.randint(66, 71)]
            flaw = Flaws[random.randint(66, 71)]
            why = Motivations[random.randint(66, 71)]
            return('My rank is ', rank, ' ', trait, ' ', ideal, ' ', bond, ' ', flaw, ' ', why)

        else: # Urchin
            trait = Traits[random.randint(96, 103)]
            ideal = Ideals[random.randint(72, 77)]
            bond = Bonds[random.randint(72, 77)]
            flaw = Flaws[random.randint(72, 77)]
            why = Motivations[random.randint(72, 77)]
            return(trait, ' ', ideal, ' ', bond, ' ', flaw, ' ', why)
