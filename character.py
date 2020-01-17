import random

traits = [ # Acolyte
'I idolize a particular hero of my faith, and constantly refer to their deeds and example.',
'I can find common ground between the fiercest enemies, empathizing with them and always working towards peace.',
'I see omens in every event and action. The gods try to speak to us, we just need to listen.',
'Nothing can shake my optimistic attitude.',
'I quote (or misquote) sacred texts and proverbs in almost every situation.',
'I am tolerant (or intolerant) of other faiths and respect (or condemn) the worship of other gods.',
'I have spent so long in the temple that I have little practical experience dealing with people in the outside world.',
# Charlatan
''
]

ideals = [ # Acolyte
'The ancient traditions of worship and sacrifice must be preserved and upheld.',
'I always try to help those in need, no matter what the personal cost.',
'We must help bring about the changes the gods are constantly working in the world.',
'I hope to one day rise to the top of the religious hierarchy of my faith.',
'I trust that my deity will guide my actions. I have faith that if I work hard, things wil go well.',
'I seek to prove myself worthy of the favor of my god by matching my actions against his or her teachings.',
# Charlatan
''
]

bonds = [ # Acolyte
'I would die to recover an ancient relic of my faith that was lost long ago.',
'I will someday get revenge on the corrupt temple hierarchy who branded me a heretic.',
'I owe my life to the priest who took me in when my parents died.',
'Everything I do is for the common people.',
'I will do anything to protect the temple where I served.',
'I seek to preserve a sacred text that my enemies consider heretical and seek to destroy.',
# Charlatan
]

flaws = [ # Acolyte
'I judge others harshly, and myself even more severely.',
'I put too much trust in those who would wield power within the hierarchy of my temple.',
'My piety sometimes leads me to blindly trust those that profess faith in my god.',
'I am inflexible in my thinking.',
'I am suspicious of strangers and expect the worst of them.',
'Once I pick a goal, I become obsessed with it to the detriment of everything else in my life.',
# Charlatan
''
]

why = [ # Acolyte

]

# Charlatan only
scams = ['I cheat at games of chance.',
'I shave coins or forge documents.',
'I insert myself into the lives of others to prey on their weaknesses and secure their fortunes.',
'I put on new identities like clothes.',
'I run sleight-of-hand cons on street corners.',
'I convince people that worthless junk is worth their hard-earned money.']



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
