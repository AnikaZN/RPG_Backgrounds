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
'I fall in and out of love easily, and am always pursuing someone.',
'I have a joke for every occasion, especially occasions where humor is inappropriate.',
'Flattery is my preferred trick for getting what I want.',
'I am a born gambler who cannot resist taking a risk for a potential payoff.',
'I lie about almost everything, even when there is no good reason to.',
'Sarcasm and insults are my weapons of choice.',
'I keep multiple holy symbols on me and invoke whatever deity might come in useful at any given moment.',
'I pocket anything I see that might have some value.',
# Criminal
'I always have a plan for what to do when things go wrong.',
'I am always calm, no matter what the situation. I never raise my voice or let my emotions control me.',
'The first thing I do in a new place is note the locations of everything valuable-or where such things could be hidden.',
'I would rather make a new friend than a new enemy.',
'I am incredibly slow to trust. Those who seem the fairest often have the most to hide.',
'I do not pay attention to the risks in a situation. Never tell me the odds.',
'The best way to get me to do something is to tell me I cannot do it.',
'I blow up at the slightest insult.',

]

ideals = [ # Acolyte
'The ancient traditions of worship and sacrifice must be preserved and upheld.',
'I always try to help those in need, no matter what the personal cost.',
'We must help bring about the changes the gods are constantly working in the world.',
'I hope to one day rise to the top of the religious hierarchy of my faith.',
'I trust that my deity will guide my actions. I have faith that if I work hard, things wil go well.',
'I seek to prove myself worthy of the favor of my god by matching my actions against his or her teachings.',
# Charlatan
'I am a free spirit – no one tells me what to do.',
'I never target people who cannot afford to lose a few coins.',
'I distribute the money I acquire to the people who really need it.',
'I never run the same con twice.',
'Material goods come and go. Bonds of friendship last forever.',
'I am determined to make something of myself.',
# Criminal
'I do not steal from others in the trade.',
'Chains are meant to be broken, as are those who would forge them.',
'I steal from the wealthy so that I can help people in need.',
'I will do whatever it takes to become wealthy.',
'I am loyal to my friends, not to any ideals, and everyone else can take a trip down the Styx for all I care.',
'There is a spark of good in everyone.',

]

bonds = [ # Acolyte
'I would die to recover an ancient relic of my faith that was lost long ago.',
'I will someday get revenge on the corrupt temple hierarchy who branded me a heretic.',
'I owe my life to the priest who took me in when my parents died.',
'Everything I do is for the common people.',
'I will do anything to protect the temple where I served.',
'I seek to preserve a sacred text that my enemies consider heretical and seek to destroy.',
# Charlatan
'I fleeced the wrong person and must work to ensure that this individual never crosses paths with me or those I care about.',
'I owe everything to my mentor – a horrible person who is probably rotting in jail somewhere.',
'Somewhere out there, I have a child who does not know me. I am making the world better for him or her.',
'I come from a noble family, and one day I will reclaim my lands and title from those who stole them from me.',
'A powerful person killed someone I love. Someday soon, I will have my revenge.',
'I swindled and ruined a person who did not deserve it. I seek to atone for my misdeeds but might never be able to forgive myself.',
# Criminal
'I am trying to pay off an old debt I owe to a generous benefactor.',
'My ill-gotten gains go to support my family.',
'Something important was taken from me, and I aim to steal it back.',
'I will become the greatest thief that ever lived.',
'I am guilty of a terrible crime. I hope I can redeem myself for it.',
'Someone I loved died because of a mistake I made. That will never happen again.',

]

flaws = [ # Acolyte
'I judge others harshly, and myself even more severely.',
'I put too much trust in those who would wield power within the hierarchy of my temple.',
'My piety sometimes leads me to blindly trust those that profess faith in my god.',
'I am inflexible in my thinking.',
'I am suspicious of strangers and expect the worst of them.',
'Once I pick a goal, I become obsessed with it to the detriment of everything else in my life.',
# Charlatan
'I cannot resist a pretty face.',
'I am always in debt. I spend my ill-gotten gains on decadent luxuries faster than I bring them in.',
'I am convinced that no one could ever fool me the way I fool others.',
'I am too greedy for my own good. I cannot resist taking a risk if there is money involved.',
'I cannot resist swindling people who are more powerful than me.'
'I hate to admit it and will hate myself for it, but I will run and preserve my own hide if the going gets tough.',
# Criminal
'When I see something valuable, I cannot think about anything but how to steal it.',
'When faced with a choice between money and my friends, I usually choose the money.',
'If there is a plan, I will forget it. If I do not forget it, I will ignore it.',
'I have a “tell” that reveals when I am lying.',
'I turn tail and run when things look bad.',
'An innocent person is in prison for a crime that I committed. I am okay with that.',

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

# Criminal only
specialties = ['Blackmailer',
'Burglar',
'Enforcer',
'Fence',
'Highway Robber',
'Hired Killer',
'Pickpocket',
'Smuggler']



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
            return(trait, ideal, bond, flaw, why)

        elif self.background == "Criminal":
            specialty = specialties[random.randint(0, 8)]
            trait = traits[random.randint(16, 24)]
            ideal = ideals[random.randint(12, 18)]
            bond = bonds[random.randint(12, 18)]
            flaw = flaws[random.randint(12, 18)]
            why =
            return(trait, ideal, bond, flaw, why)

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
