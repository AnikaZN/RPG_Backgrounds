import random
import os
from .traits import traits
from .ideals import ideals
from .bonds import bonds
from .flaws import flaws
from .why import why
from .unique import scams, specialties, routines, events, guilds, reasons, focuses

class Character():
    def __init__(name, age, race, class, background):
        self.name = name
        self.age = age
        self.race = race
        self.class = class
        self.background = background

    def background(self):
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
            trait = traits[random.randint(56, 64)]
            ideal = ideals[random.randint(42, 48)]
            bond = bonds[random.randint(42, 48)]
            flaw = flaws[random.randint(42, 48)]
            why =
            return(trait, ideal, bond, flaw, why)

        elif self.background == "Outlander":
            trait = traits[random.randint(64, 72)]
            ideal = ideals[random.randint(48, 54)]
            bond = bonds[random.randint(48, 54)]
            flaw = flaws[random.randint(48, 54)]
            why =
            return(trait, ideal, bond, flaw, why)

        elif self.background == "Sage":
            focus = focuses[random.randint(0, 8)]
            trait = traits[random.randint(72, 80)]
            ideal = ideals[random.randint(54, 60)]
            bond = bonds[random.randint(54, 60)]
            flaw = flaws[random.randint(54, 60)]
            why =
            return(focus, trait, ideal, bond, flaw, why)

        elif self.background == "Sailor":
            trait = traits[random.randint(80, 88)]
            ideal = ideals[random.randint(60, 66)]
            bond = bonds[random.randint(60, 66)]
            flaw = flaws[random.randint(60, 66)]
            why =
            return(trait, ideal, bond, flaw, why)

        elif self.background == "Soldier":

        else: # Urchin
