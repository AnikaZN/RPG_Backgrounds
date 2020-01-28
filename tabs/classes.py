import random
import os
from .traits import Traits
from .ideals import Ideals
from .bonds import Bonds
from .flaws import Flaws
from .why import Motivations
from .unique import Scams, Specialties, Routines, Events, Guilds, Reasons, Focuses, Ranks
from .events import Core, Adventures, Arcane, Boons, Crime, Punishment, Supernatural, Tragedies, War, Weird

class Personality():
    def __init__(self, background):
        self.background = background

    def personality(self):
        if self.background == "Acolyte":
            trait = Traits[random.randint(0, 7)]
            ideal = Ideals[random.randint(0, 5)]
            bond = Bonds[random.randint(0, 5)]
            flaw = Flaws[random.randint(0, 5)]
            why = Motivations[random.randint(0, 5)]
            return(trait + ' ' + ideal + ' ' + bond + ' ' + flaw + ' ' + why)

        elif self.background == "Charlatan":
            scam = Scams[random.randint(0, 5)]
            trait = Traits[random.randint(8, 15)]
            ideal = Ideals[random.randint(6, 11)]
            bond = Bonds[random.randint(6, 11)]
            flaw = Flaws[random.randint(6, 11)]
            why = Motivations[random.randint(6, 11)]
            return('My favorite scam is ' + scam + ' ' + trait + ' ' + ideal + ' ' + bond + ' ' + flaw + ' ' + why)

        elif self.background == "Criminal":
            specialty = Specialties[random.randint(0, 7)]
            trait = Traits[random.randint(16, 23)]
            ideal = Ideals[random.randint(12, 17)]
            bond = Bonds[random.randint(12, 17)]
            flaw = Flaws[random.randint(12, 17)]
            why = Motivations[random.randint(12, 17)]
            return('My speciality is ' + specialty + ' ' +  trait + ' ' + ideal + ' ' + bond + ' ' + flaw + ' ' + why)

        elif self.background == "Entertainer":
            routine = Routines[random.randint(0, 9)]
            trait = Traits[random.randint(24, 31)]
            ideal = Ideals[random.randint(18, 23)]
            bond = Bonds[random.randint(18, 23)]
            flaw = Flaws[random.randint(18, 23)]
            why = Motivations[random.randint(18, 23)]
            return('I am mainly a ' + routine + ' ' + trait + ' ' + ideal + ' ' + bond + ' ' + flaw + ' ' + why)

        elif self.background == "Folk Hero":
            event = Events[random.randint(0, 9)]
            trait = Traits[random.randint(32, 39)]
            ideal = Ideals[random.randint(24, 29)]
            bond = Bonds[random.randint(24, 29)]
            flaw = Flaws[random.randint(24, 29)]
            why = Motivations[random.randint(24, 29)]
            return(event + ' ' + trait + ' ' + ideal + ' ' + bond + ' ' + flaw + ' ' + why)

        elif self.background == "Guild Artisan":
            guild = Guilds[random.randint(0, 19)]
            trait = Traits[random.randint(40, 47)]
            ideal = Ideals[random.randint(30, 35)]
            bond = Bonds[random.randint(30, 35)]
            flaw = Flaws[random.randint(30, 35)]
            why = Motivations[random.randint(30, 35)]
            return('I belong to the guild of ' + guild + ' ' + trait + ' ' + ideal + ' ' + bond + ' ' + flaw + ' ' + why)

        elif self.background == "Hermit":
            reason = Reasons[random.randint(0, 7)]
            trait = Traits[random.randint(48, 55)]
            ideal = Ideals[random.randint(36, 41)]
            bond = Bonds[random.randint(36, 41)]
            flaw = Flaws[random.randint(36, 41)]
            why = Motivations[random.randint(36, 41)]
            return(reason + ' ' + trait + ' ' + ideal + ' ' + bond + ' ' + flaw + ' ' + why)

        elif self.background == "Noble":
            trait = Traits[random.randint(56, 63)]
            ideal = Ideals[random.randint(42, 47)]
            bond = Bonds[random.randint(42, 47)]
            flaw = Flaws[random.randint(42, 47)]
            why = Motivations[random.randint(42, 47)]
            return(trait + ' ' + ideal + ' ' + bond + ' ' + flaw + ' ' + why)

        elif self.background == "Outlander":
            trait = Traits[random.randint(64, 71)]
            ideal = Ideals[random.randint(48, 53)]
            bond = Bonds[random.randint(48, 53)]
            flaw = Flaws[random.randint(48, 53)]
            why = Motivations[random.randint(48, 53)]
            return(trait + ' ' + ideal + ' ' + bond + ' ' + flaw + ' ' + why)

        elif self.background == "Sage":
            focus = Focuses[random.randint(0, 7)]
            trait = Traits[random.randint(72, 79)]
            ideal = Ideals[random.randint(54, 59)]
            bond = Bonds[random.randint(54, 59)]
            flaw = Flaws[random.randint(54, 59)]
            why = Motivations[random.randint(54, 59)]
            return('My focus is as a ' + focus + ' ' + trait + ' ' + ideal + ' ' + bond + ' ' + flaw + ' ' + why)

        elif self.background == "Sailor":
            trait = Traits[random.randint(80, 87)]
            ideal = Ideals[random.randint(60, 65)]
            bond = Bonds[random.randint(60, 65)]
            flaw = Flaws[random.randint(60, 65)]
            why = Motivations[random.randint(60, 65)]
            return(trait + ' ' + ideal + ' ' + bond + ' ' + flaw + ' ' + why)

        elif self.background == "Soldier":
            rank = Ranks[random.randint(0, 7)]
            trait = Traits[random.randint(88, 95)]
            ideal = Ideals[random.randint(66, 71)]
            bond = Bonds[random.randint(66, 71)]
            flaw = Flaws[random.randint(66, 71)]
            why = Motivations[random.randint(66, 71)]
            return('My rank is ' + rank + ' ' + trait + ' ' + ideal + ' ' + bond + ' ' + flaw + ' ' + why)

        else: # Urchin
            trait = Traits[random.randint(96, 102)]
            ideal = Ideals[random.randint(72, 76)]
            bond = Bonds[random.randint(72, 76)]
            flaw = Flaws[random.randint(72, 76)]
            why = Motivations[random.randint(72, 76)]
            return(trait + ' ' + ideal + ' ' + bond + ' ' + flaw + ' ' + why)

    def birthplace(self):
        born = random.randint(0, 99)
        if born < 50:
            return "I was born at home."
        elif 50 <= born <= 54:
            return "I was born in the home of a family friend."
        elif 55 <= born <= 62:
            return "I was born in the home of a healer or midwife."
        elif 63 <= born <= 64:
            return "I was born in a carriage, cart, or wagon."
        elif 65 <= born <= 67:
            return "I was born in a barn or a shed."
        elif 68 <= born <= 69:
            return "I was born in a cave."
        elif 70 <= born <= 71:
            return "I was born in a field."
        elif 72 <= born <= 73:
            return "I was born in a forest."
        elif 74 <= born <= 76:
            return "I was born in a temple."
        elif born == 77:
            return "I was born on a battlefield."
        elif 78 <= born <= 79:
            return "I was born in an alley or on a street."
        elif 80 <= born <= 81:
            return "I was born in a brothel, tavern, or inn."
        elif 82 <= born <= 83:
            return "I was born in a castle, keep, tower, or palace."
        elif born == 84:
            return "I was born in a sewer or rubbish heap."
        elif 85 <= born <= 87:
            return "I was born among people of a different race."
        elif 88 <= born <= 90:
            return "I was born onboard a boat or ship."
        elif 91 <= born <= 92:
            return "I was born in a prison or in the headquarters of a secret organization."
        elif 93 <= born <= 94:
            return "I was born in a sage's laboratory."
        elif born == 95:
            return "I was born in the Feyworld."
        elif born == 96:
            return "I was born in the Shadowfell."
        elif born == 97:
            return "I was born on the Astral or Ethereal Plane."
        elif born == 98:
            return "I was born on one of the Inner Planes."
        else:
            return "I was born on one of the Outer Planes."

    def siblings(self):
        roll = random.randint(1, 10)

        if 1 <= roll <= 2:
            number = 0
        elif 3 <= roll <= 4:
            number = (random.randint(1, 3))
        elif 5 <= roll <= 6:
            number = (random.randint(1, 4)) + 1
        elif 7 <= roll <= 8:
            number = (random.randint(1, 6)) + 2
        else:
            number = (random.randint(1, 8)) + 3

        if number == 0:
            return "I do not have any siblings."
        else:
            roll2 = random.randint(1, 6) + random.randint(1, 6)
            if roll2 == 2:
                return f"I am a twin, triplet, or quadruplet and have {number} total sibling(s)."
            elif 3 <= roll2 <= 7:
                return f"I am the oldest, with {number} sibling(s)."
            else:
                return f"I am the youngest, with {number} sibling(s)."

    def family_lifestyle_home(self):
        roll_f = random.randint(1, 100)
        roll_l = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        roll_h = random.randint(1, 100)

        if roll_f == 1:
            family = "I have never had a family."
        elif roll_f == 2:
            family = "I grew up in an institution."
        elif roll_f == 3:
            family = "I grew up in a temple."
        elif 4 <= roll_f <= 5:
            family = "I grew up in an orphanage."
        elif 6 <= roll_f <= 7:
            family = "I grew up under care of a guardian."
        elif 8 <= roll_f <= 15:
            family = "I grew up under care of an aunt/uncle or other extended family."
        elif 16 <= roll_f <= 25:
            family = "I grew up under care of my grandparents."
        elif 26 <= roll_f <= 35:
            family = "I grew up in an adopted family."
        elif 36 <= roll_f <= 55:
            family = "I grew up with just my father."
        elif 56 <= roll_f <= 74:
            family = "I grew up with just my mother."
        else:
            family = "I grew up with two parents."

        if roll_l == 3:
            lifestyle = "I had a wretched lifestyle growing up."
            roll_h = roll_h - 40
        elif 4 <= roll_l <= 5:
            lifestyle = "I had a squalid lifestyle growing up."
            roll_h = roll_h - 20
        elif 6 <= roll_l <= 8:
            lifestyle = "I had a poor lifestyle growing up."
            roll_h = roll_h - 10
        elif 9 <= roll_l <= 12:
            lifestyle = "I had a modest lifestyle growing up."
        elif 13 <= roll_l <= 15:
            lifestyle = "I had a comfortable lifestyle growing up."
            roll_h = roll_h + 10
        elif 16 <= roll_l <= 17:
            lifestyle = "I had a wealthy lifestyle growing up."
            roll_h = roll_h + 20
        else:
            lifestyle = "I had an aristocratic lifestyle growing up."
            roll_h = roll_h + 40

        if roll_h <= 0:
            home = "I grew up on the streets."
        elif 1 <= roll_h <= 20:
            home = "I grew up in a rundown shack."
        elif 21 <= roll_h <= 30:
            home = "I had no permanent residence growing up; we moved around a lot."
        elif 31 <= roll_h <= 40:
            home = "I grew up in an encampment or village in the wilderness."
        elif 41 <= roll_h <= 50:
            home = "I grew up in an apartment in a rundown neighborhood."
        elif 51 <= roll_h <= 70:
            home = "I grew up in a small house."
        elif 71 <= roll_h <= 90:
            home = "I grew up in a large house."
        elif 91 <= roll_h <= 110:
            home = "I grew up in a mansion."
        else:
            home = "I grew up in a palace or castle."

        return family + ' ' + lifestyle + ' ' + home


class Backstory():
    def __init__(self, age):
        self.age = age

    def life_events(self):
        if self.age <= 20:
            count = 1
        elif 21 <= self.age <= 30:
            count = random.randint(1, 4)
        elif 31 <= self.age <= 40:
            count = random.randint(1, 6)
        elif 41 <= self.age <= 50:
            count = random.randint(1, 8)
        elif 51 <= self.age <= 60:
            count = random.randint(1, 10)
        else:
            count = random.randint(1, 12)

        list = [random.randint(1, 100) for _ in range(count)]

        events = []

        for item in list:
            if 1 <= item <= 10:
                result = Core[0] + Tragedies[random.randint(0, 10)]
                events.append(result)
            elif 11 <= item <= 20:
                result = Core[1] + Boons[random.randint(0, 9)]
                events.append(result)
            elif 21 <= item <= 30:
                result = Core[2]
                events.append(result)
            elif 31 <= item <= 40:
                result = Core[3]
                events.append(result)
            elif 41 <= item <= 50:
                result = Core[4]
                events.append(result)
            elif 51 <= item <= 70:
                result = Core[5]
                events.append(result)
            elif 71 <= item <= 75:
                result = Core[6]
                events.append(result)
            elif 76 <= item <= 80:
                result = Core[7] + Adventures[random.randint(0, 10)]
                events.append(result)
            elif 81 <= item <= 85:
                result = Core[8] + Supernatural[random.randint(0, 14)]
                events.append(result)
            elif 86 <= item <= 90:
                result = Core[9] + War[random.randint(0, 6)]
                events.append(result)
            elif 91 <= item <= 95:
                result = Core[10] + Crime[random.randint(0, 7)] + Punishment[random.randint(0, 3)]
                events.append(result)
            elif 96 <= item <= 99:
                result = Core[11] + Arcane[random.randint(0, 9)]
                events.append(result)
            else:
                result = Core[12] + Weird[random.randint(0, 11)]
                events.append(result)

            string_events = ' '.join(events)

        return string_events
