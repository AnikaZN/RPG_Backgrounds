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
            trait = Traits[random.randint(0, 8)]
            ideal = Ideals[random.randint(0, 6)]
            bond = Bonds[random.randint(0, 6)]
            flaw = Flaws[random.randint(0, 6)]
            why = Motivations[random.randint(0, 6)]
            return(trait, ideal, bond, flaw, why)

        elif self.background == "Charlatan":
            scam = Scams[random.randint(0, 6)]
            trait = Traits[random.randint(8, 16)]
            ideal = Ideals[random.randint(6, 12)]
            bond = Bonds[random.randint(6, 12)]
            flaw = Flaws[random.randint(6, 12)]
            why = Motivations[random.randint(6, 12)]
            return(scam, trait, ideal, bond, flaw, why)

        elif self.background == "Criminal":
            specialty = Specialties[random.randint(0, 8)]
            trait = Traits[random.randint(16, 24)]
            ideal = Ideals[random.randint(12, 18)]
            bond = Bonds[random.randint(12, 18)]
            flaw = Flaws[random.randint(12, 18)]
            why = Motivations[random.randint(12, 18)]
            return(specialty, trait, ideal, bond, flaw, why)

        elif self.background == "Entertainer":
            routine = Routines[random.randint(0, 10)]
            trait = Traits[random.randint(24, 32)]
            ideal = Ideals[random.randint(18, 24)]
            bond = Bonds[random.randint(18, 24)]
            flaw = Flaws[random.randint(18, 24)]
            why = Motivations[random.randint(18, 24)]
            return(routine, trait, ideal, bond, flaw, why)

        elif self.background == "Folk Hero":
            event = Events[random.randint(0, 10)]
            trait = Traits[random.randint(32, 40)]
            ideal = Ideals[random.randint(24, 30)]
            bond = Bonds[random.randint(24, 30)]
            flaw = Flaws[random.randint(24, 30)]
            why = Motivations[random.randint(24, 30)]
            return(event, trait, ideal, bond, flaw, why)

        elif self.background == "Guild Artisan":
            guild = Guilds[random.randint(0, 20)]
            trait = Traits[random.randint(40, 48)]
            ideal = Ideals[random.randint(30, 36)]
            bond = Bonds[random.randint(30, 36)]
            flaw = Flaws[random.randint(30, 36)]
            why = Motivations[random.randint(30, 36)]
            return(guild, trait, ideal, bond, flaw, why)

        elif self.background == "Hermit":
            reason = Reasons[random.randint(0, 8)]
            trait = Traits[random.randint(48, 56)]
            ideal = Ideals[random.randint(36, 42)]
            bond = Bonds[random.randint(36, 42)]
            flaw = Flaws[random.randint(36, 42)]
            why = Motivations[random.randint(36, 42)]
            return(reason, trait, ideal, bond, flaw, why)

        elif self.background == "Noble":
            trait = Traits[random.randint(56, 64)]
            ideal = Ideals[random.randint(42, 48)]
            bond = Bonds[random.randint(42, 48)]
            flaw = Flaws[random.randint(42, 48)]
            why = Motivations[random.randint(42, 48)]
            return(trait, ideal, bond, flaw, why)

        elif self.background == "Outlander":
            trait = Traits[random.randint(64, 72)]
            ideal = Ideals[random.randint(48, 54)]
            bond = Bonds[random.randint(48, 54)]
            flaw = Flaws[random.randint(48, 54)]
            why = Motivations[random.randint(48, 54)]
            return(trait, ideal, bond, flaw, why)

        elif self.background == "Sage":
            focus = Focuses[random.randint(0, 8)]
            trait = Traits[random.randint(72, 80)]
            ideal = Ideals[random.randint(54, 60)]
            bond = Bonds[random.randint(54, 60)]
            flaw = Flaws[random.randint(54, 60)]
            why = Motivations[random.randint(54, 60)]
            return(focus, trait, ideal, bond, flaw, why)

        elif self.background == "Sailor":
            trait = Traits[random.randint(80, 88)]
            ideal = Ideals[random.randint(60, 66)]
            bond = Bonds[random.randint(60, 66)]
            flaw = Flaws[random.randint(60, 66)]
            why = Motivations[random.randint(60, 66)]
            return(trait, ideal, bond, flaw, why)

        elif self.background == "Soldier":
            rank = Ranks[random.randint(0, 7)]
            trait = Traits[random.randint(88, 96)]
            ideal = Ideals[random.randint(66, 72)]
            bond = Bonds[random.randint(66, 72)]
            flaw = Flaws[random.randint(66, 72)]
            why = Motivations[random.randint(66, 72)]
            return(rank, trait, ideal, bond, flaw, why)

        else: # Urchin
            trait = Traits[random.randint(96, 104)]
            ideal = Ideals[random.randint(72, 78)]
            bond = Bonds[random.randint(72, 78)]
            flaw = Flaws[random.randint(72, 78)]
            why = Motivations[random.randint(72, 78)]
            return(trait, ideal, bond, flaw, why)
