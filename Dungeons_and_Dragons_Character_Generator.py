"""
Created on Tuesday April 30 2019

@author: terreratman
"""

# =============================================================================
# I made this because my group has their noses in the books 24/7 and I want things to go a bit quicker. I'm hoping some random characters will allow them to focus on familiarizing themselves with the game rules by pushing them through different situations
# The code contains every race allowed in the Adventurer's League as well as some extras, every published class and background (I listed some extra classes, but have not finished their code until I test their balance)
# None of my code is very elegant as I have just learned python in the past two weeks.
# Please feel free to leave critisisms and suggestions, it will help me learn. :)
#
# Known Gaps in the character creator:
#
# Does not account for the level 4, 8, 12, and 16 stat increase or feat choice if making a higher level character
# Does not include languages yet because I'm still investigating a method to add a random item to a list only if the addition is not already in the list, and if it was already in the list, pick a new item and try to add
# Does not have a seperate category for currency because I'm not sure how to account for adding from multiple sources
# Does not account for Personality Traits, Ideals or Bonds because I don't want to write a random.choice for things that bulky, trying to find another way
# Not all Skin/Hair/Eye colours may be correct, I just put some in quickly
# It does not print class traits
# =============================================================================

import random
import collections

def Normal(Min, Max): # Not exactly sure how this one is working, but it gives a more realistic result for age, height and weight
    r = round(random.triangular(low = Min, high = Max))# Round gives us a whole number for a character's age
    return r

def HitPoints(MaxDice):
    HITPOINTS :int = 0
    if Level == 1:
        HITPOINTS :int = MaxDice + CONMOD 
        if HITPOINTS <= MaxDice:  # This makes it so that the minimum HP is your HP die but you can start stronger if it "rolls well"
            HITPOINTS :int = MaxDice
        return(HITPOINTS)
    else:
        HITPOINTS :int = MaxDice + (Level * CONMOD)
        n = 1
        while n < Level:
            ADDITION = random.randint(1,MaxDice)
            HITPOINTS :int = HITPOINTS + ADDITION
            n += 1
    if HITPOINTS <= MaxDice + (Level - 1):  # This makes it so the minimum HP increase is 1, I don't like to play with weakening characters
        HITPOINTS :int = MaxDice + (Level - 1)
    return(HITPOINTS)

def StatIncrease(Stat, NumberofIncrease):
    if Stat <= 20 - NumberofIncrease:
        Stat :int =  Stat + NumberofIncrease
    else:
        Stat :int =  20
    return(Stat)
        
def StatDecrease(Stat, NumberofDecrease):
    if Stat >= 1 + NumberofDecrease:
        Stat :int =  Stat - NumberofDecrease
    else:
        Stat :int =  1
    return(Stat)
        
def STATMOD(STAT):
    MOD :int =  round((STAT-10) / 2)
    return MOD
    
def RemoveDuplicates(List):
    final_list :list[int] = []
    for num in List:
        if num not in final_list:
            final_list.append(num)
    return final_list

Level :int = 3

# =============================================================================
# # In stead of a d20 for stats you could 4d6 drop the lowest
# def StatRoll():
#     List = []
#     n=0
#     while n < 4:
#         List.append(random.randint(1,6))
#         n = n + 1
#     MIN = (min(List))
#     List.remove(MIN)
#     Stat :int =  sum(List)
#     return Stat
# 
# STR :int = StatRoll()
# =============================================================================

Stats = ["STR", "DEX", "CON", "INT", "WIS", "CHA"] # This list will be used for the variant human later on

STR :int = random.randint (1,20)
DEX :int = random.randint (1,20)
CON :int = random.randint (1,20)
INT :int =random.randint (1,20)
WIS :int = random.randint (1,20)
CHA :int = random.randint (1,20)

ArmourProficiencies :list[str] = []
WeaponProficiencies :list[str] = []
ToolProficiencies :list[str] = []
SavingThrowProficiencies :list[str] = []
SkillProficiencies :list[str] = []
Resistances :list[str] = []
Immunities :list[str] = []
Vulnerabilities :list[str] = []
Traits :list[str] = []
Equipment :list[str] = []

Subrace :str = "N/A"
Subclass :str = "N/A"
FightingStyle :str = "N/A"
HP :int = 0
Age :int = 0
SizeMod :float = 0
Height :float = 0
Weight :float = 0
Eyes :str = "N/A"
Skin :str = "N/A"
Hair :str = "N/A"
Speed :int = 0

Skills :list[str] = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]
ArtisanTools :list[str] = ["Alchemist's Supplies", "Brewer's Supplies", "Calligrapher's Supplies", "Carpenter's Tools", "Cartographer's Tools", "Cobbler's Tools", "Cook's Utensils", "Glassblower's Tools", "Jeweler's Tools", "Leatherworker's Tools", "Mason's Tools", "Painter's Tools", "Potter's Tools", "Smith's Tools", "Tinker's Tools", "Weaver's Tools", "Woodcarver's Tools"]
GamingSets :list[str] = ["Dice Set", "Dragonchess Set", "Playing Card Set", "Three-Dragon Ante Set"]
MusicalInstruments :list[str] = ["Bagpipes", "Drum", "Dulcimer", "Flute", "Lute", "Lyre", "Horn", "Pan Flute", "Shawm", "Viol"]
MartialWeapons :list[str] = ["Battleaxe", "Flail", "Glaive", "Greataxe", "Greatsword", "Halberd", "Lance", "Longsword", "Maul", "Morningstar", "Pike", "Rapier", "Scimitar", "Shortsword", "Trident", "War Pick", "Warhammer", "Whip", "Blowgun", "Hand Crossbow", "Heavy Crossbow", "Longbow", "Net"]
MartialMelee :list[str] = ["Battleaxe", "Flail", "Glaive", "Greataxe", "Greatsword", "Halberd", "Lance", "Longsword", "Maul", "Morningstar", "Pike", "Rapier", "Scimitar", "Shortsword", "Trident", "War Pick", "Warhammer", "Whip"]
SimpleWeapons :list[str] = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer", "Mace", "Quarterstaff", "Sickle", "Spear", "Light Crossbow", "Dart", "Shortbow", "Sling"]
SimpleMelee :list[str] = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer", "Mace", "Quarterstaff", "Sickle", "Spear"]

Race :list[str] = ["Aasimar", "Bugbear", "Dragonborn", "Dwarf", "Elf", "Firbolg", "Genasi", "Gith", "Gnome", "Goblin", "Goliath", "Hobgoblin", "Half-Elf", "Halfling", "Half-Orc", "Human", "Juiblexian", "Kender", "Kenku", "Kobold", "Lizardfolk", "Mousefolk", "Orc", "Succubus", "Tabaxi", "Tiefling", "Tortle", "Triton", "Yuan-Ti Pureblood"]
Race = random.choice(Race)

if Race == "Aasimar":
    Subrace :str = random.choice(["Fallen", "Protector", "Scourge"])
    CHA :int = StatIncrease(CHA, 2)
    if Subrace == "Fallen":
        STR :int = StatIncrease(STR, 1)
    if Subrace == "Protector":
        WIS :int = StatIncrease(WIS, 1)
    if Subrace == "Scourge":
        CON :int = StatIncrease(CON, 1)
    Age :int = Normal(20,140)
    SizeMod :int = Normal(2,20)
    Height :int = 4 * 12 + 10 + SizeMod
    Weight :int = 110 + SizeMod * Normal(2,8)
    Eyes :str = random.choice(["Pupil-less Pale White", "Pupil-less Gold", "Pupil-less Gray", "Pupil-less Topaz"])
    Skin :str= random.choice(["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black", "Emerald", "Gold", "Silver"])
    Hair :str = random.choice(["Red", "Blond", "Brown", "Black", "Silver"])
    Speed :int = 30
    Traits.extend(["Darkvision (60ft)", "Healing Hands", "Light Bearer"])
    Resistances.extend(["Necrotic", "Radiant"])
    if Level >= 3:
        if Subrace == "Fallen":
            Traits.extend(["Necrotic Shroud"])
        if Subrace == "Protector":
            Traits.extend(["Radiant Soul"])
        if Subrace == "Scourge":
            Traits.extend(["Radiant Consumption"])
    
if Race == "Bugbear":
    STR :int = StatIncrease(STR, 2)
    DEX :int = StatIncrease(DEX, 1)
    Age :int = Normal(16,60)
    SizeMod :int = Normal(2,16)
    Height :int = 6 * 12 + 4 + SizeMod
    Weight :int = 230 + SizeMod * Normal(2,12)
    Eyes :str = random.choice(["Yellow", "Orange", "Red", "Brown", "Greenish White"])
    Skin :str = random.choice(["Yellow", "Muddy Yellow", "Reddish Orange", "Reddish Brown"])
    Hair :str = random.choice(["Brown", "Red"])
    Speed :int = 30
    Traits.extend(["Darkvision (60ft)", "Long-Limbed", "Powerful Build", "Surprise Attack"])
    SkillProficiencies.extend(["Stealth"])
    
if Race == "Dragonborn":
    Subrace :list[str] = ["Red", "Green", "Blue", "White", "Black", "Gold", "Silver", "Brass", "Copper", "Bronze"]
    Subrace :str = random.choice(Subrace)
    STR :int = StatIncrease(STR, 2)
    CHA :int = StatIncrease(CHA, 1)
    Age :int = Normal(15,60)
    SizeMod :int = Normal(2,16)
    Height :int = 5 * 12 + 6 + SizeMod
    Weight :int = 175 + SizeMod * Normal(2,12)
    Eyes :list[str] = ["Red", "Gold"]
    Eyes :str = random.choice(Eyes)
    Skin :str= Subrace + " Scales"
    Speed :int = 30
    if Subrace == "Black":
        Resistances.extend(["Acid"])
        Traits.extend(["Acid Breath"])
    if Subrace == "Blue":
        Resistances.extend(["Lightning"])
        Traits.extend(["Lightning Breath"])
    if Subrace == "Brass":
        Resistances.extend(["Fire"])
        Traits.extend(["Fire Breath"])
    if Subrace == "Bronze":
        Resistances.extend(["Lightning"])
        Traits.extend(["Lightning Breath"])
    if Subrace == "Copper":
        Resistances.extend(["Acid"])
        Traits.extend(["Acid Breath"])
    if Subrace == "Gold":
        Resistances.extend(["Fire"])
        Traits.extend(["Fire Breath"])
    if Subrace == "Green":
        Resistances.extend(["Poison"])
        Traits.extend(["Poison Breath"])
    if Subrace == "Red":
        Resistances.extend(["Fire"])
        Traits.extend(["Fire Breath"])
    if Subrace == "Silver":
        Resistances.extend(["Cold"])
        Traits.extend(["Cold Breath"])
    if Subrace == "White":
        Resistances.extend(["Cold"])
        Traits.extend(["Cold Breath"])

    
if Race == "Dwarf":
    Subrace :list[str] = ["Duergar", "Hill", "Mountain"]
    Subrace :str = random.choice(Subrace)
    CON :int = StatIncrease(CON, 2)
    if Subrace == "Hill":
        WIS :int = StatIncrease(WIS, 1)
    if Subrace == "Mountain":
        STR :int = StatIncrease(STR, 2)
    if Subrace == "Duergar":
        STR :int = StatIncrease(STR, 1)
    Age :int = Normal(20,320)
    SizeMod :int = Normal(2,8)
    if Subrace == "Hill":
        Height :int = 3 * 12 + 8 + SizeMod
        Weight :int = 115 + SizeMod * Normal(2,12)
    if Subrace == "Mountain":
        Height :int = 4 * 12 + SizeMod
        Weight :int = 130 + SizeMod * Normal(2,12)
    if Subrace == "Duergar":
        Height :int = 3 * 12 + 8 + SizeMod
        Weight :int = 115 + SizeMod * Normal(2,12)
    Eyes :list[str] = ["Brown", "Hazel", "Green"]
    Eyes :str = random.choice(Eyes)
    Skin :list[str] = ["White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
    Skin :str= random.choice(Skin)
    Hair :list[str] = ["Bald", "Brown", "Black", "Blond", "Red"]
    Hair :str = random.choice(Hair)
    Speed :int = 25
    WeaponProficiencies.extend(["Battleaxe", "Handaxe", "Throwing Hammer", "Warhammer"])
    Traits.extend(["Dwarven Resilience"])
    if Subrace == "Hill":
        HP :int = HP + Level
        Traits.extend(["Darkvision (60ft)"])
    if Subrace == "Mountain":
        ArmourProficiencies.extend(["Light Armour", "Medium Armour"])
        Traits.extend(["Darkvision (60ft)"])
    if Subrace == "Duergar":
        Traits.extend(["Darkvision (120ft)", "Duergar Resilience", "Duergar Magic", "Sunlight Sensitivity"])
    
if Race == "Elf":
    Subrace :list[str] = ["Eladrin", "Drow", "High", "Sea", "Shadar-Kai", "Wood"]
    Subrace :str = random.choice(Subrace)
    DEX :int = StatIncrease(DEX, 2)
    if Subrace == "Eladrin" or Subrace == "Drow":
        CHA :int = StatIncrease(CHA, 1)
    if Subrace == "High":
        INT :int =StatIncrease(INT, 1)
    if Subrace == "Sea" or Subrace == "Shadar-Kai":
        CON :int = StatIncrease(CON, 1)
    if Subrace == "Wood":
        WIS :int = StatIncrease(WIS, 1)
    Age :int = Normal(20,700)
    if Subrace == "Eladrin":
        SizeMod :int = Normal(2,24)
    if Subrace == "Drow":
        SizeMod :int = Normal(2,12)
    if Subrace == "High" or Subrace == "Wood":
        SizeMod :int = Normal(2,20)
    if Subrace == "Sea" or Subrace == "Shadar-Kai":
        SizeMod :int = Normal(2,16)
    if Subrace == "Eladrin":
        Height :int = 4 * 12 + 6 + SizeMod
        Weight :int = 90 + SizeMod * random.randint(1,4)
    if Subrace == "Drow":
        Height :int = 4 * 12 + 5 + SizeMod
        Weight :int = 75 + SizeMod * random.randint(1,6)
    if Subrace == "High":
        Height :int = 4 * 12 + 6 + SizeMod
        Weight :int = 90 + SizeMod * random.randint(1,4)
    if Subrace == "Sea":
        Height :int = 4 * 12 + 6 + SizeMod
        Weight :int = 90 + SizeMod * random.randint(1,4)
    if Subrace == "Shadar-Kai":
        Height :int = 4 * 12 + 8 + SizeMod
        Weight :int = 90 + SizeMod * random.randint(1,4)
    if Subrace == "Wood":
        Height :int = 4 * 12 + 6 + SizeMod
        Weight :int = 100 + SizeMod * random.randint(1,4)
    Eyes :list[str] = ["Blue", "Violet", "Green"]
    Eyes :str = random.choice(Eyes)
    Skin :list[str] = ["Lightly Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown"]
    Skin :str= random.choice(Skin)
    Hair :list[str] = ["Dark Brown", "Autumn Orange", "Mossy Green", "Deep Gold"]
    Hair :str = random.choice(Hair)
    Speed :int = 30
    Traits.extend(["Keen Senses", "Fey Ancestry", "Trance"])
    if Subrace == "Eladrin":
        Subrace :list[str] = ["Eladrin of Autumn", "Eladrin of Winter", "Eladrin of Spring", "Eladrin of Summer"]
        Subrace :str = random.choice(Subrace)
        Traits.extend(["Darkvision (60ft)", "Fey Step"])
    if Subrace == "Drow":
        WeaponProficiencies.extend(["Rapiers", "Shortswords", "Hand Crossbows"])
        Traits.extend(["Darkvision (120ft)", "Sunlight Sensitivity", "Drow Magic"])
    if Subrace == "High":
        WeaponProficiencies.extend(["Longswords", "Shortswords", "Shortbows", "Longbows"])
        Traits.extend(["Wizard Cantrip"])
    if Subrace == "Sea":
        WeaponProficiencies.extend(["Spears", "Tridents", "Light Crossbows", "Nets"])
        Traits.extend(["Swim (30ft)", "Child of the Sea", "Friend of the Sea"])
    if Subrace == "Shadar-Kai":
        Resistances.extend(["Necrotic"])
        Traits.extend(["Blessing of the Raven Queen"])
    if Subrace == "Wood":
        Speed :int = 35
        WeaponProficiencies.extend(["Longswords", "Shortswords", "Shortbows", "Longbows"])
        Traits.extend(["Mask of the Wild"])

if Race == "Firbolg":
    WIS :int = StatIncrease(WIS, 2)
    STR :int = StatIncrease(STR, 1)
    Age :int = Normal(30,450)
    SizeMod :int = Normal(2,24)
    Height :int = 6 * 12 + 4 + SizeMod
    Weight :int = 210 + SizeMod * Normal(1,4)
    Eyes :list[str] = ["Blue", "Violet", "Green"]
    Eyes :str = random.choice(Eyes) 
    Skin :list[str] = ["Light Pink", "Grayish Blue"]
    Skin :str= random.choice(Skin)
    Hair :list[str] = ["Red", "Blonde", "Dark Brown"]
    Hair :str = random.choice(Hair)
    Speed :int = 30
    Traits.extend(["Firbolg Magic", "Hidden Step", "Powerful Build", "Speech of Beast and Leaf"])

if Race == "Genasi":
    Subrace :list[str] = ["Air", "Earth", "Fire", "Water"]
    Subrace :str = random.choice(Subrace)
    CON :int = StatIncrease(CON, 2)
    if Subrace == "Air":
        DEX :int = StatIncrease(DEX, 1)
    if Subrace == "Earth":
        STR :int = StatIncrease(STR, 1)
    if Subrace == "Fire":
        INT :int =StatIncrease(INT, 1)
    if Subrace == "Water":
        WIS :int = StatIncrease(WIS, 1)
    Age :int = Normal(20,100)
    SizeMod :int = Normal(2,20)
    Height :int = 4 * 12 + 8 + SizeMod
    Weight :int = 110 + SizeMod * Normal(2,8)
    if Subrace == "Air":
        Eyes :str = "Pale Blue"
        Skin :str= "Blueish Silver"
        Hair :str = "Blue and Gray Crystalline Hair"
    if Subrace == "Earth":
        Eyes :str = "Golden"
        Skin :str= "Brownish Gray"
        Hair :str = "Black"
    if Subrace == "Fire":
        Eyes :str = "Reddish Orange"
        Skin :str= "Bronze"
        Hair :str = "Orange"
    if Subrace == "Water":
        Eyes :str = "Deep Blue"
        Skin :str= "Green"
        Hair :str = "Dark Green"
    Speed :int = 30
    if Subrace == "Air":
        Traits.extend(["Unending Breath", "Mingle with the Wind"])
    if Subrace == "Earth":
        Traits.extend(["Earth Walk", "Merge with Stone"])
    if Subrace == "Fire":
        Resistances.extend(["Fire"])
        Traits.extend(["Darkvision(60ft)", "Reach to the Blaze"])
    if Subrace == "Water":
        Resistances.extend(["Acid"])
        Traits.extend(["Amphibious", "Swim (30ft)", "Call to the Wave"])

if Race == "Gith":
    Subrace :list[str] = ["Githyanki", "Githzerai"]
    Subrace :str = random.choice(Subrace)
    INT :int =StatIncrease(INT, 1)
    if Subrace == "Githyanki":
        STR :int = StatIncrease(STR, 2)
    if Subrace == "Githzerai":
        WIS :int = StatIncrease(WIS, 2)
    Age :int = Normal(20,80)
    SizeMod :int = Normal(2,24)
    if Subrace == "Githyanki":
        Height :int = 5 * 12 + SizeMod
        Weight :int = 100 + SizeMod * Normal(2,8)
    if Subrace == "Githzerai":
        Height :int = 4 * 12 + 11 + SizeMod
        Weight :int = 90 + SizeMod * Normal(2,8)
    Eyes :str = "Yellow"
    Skin :list[str] = ["Fair", "Pale Yellow with Green Tones", "Pale Yellow with Brown Tones"]
    Skin :str= random.choice(Skin)
    Hair :list[str] = ["Russet", "Black", "Gray"]
    Hair :str = random.choice(Hair)
    Speed :int = 30
    if Subrace == "Githyanki":
        ArmourProficiencies.extend(["Light Armour", "Medium Armour"])
        WeaponProficiencies.extend(["Shortswords", "Longswords", "Greatswords"])
        Traits.extend(["Decadent Mastery", "Githyanki Psionics"])
    if Subrace == "Githzerai":
        Traits.extend(["Mental Discipline", "Githzerai Psionics"])
    
if Race == "Gnome":
    Subrace :list[str] = ["Deep", "Forest", "Rock"]
    Subrace :str = random.choice(Subrace)
    INT :int =StatIncrease(INT, 2)
    if Subrace == "Deep" or Subrace == "Forest":
        DEX :int = StatIncrease(DEX, 1)
    if Subrace == "Rock":
        CON :int = StatIncrease(CON, 1)
    Age :int = Normal(20,400)
    SizeMod :int = Normal(2,8)
    Height :int = 2 * 12 + 11 + SizeMod
    Weight :int = 35 + SizeMod
    Eyes :list[str] = ["Glittering Opaque Black", "Glittering Opaque Blue"]
    Eyes :str = random.choice(Eyes)
    Skin :list[str] = ["Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black", "Rocky Gray"]
    Skin :str= random.choice(Skin)
    Hair :list[str] = ["Red", "Black", "Grey", "Dark Brown", "Brown", "Dirty Blonde", "Blonde", "White"]
    Hair :str = random.choice(Hair)
    Speed :int = 25
    Traits.extend(["Gnome Cunning"])
    if Subrace == "Deep":
        Traits.extend(["Darkvision (120ft)", "Stone Camoflage"])
    if Subrace == "Forest":
        Traits.extend(["Darkvision (60ft)", "Natural Illusionist", "Speak with Small Beasts"])
    if Subrace == "Rock":
        ToolProficiencies.extend(["Artisan's Tools"])
        Traits.extend(["Artificer's Lore", "Tinker"])

if Race == "Goblin":
    DEX :int = StatIncrease(DEX, 2)
    CON :int = StatIncrease(CON, 1)
    Age :int = Normal(10,35)
    SizeMod :int = Normal(2,8)
    Height :int = 2 * 12 + 11 + SizeMod
    Weight :int = 40 + SizeMod
    Eyes :str = "Beady Black"
    Skin :list[str] = ["Brownish Orange", "Greenish Orange", "Brownish Green", "Green"]
    Skin :str= random.choice(Skin)
    Hair :list[str] = ["Black", "Deep Grey", "Silver"]
    Hair :str = random.choice(Hair)
    Speed :int = 30
    Traits.extend(["Darkvision (60ft)", "Fury of the Small", "Nimble Escape"])

if Race == "Goliath":
    STR :int = StatIncrease(STR, 2)
    CON :int = StatIncrease(CON, 1)
    Age :int = Normal(20,80)
    SizeMod :int = Normal(2,20)
    Height :int = 6 * 12 + 8 + SizeMod
    Weight :int = 270 + SizeMod * Normal(2,12)
    Eyes :list[str] = ["Blue", "Green"]
    Eyes :str = random.choice(Eyes)
    Skin :str= "Grey"
    Hair :list[str] = ["Black", "Dark Brown", "Dark Grey"]
    Hair :str = random.choice(Hair)
    Speed :int = 30
    SkillProficiencies.extend(["Athletics"])
    Traits.extend(["Stone's Endurance", "Powerful Build", "Mountain Born"])
    
if Race == "Hobgoblin":
    CON :int = StatIncrease(CON, 2)
    INT :int =StatIncrease(INT, 1)
    Age :int = Normal(20,80)
    SizeMod :int = Normal(2,16)
    Height :int = 5 * 12 + 6 + SizeMod
    Weight :int = 175 + SizeMod * Normal(2,12)
    Eyes :list[str] = ["Black", "Red"]
    Eyes :str = random.choice(Eyes)
    Skin :list[str] = ["Orange", "Dirty Orange", "Red", "Dull Red", "Reddish Brown"]
    Skin :str= random.choice(Skin)
    Hair :list[str] = ["Dark Brown", "Dark Grey", "Orange", "Red"]
    Hair :str = random.choice(Hair)
    Speed :int = 30
    Traits.extend(["Darkvision (60ft)", "Martial Training", "Saving Face"])

if Race == "Half-Elf":
    Subrace :list[str] = ["N/A", "Drow", "Sun", "Moon", "Wood"]
    Subrace :str = random.choice(Subrace)
    CHA :int = StatIncrease(CHA, 2)
    Age :int = Normal(20,160)
    SizeMod :int = Normal(2,16)
    Height :int = 4 * 12 + 9 + SizeMod
    Weight :int = 110 + SizeMod * Normal(2,8)
    Eyes :list[str] = ["Blue", "Violet", "Green"]
    Eyes :str = random.choice(Eyes)
    Skin :list[str] = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown"]
    Skin :str= random.choice(Skin)
    Hair :list[str] = ["Red", "Blond", "Brown", "Black"]
    Hair :str = random.choice(Hair)
    Speed :int = 30
    Traits.extend(["Darkvision (60ft)", "Fey Ancestry"])
    if Subrace == "N/A":
        Traits.extend(["Skill Versatility"])
    if Subrace == "Drow":
        Traits.extend(["Drow Magic"])
    if Subrace == "Sun" or Subrace == "Moon":
        Choice = random.choice(["Elf Weapon Training", "Wizard Cantrip"])
        Traits.extend([Choice])
    if Subrace == "Wood":
        Choice = random.choice(["Elf Weapon Training", "Fleet of Foot", "Mask of the Wild"])
        Traits.extend([Choice])

if Race == "Halfling":
    Subrace :list[str] = ["Ghostwise", "Lightfoot", "Stout"]
    Subrace :str = random.choice(Subrace)
    DEX :int = StatIncrease(DEX, 2)
    if Subrace == "Ghostwise":
        WIS :int = StatIncrease(WIS, 1)
    if Subrace == "Lightfoot":
        CHA :int = StatIncrease(CHA, 1)
    if Subrace == "Stout":
        CON :int = StatIncrease(CON, 1)
    Age :int = Normal(20,200)
    SizeMod :int =  Normal(2,8)
    Height :int = 2 * 12 + 7 + SizeMod
    Weight :int = 35 + SizeMod
    Eyes :str = "Brown"
    Skin :list[str] = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
    Skin :str= random.choice(Skin)
    Hair :list[str] = ["Aubrun", "Black", "Brown", "Gray"]
    Hair :str = random.choice(Hair)
    Speed :int = 25
    Traits.extend(["Lucky", "Brave", "Halfling Nimbleness"])
    if Subrace == "Ghostwise":
        Traits.extend(["Silent Speech"])
    if Subrace == "Lightfoot":
        Traits.extend(["Naturally Stealthy"])
    if Subrace == "Stout":
        Resistances.extend(["Poison"])
        Traits.extend(["Stout Resilience"])
    
if Race == "Half-Orc":
    STR :int = StatIncrease(STR, 2)
    CON :int = StatIncrease(CON, 1)
    Age :int = Normal(14,60)
    SizeMod :int = Normal(2,20)
    Height :int = 4 * 12 + 10 + SizeMod
    Weight :int = 140 + SizeMod * Normal(2,12)
    Eyes :list[str] = ["Reddish Brown", "Reddish Blue", "Reddish Green", "Reddish Grey"]
    Eyes :str = random.choice(Eyes)
    Skin :str= "Greyish Green"
    Hair :list[str] = ["Dark Brown", "Bald", "Red"]
    Hair :str = random.choice(Hair)
    Speed :int = 30
    SkillProficiencies.extend(["Intimidation"])
    Traits.extend(["Darkvision (60ft)", "Relentless Endurance", "Savage Attacks"])

if Race == "Human": # I have not accounted for the different Human ethnicities
    Subrace :list[str] = ["Stat Increase", "Variant", "Variant"] # Two chances for variant, just to spice things up
    Subrace :str = random.choice(Subrace)
    if Subrace == "Stat Increase":
        STR :int = StatIncrease(STR, 1)
        DEX :int = StatIncrease(DEX, 1)
        CON :int = StatIncrease(CON, 1)
        INT :int =StatIncrease(INT, 1)
        WIS :int = StatIncrease(WIS, 1)
        CHA :int = StatIncrease(CHA, 1)
    if Subrace == "Variant":
        Choices = random.sample(Stats, 2)  # Stats list is found on line 101 above the STR/DEX/CON/INT/WIS/CHA :int = 0
        if "STR" in Choices:
            STR :int = StatIncrease(STR, 1)
        if "DEX" in Choices:
            DEX :int = StatIncrease(DEX, 1)
        if "CON" in Choices:
            CON :int = StatIncrease(CON, 1)
        if "INT" in Choices:
            INT :int =StatIncrease(INT, 1)
        if "WIS" in Choices:
            WIS :int = StatIncrease(WIS, 1)
        if "CHA" in Choices:
            CHA :int = StatIncrease(CHA, 1)        
    Age :int = Normal(20,60)
    SizeMod :int = Normal(2,20)
    Height :int = 4 * 12 + 8 + SizeMod
    Weight :int = 110 + SizeMod * Normal(2,8)
    Eyes :list[str] = ["Brown", "Hazel", "Blue", "Green", "Grey", "Amber"]
    Eyes :str = random.choice(Eyes)
    Skin :list[str] = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
    Skin :str= random.choice(Skin)
    Hair :list[str] = ["Black", "Brown", "Blonde", "Red", "White"]
    Hair :str = random.choice(Hair)
    Speed :int = 30
    if Subrace == "Variant":
        Traits.extend(["Choice of Feat"])
        SkillProficiencies.extend([random.choice(Skills)])
        
if Race == "Juiblexian":
    Subrace :list[str] = ["Corrosive", "Blasphemy", "Mnemonic"]
    Subrace :str = random.choice(Subrace)
    CON :int = StatIncrease(CON, 2)
    if Subrace == "Corrosive":
        DEX :int = StatIncrease(DEX, 1)
    if Subrace == "Blasphemy":
        CHA :int = StatIncrease(CHA, 1)
    if Subrace == "Mnemonic":
        INT :int =StatIncrease(INT, 1)
    Age :int = Normal(100,200)
    SizeMod :int = Normal(2,20)
    Height :int = 4 * 12 + 10 + SizeMod
    Weight :int = 80 + SizeMod * Normal(2,8)
    Eyes :str = "N/A"
    Skin :str= "Transparent " + random.choice(["Green", "Blueish White", "Yellow", "Orange", "Blue", "Red"])
    Hair :str = "N/A"
    Speed :int = 30
    Immunities.extend(["Poison", "Poisoned"])
    Traits.extend(["Amorphous Ooze", "Blind Vision", "Gelatinous Trance"])
    if Subrace == "Corrosive":
        Traits.extend(["Caustic Touch", "Corrosive Body"])
        Resistances.extend(["Acid"])
    if Subrace == "Blasphemy":
        Traits.extend(["Elemental Chaos", "Innate Spellcasting"])
    if Subrace == "Mnemonic":
        Traits.extend(["False Appearance", "Mnemonic Echoes"])

if Race == "Kender":
    DEX :int = StatIncrease(DEX, 2)
    CHA :int = StatIncrease(CHA, 1)
    Age :int = Normal(15,80)
    SizeMod :int = Normal(2,8)
    Height :int = 3 * 12 + 4 + SizeMod
    Weight :int = 50 + SizeMod * random.randint(1,4)
    Eyes :list[str] = ["Brown", "Hazel", "Blue", "Green", "Grey", "Amber"]
    Eyes :str = random.choice(Eyes)
    Skin :list[str] = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
    Skin :str= random.choice(Skin)
    Hair :list[str] = ["Black", "Brown", "Blonde", "Red", "White"]
    Hair :str = random.choice(Hair)
    Speed :int = 25
    Immunities.extend(["Frightened"])
    ToolProficiencies.extend(["Thieves' Tools"])
    Traits.extend(["Kender Pockets", "Nimbleness", "Taunt"])
    
if Race == "Kenku":
    DEX :int = StatIncrease(DEX, 2)
    WIS :int = StatIncrease(WIS, 1)
    Age :int = Normal(12,45)
    SizeMod :int = Normal(2,16)
    Height :int = 4 * 12 + 4 + SizeMod
    Weight :int = 50 + SizeMod * random.randint(1,6)
    Eyes :str = "Beady Black"
    Skin :str= "Black"
    Hair :str = "Black Feathers"
    Speed :int = 30
    Traits.extend(["Expert Forgery", "Mimicry"])
    KenkuSkills :list[str] = ["Acrobatics", "Deception", "Stealth", "Sleight of Hand"]
    SkillProficiencies.extend(random.sample(KenkuSkills, 2))
    
if Race == "Kobold":
    DEX :int = StatIncrease(DEX, 2)
    STR :int = StatDecrease(STR, 2)
    Age :int = Normal(8,80)
    SizeMod :int = Normal(2,8)
    Height :int = 2 * 12 + 1 + SizeMod
    Weight :int = 25 + SizeMod
    Eyes :list[str] = ["Burnt Orange", "Red"]
    Eyes :str = random.choice(Eyes)
    Skin :list[str] = ["Reddish Brown", "Green", "Blue"]
    Skin :str= random.choice(Skin)
    Hair :str = "N/A"
    Speed :int = 30
    Traits.extend(["Darkvision (60ft)", "Grovel, Cower and Beg", "Pack Tactics", "Sunlight Sensitivity"])

if Race == "Lizardfolk":
    CON :int = StatIncrease(CON, 2)
    WIS :int = StatIncrease(WIS, 1)
    Age :int = Normal(14,45)
    SizeMod :int = Normal(2,20)
    Height :int = 4 * 12 + 9 + SizeMod
    Weight :int = 120 + SizeMod * Normal(2,12)
    Eyes :list[str] = ["Red", "Green", "Gold", "Orange", "Blue"]
    Eyes :str = random.choice(Eyes)
    Skin :list[str] = ["Green Scales", "Greenish Brown", "Brown Scales", "Black Scales", "Tan Scales", "Albino Scales"]
    Skin :str= random.choice(Skin)
    Hair :list[str] = ["Pair of Spikes", "Lots of Spikes", "N/A"]
    Hair :str = random.choice(Hair)
    Speed :int = 30
    Traits.extend(["Bite", "Cunning Artisan", "Hold Breath", "Natural Armour", "Hungry Jaws"])
    LizardfolkSkills :list[str] = ["Animal Handling", "Nature", "Perception", "Stealth", "Survival"]
    SkillProficiencies.extend(random.sample(LizardfolkSkills, 2))
    
if Race == "Mousefolk":
    DEX :int = StatIncrease(DEX, 2)
    CHA :int = StatIncrease(CHA, 1)
    Age :int = Normal(10,45)
    SizeMod :int = Normal(2,8)
    Height :int = 2 * 12 + 11 + SizeMod
    Weight :int = 40 + SizeMod
    Eyes :list[str] = ["Pink", "Black"]
    Eyes :str = random.choice(Eyes)
    Skin :str= "Pink"
    Hair :list[str] = ["Beige Fur", "Black Fur", "Chocolate Fur", "Coffee Fur", "Cream Fur", "Ivory Fur", "Lilac Fur", "Silver Fur", "White Fur", "Tan Fur"]
    Hair :str = random.choice(Hair)
    Speed :int = 25
    Traits.extend(["Darkvision (60ft)", "Light Sleeper", "Mouse's Agility", "Mousefolk Senses", "Mouse's Survival"]) # I will be ediditing some of these for my campaign as they aren't well balanced
    
if Race == "Orc":
    STR :int = StatIncrease(STR, 2)
    CON :int = StatIncrease(CON, 1)
    INT :int =StatDecrease(INT, 2)
    Age :int = Normal(12,30)
    SizeMod :int = Normal(2,16)
    Height :int = 5 * 12 + 4 + SizeMod
    Weight :int = 175 + SizeMod * Normal(2,12)
    Eyes :str = "Red"
    Skin :list[str] = ["Greenish Grey", "Light Grey", "Dark Grey"]
    Skin :str= random.choice(Skin)
    Hair :str = "Black"
    Speed :int = 30
    Traits.extend(["Darkvision (60ft)", "Aggressive", "Powerful Build"])
    SkillProficiencies.extend(["Intimidation"])
    
if Race == "Succubus": # Extra class I found https://www.dndbeyond.com/races/1524-succubus
    CHA :int = StatIncrease(CHA, 1)
    Age :int = Normal(20,1000)
    SizeMod :int = Normal(2,20)
    Height :int = 4 * 12 + 8 + SizeMod
    Weight :int = 110 + SizeMod * Normal(2,8)
    Eyes :list[str] = ["Glowing Red", "Glowing Blue", "Glowing Brown", "Glowing Green"]
    Eyes :str = random.choice(Eyes)
    Skin :list[str] = ["Tan", "Olive", "White"]
    Skin :str= random.choice(Skin)
    Hair :list[str] = ["Black", "Red"]
    Hair :str = random.choice(Hair)
    Speed :int = 30
    SkillProficiencies.extend(["Persuasion"])
    Traits.extend(["Charm", "Darkvision (60ft)", "Fiendish Nature", "Shapechanger", "Small Wings"]) # I might switch some of these around with playtesting
    Vulnerabilities.extend(["Radiant"])

if Race == "Tabaxi":
    DEX :int = StatIncrease(DEX, 2)
    CHA :int = StatIncrease(CHA, 1)
    Age :int = Normal(20,60)
    SizeMod :int = Normal(2,20)
    Height :int = 4 * 12 + 10 + SizeMod
    Weight :int = 90 + SizeMod * Normal(2,8)
    Eyes :list[str] = ["Green", "Yellow"]
    Eyes :str = random.choice(Eyes)
    Skin :str= "Pink"
    Hair :list[str] = ["Yelow", "Spotted Yellow", "Orange", "Spotted Orange", "Red", "Spotted Red"]
    Hair :str = random.choice(Hair)
    Speed :int = 30
    Traits.extend(["Darkvision (60ft)", "Feline Agility", "Cat Claws"])
    SkillProficiencies.extend(["Perception", "Stealth"])
    
if Race == "Tiefling":
    Subrace :list[str] = ["Asmodeus", "Baalzebul", "Devil's Tongue", "Dispater", "Feral", "Fierna", "Glasya", "Hellfire", "Levistus", "Mammon", "Mephistopheles", "Zariel"]
    Subrace :str = random.choice(Subrace)
    if Subrace == "Asmodeus" or Subrace == "Baalzebul" or Subrace == "Devil's Tongue" or Subrace == "Hellfire" or Subrace == "Mammon" or Subrace == "Mephistopheles":
        CHA :int = StatIncrease(CHA, 2)
        INT :int =StatIncrease(INT, 1)
    if Subrace == "Dispater" or Subrace == "Glasya":
        CHA :int = StatIncrease(CHA, 2)
        DEX :int = StatIncrease(DEX, 1)
    if Subrace == "Feral":
        DEX :int = StatIncrease(DEX, 2)
        INT :int =StatIncrease(INT, 1)
    if Subrace == "Fierna":
        CHA :int = StatIncrease(CHA, 2)
        WIS :int = StatIncrease(WIS, 1)
    if Subrace == "Livistus":
        CHA :int = StatIncrease(CHA, 2)
        CON :int = StatIncrease(CON, 1)
    if Subrace == "Zariel":
        CHA :int = StatIncrease(CHA, 2)
        STR :int = StatIncrease(STR, 1)
    Age :int = Normal(20,60)
    SizeMod :int = Normal(2,16)
    Height :int = 4 * 12 + 9 + SizeMod
    Weight :int = 110 + SizeMod * Normal(2,8)
    Eyes :list[str] = ["Solid Orb of Red", "Solid Orb of Black", "Solid Orb of White", "Solid Orb of Silver", "Solid Orb of Gold"]
    Eyes :str = random.choice(Eyes)
    Skin :list[str] = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black", "Light Red", "Maroon", "Burgundy", "Dark Red", "Red"]
    Skin :str= random.choice(Skin)
    Hair :list[str] = ["Red", "Brown", "Black", "Dark Blue", "Purple"]
    Hair :str = random.choice(Hair)
    Speed :int = 30
    Traits.extend(["Darkvision (60ft)"])
    Resistances.extend(["Fire"])
    if Subrace == "Asmodeus" or Subrace == "Feral":
        Traits.extend(["Infernal Legacy"])
    if Subrace == "Baalzebul":
        Traits.extend(["Legacy of Maladomini"])
    if Subrace == "Devil's Tongue":
        Traits.extend(["Devil's Tongue"])
    if Subrace == "Dispater":
        Traits.extend(["Legacy of Dis"])
    if Subrace == "Fierna":
        Traits.extend(["Legacy of Phlegethos"])
    if Subrace == "Glasya":
        Traits.extend(["Legacy of Malbolge"])
    if Subrace == "Hellfire":
        Traits.extend(["Hellfire"])
    if Subrace == "Levistus":
        Traits.extend(["Legacy of Stygia"])
    if Subrace == "Mammon":
        Traits.extend(["Legacy of Minauros"])
    if Subrace == "Mephistopheles":
        Traits.extend(["Legacy of Cania"])
    if Subrace == "Zariel":
        Traits.extend(["Legacy of Avernus"])
    
if Race == "Tortle":
    STR :int = StatIncrease(STR, 2)
    WIS :int = StatIncrease(WIS, 1)
    Age :int = Normal(30,320)
    SizeMod :int = Normal(2,20)
    Height :int = 4 * 12 + 8 + SizeMod
    Weight :int = 350 + SizeMod * Normal(2,12)
    Eyes :list[str] = ["Yellow", "Green", "Red", "Orange", "Brown", "Brownish Yellow"]
    Eyes :str = random.choice(Eyes)
    Skin :list[str] = ["Olive Green", "Blueish Green"]
    Skin :str= random.choice(Skin)
    Hair :str = "N/A"
    Speed :int = 25
    SkillProficiencies.extend(["Survival"])
    Traits.extend(["Claws", "Hold Breath", "Natural Armour", "Shell Defense"])
    
if Race == "Triton":
    STR :int = StatIncrease(STR, 1)
    CON :int = StatIncrease(CON, 1)
    CHA :int = StatIncrease(CHA, 1)
    Age :int = Normal(15,170)
    SizeMod :int = Normal(2,20)
    Height :int = 4 * 12 + 6 + SizeMod
    Weight :int = 90 + SizeMod * Normal(2,8)
    Eyes :list[str] = ["Brown", "Hazel", "Blue", "Green", "Grey", "Amber"]
    Eyes :str = random.choice(Eyes)
    Skin :list[str] = ["Silver", "Blueish Silver"]
    Skin :str= random.choice(Skin)
    Hair :list[str] = ["Deep Blue", "Greenish Blue", "Green"]
    Hair :str = random.choice(Hair)
    Speed :int = 30
    Traits.extend(["Amphibious", "Control Air and Water", "Emissary of the Sea", "Guardians of the Depths"])
    
if Race == "Yuan-Ti Pureblood":
    CHA :int = StatIncrease(CHA, 2)
    INT :int =StatIncrease(INT, 1)
    Age :int = Normal(20,60)
    SizeMod :int = Normal(2,20)
    Height :int = 4 * 12 + 8 + SizeMod
    Weight :int = 110 + SizeMod * Normal(2,8)
    Eyes :list[str] = ["Red", "Orange", "Silver", "Copper", "Green", "Yellow"]
    Eyes :str = random.choice(Eyes)
    Skin :list[str] = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
    Skin :str= random.choice(Skin)
    Hair :list[str] = ["Black", "Brown", "Blonde", "Red", "White"]
    Hair :str = random.choice(Hair)
    Speed :int = 30
    Immunities.extend(["Poison", "Poisoned"])
    Traits.extend(["Darkvision (60ft)", "Innate Spellcasting", "Magic Resistance"])
    
STRMOD :int =STATMOD(STR)
DEXMOD :int = STATMOD(DEX)
CONMOD :int = STATMOD(CON)
INTMOD :int = STATMOD(INT)
WISMOD :int = STATMOD(WIS)
CHAMOD :int = STATMOD(CHA)

Class :str = random.choice(["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"])

# =============================================================================
# if Class == "Alchemist":
# =============================================================================
    
# =============================================================================
# if Class == "Artificer":
# =============================================================================

if Class == "Barbarian":
    if Level >= 3:
        Subclass :list[str]  = ["Path of the Ancestral Guardian", "Path of the Battlerager", "Path of the Berserker", "Path of the Storm Herald", "Path of the Totem Warrior", "Path of the Zealot"]
        Subclass :str = random.choice(Subclass)
    HP :int = HP + HitPoints(12)
    ArmourProficiencies.extend(["Light Armour", "Medium Armour", "Shields"])
    WeaponProficiencies.extend(["Simple Weapons", "Martial Weapons"])
    SavingThrowProficiencies.extend(["STR", "CON"])
    SkillProficiencies.extend(random.sample(["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"], 2))
    Equipment.extend([random.choice(["Greataxe", random.choice(MartialMelee)]), random.choice(["Two Handaxes", random.choice(SimpleWeapons)]), "Explorer's Pack", "Four Javelins"])
    
if Class == "Bard":
    if Level >= 3:
        Subclass :list[str]  = ["College of Glamour", "College of Lore", "College of Satire", "College of Swords", "College of Valor", "College of Whispers"]
        Subclass :str = random.choice(Subclass)
    HP :int = HP + HitPoints(8)
    ArmourProficiencies.extend(["Light Armour"])
    WeaponProficiencies.extend(["Simple Weapons", "Hand Crossbows", "Longswords", "Rapiers", "Shortswords"])
    ToolProficiencies.extend(random.sample(MusicalInstruments, 3))
    SavingThrowProficiencies.extend(["DEX", "CHA"])
    SkillProficiencies.extend(random.sample(Skills, 3))
    Equipment.extend([random.choice(["Rapier", "Longsword", random.choice(SimpleWeapons)]), random.choice(["Diplomat's Pack", "Entertainer's Pack"]), random.choice(["Lute", random.choice(MusicalInstruments)]), "Leather Armour", "Dagger"])
    
# =============================================================================
# if Class == "Blood Hunter":
# =============================================================================

# =============================================================================
# if Class == "Cardcaster":
# =============================================================================
    
if Class == "Cleric":
    Subclass :list[str]  = ["Arcana Domain", "Ambition Domain", "City Domain", "Death Domain", "Forge Domain", "Grave Domain", "Knowledge Domain", "Life Domain", "Light Domain", "Nature Domain", "Order Domain", "Protection Domain", "Solidarity Domain", "Strength Domain", "Tempest Domain", "Trickery Domain", "War Domain", "Zeal Domain"]
    Subclass :str = random.choice(Subclass)
    HP :int = HP + HitPoints(8)
    ArmourProficiencies.extend(["Light Armour", "Medium Armour", "Shields"])
    WeaponProficiencies.extend(["Simple Weapons"])
    SavingThrowProficiencies.extend(["WIS", "CHA"])
    SkillProficiencies.extend(random.sample(["History", "Insight", "Medicine", "Persuasion", "Religion"], 2))
    if "Warhammer" in WeaponProficiencies or "Martial Weapons" in WeaponProficiencies:
        Equipment.extend([random.choice(["Mace", "Warhammer"])])
    else:
        Equipment.extend(["Mace"])
    if "Chain Mail" in ArmourProficiencies or "Heavy Armour" in ArmourProficiencies:
        Equipment.extend([random.choice(["Scale Mail", "Leather Armour", "Chain Mail"])])
    else:
        Equipment.extend([random.choice(["Scale Mail", "Leather Armour"])])
    Equipment.extend([random.choice(["Light Crossbow with 20 Bolts", random.choice(SimpleWeapons)]), random.choice(["Priest's Pack", "Explorer's Pack"]), "Shield", "Holy Symbol"])
    
# =============================================================================
# if Class == "Diabolist":
# =============================================================================
    
if Class == "Druid":
    if Level >= 2:
        Subclass :list[str]  = ["Circle of Dreams", "Circle of the Land", "Circle of the Moon", "Circle of the Shepherd", "Circle of Spores", "Circle of Twilight"]
        Subclass :str = random.choice(Subclass)
        if Subclass == "Circle of the Land":
            Land :int = random.choice(["(Arctic)", "(Coast)", "(Desert)", "(Forest)", "(Grassland)", "(Mountain)", "(Swamp)", "(Underdark)"])
            Subclass :str = "Circle of the Land " + Land
    HP :int = HP + HitPoints(8)
    ArmourProficiencies.extend(["Light Armour", "Medium Armour", "Shields"])
    WeaponProficiencies.extend(["Clubs", "Daggers", "Darts", "Javelins", "Maces", "Quarterstaffs", "Scimitars", "Sickles", "Slings", "Spears"])
    ToolProficiencies.extend(["Herbalism Kit"])
    SavingThrowProficiencies.extend(["INT", "WIS"])
    SkillProficiencies.extend(random.sample(["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"], 2))
    Equipment.extend([random.choice(["Wooden Shield", random.choice(SimpleWeapons)]), random.choice(["Scimitar", random.choice(SimpleMelee)]), "Leather Armour", "Explorer's Pack", "Druidic Focus"])
    
# =============================================================================
# if Class == "Feywalker":
# =============================================================================
    
if Class == "Fighter":
    FightingStyle = ["Archery", "Defense", "Dueling", "Great Weapon Fighting", "Protection", "Two-Weapon Fighting"]
    FightingStyle = random.choice(FightingStyle)
    if Level >= 3:
        Subclass :list[str]  = ["Arcane Archer", "Battle Master", "Brute", "Cavalier", "Champion", "Eldritch Knight", "Purple Dragon Knight", "Samurai", "Scout", "Sharpshooter"]
        Subclass :str = random.choice(Subclass)
    HP :int = HP + HitPoints(10)
    ArmourProficiencies.extend(["Light Armour, Medium Armour, Heavy Armour", "Shields"])
    WeaponProficiencies.extend(["Simple Weapons", "Martial Weapons"])
    SavingThrowProficiencies.extend(["STR", "CON"])
    SkillProficiencies.extend(random.sample(["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"], 2))
# =============================================================================
#   This whole equipment section got messed up because one choice of equipment gives multiple items, which gives my code lists within lists. My print functions don't work with lists within lists. I'm looking for a way to simplify this. Similar issue encountered with Paladin and Ranger
# =============================================================================
    EqptExtnd = [random.choice(["Light Crossbow with 20 Bolts", "Two Handaxes"]), random.choice(["Dungeoneer's Pack", "Explorer's Pack"])]
    EqptExtnd.extend(random.choice([["Chain Mail"], ["Leather Armour", "Longbow with 20 Arrows"]]))
    EqptExtnd.extend(random.choice([[random.choice(MartialWeapons), "Shield"], random.sample(MartialWeapons, 2)]))
    Equipment.extend(EqptExtnd)
    
if Class == "Monk":
    if Level >= 3:
        Subclass :list[str]  = ["Way of the Drunken Master", "Way of the Four Elements", "Way of the Kensei", "Way of the Long Death", "Way of the Open Hand", "Way of Shadow", "Way of the Sun Soul", "Way of Tranquility"]
        Subclass :str = random.choice(Subclass)
    HP :int = HP + HitPoints(8)
    WeaponProficiencies.extend(["Simple Weapons", "Shortswords"])
    ToolProficiencies.extend([random.choice([random.choice(MusicalInstruments), random.choice(ArtisanTools)])])
    SavingThrowProficiencies.extend(["STR", "DEX"])
    SkillProficiencies.extend(random.sample(["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"], 2))
    Equipment.extend([random.choice(["Shortsword", random.choice(SimpleWeapons)]), random.choice(["Dungeoneer's Pack", "Explorer's Pack"]), "10 Darts"])
    
# =============================================================================
# if Class == "Morph":
# =============================================================================
    
# =============================================================================
# if Class == "Occultist":
# =============================================================================
    
if Class == "Paladin":
    if Level >= 2:
        FightingStyle = ["Defense", "Dueling", "Great Weapon Fighting", "Protection"]
        FightingStyle = random.choice(FightingStyle)
    if Level >= 3:
        Subclass :list[str]  = ["Oath of the Ancients", "Oath of Conquests", "Oath of the Crown", "Oath of Devotion", "Oath of Redemption", "Oath of Vengeance", "Oathbreaker", "Oath of Treachery"]
        Subclass :str = random.choice(Subclass)
    HP :int = HP + HitPoints(10)
    ArmourProficiencies.extend(["Light Armour", "Medium Armour", "Heavy Armour", "Shields"])
    WeaponProficiencies.extend(["Simple Weapons", "Martial Weapons"])
    SavingThrowProficiencies.extend(["WIS", "CHA"])
    SkillProficiencies.extend(random.sample(["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"], 2))
    EqptExtnd = random.choice([[random.choice(MartialWeapons), "Shield"], random.sample(MartialWeapons, 2)])
    EqptExtnd.extend([random.choice(["5 Javelins", random.choice(SimpleMelee)])])
    EqptExtnd.extend(["Chain Mail", "Holy Symbol"])
    Equipment.extend(EqptExtnd)
    
if Class == "Ranger":
    if Level >= 2:
        FightingStyle = ["Archery", "Defense", "Dueling", "Two-Weapon Fighting"]
        FightingStyle = random.choice(FightingStyle)
    if Level >= 3:
        Subclass :list[str]  = ["Beast Master", "Gloom Stalker", "Horizon Walker", "Hunter", "Monster Slayer", "Primeval Guardian"]
        Subclass :str = random.choice(Subclass)
    HP :int = HP + HitPoints(10)
    ArmourProficiencies.extend(["Light Armour", "Medium Armour", "Shields"])
    WeaponProficiencies.extend(["Simple Weapons", "Martial Weapons"])
    SavingThrowProficiencies.extend(["STR", "DEX"])
    SkillProficiencies.extend(random.sample(["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"], 3))
    EqptExtnd =[random.choice(["Scale Mail", "Leather Armour"])]
    EqptExtnd.extend(random.choice([["Two Shortswords"], random.sample(SimpleMelee, 2)]))
    EqptExtnd.extend([random.choice(["Dungeoneer's Pack", "Explorer's Pack"])])
    EqptExtnd.extend(["Longbow with 20 Arrows"])
    Equipment.extend(EqptExtnd)
    
if Class == "Rogue":
    if Level >= 3:
        Subclass :list[str]  = ["Arcane Trickster", "Assassin", "Inquisitive", "Mastermind", "Scout", "Swashbuckler", "Thief"]
        Subclass :str = random.choice(Subclass)
    HP :int = HP + HitPoints(8)
    ArmourProficiencies.extend(["Light Armour"])
    WeaponProficiencies.extend(["Simple Weapons", "Hand Crossbows", "Longswords", "Rapiers", "Shortswords"])
    ToolProficiencies.extend(["Thieves' Tools"])
    SavingThrowProficiencies.extend(["DEX", "INT"])
    SkillProficiencies.extend(random.sample(["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"], 4))
    Equipment.extend([random.choice(["Rapier", "Shortsword"]), random.choice(["Shortbow with 20 Arrows", "Shortsword"]), random.choice(["Burglar's Pack", "Dungeoneer's Pack", "Explorer's Pack"]), "Leather Armour", "Two Daggers", "Thieves's Tools"])
    
if Class == "Sorcerer":
    Subclass :list[str]  = ["Divine Soul", "Draconic Bloodline", "Giant Soul", "Pheonix Sorcery", "Pyromancer", "Sea Sorcery", "Shadow Magic", "Stone Soercery", "Storm Sorcery", "Wild Magic"]
    Subclass :str = random.choice(Subclass)
    HP :int = HP + HitPoints(6)
    WeaponProficiencies.extend(["Daggers", "Darts", "Slings", "Quarterstaffs", "Light Crossbows"])
    SavingThrowProficiencies.extend(["CON", "CHA"])
    SkillProficiencies.extend(random.sample(["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"], 2))
    Equipment.extend([random.choice(["Light Crossbow with 20 Bolts", random.choice(SimpleWeapons)]), random.choice(["Component Pouch", "Arcane Focus"]), random.choice(["Dungeoneer's Pack", "Explorer's Pack"]), "Two Daggers"])
    
if Class == "Warlock":
    Subclass :list[str]  = ["The Archfey", "The Celestial", "The Fiend", "The Ghost in the Machine", "The Great Old One", "The Hexblade", "The Raven Queen", "The Seeker", "The Undying"]
    Subclass :str = random.choice(Subclass)
    if Level >= 3:
        FightingStyle = ["Pact of the Chain", "Pact of the Blade", "Pact of the Tome"]
        FightingStyle = random.choice(FightingStyle)
    HP :int = HP + HitPoints(8)
    ArmourProficiencies.extend(["Light Armour"])
    WeaponProficiencies.extend(["Simple Weapons"])
    SavingThrowProficiencies.extend(["WIS", "CHA"])
    SkillProficiencies.extend(random.sample(["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"], 2))
    Equipment.extend([random.choice(["Light Crossbow with 20 Bolts", random.choice(SimpleWeapons)]), random.choice(["Component Pouch", "Arcane Focus"]), random.choice(["Scholar's Pack", "Dungeoneer's Pack"]), "Leather Armour", random.choice(SimpleWeapons), "Two Daggers"])
    
if Class == "Wizard":
    if Level >= 2:
        Subclass :list[str]  = ["Artificier", "Bladesinger", "Lore Mastery", "School of Abjuration", "School of Conjuration", "School of Divination", "School of Enchantment", "School of Evocation", "School of Illusion", "School of Invention", "School of Necromancy", "School of Transmutation", "Technomancy", "Theurgy", "War Magic"]
        Subclass :str = random.choice(Subclass)
    HP :int = HP + HitPoints(6)
    WeaponProficiencies.extend(["Daggers", "Darts", "Slings", "Quarterstaffs", "Light Crossbows"])
    SavingThrowProficiencies.extend(["INT", "WIS"])
    SkillProficiencies.extend(random.sample(["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"], 2))
    Equipment.extend([random.choice(["Quarterstaff", "Dagger"]), random.choice(["Component Pouch", "Arcane Focus"]), random.choice(["Scholar's Pack", "Explorer's Pack"]), "Spellbook"])

# Currently Removed: "Dissenter"
Background = ["Acolyte", "Anthropologist", "Archaeologist", "Black Fist Double Agent", "Caravan Specialist", "Charlatan", "City Watch", "Clan Crafter", "Cloistered Scholar", "Courtier", "Criminal", "Dragon Casualty", "Earthspur Miner", "Entertainer", "Faction Agent", "Far Traveller", "Folk Hero", "Gate Urchin", "Guild Artisan", "Harborfolk", "Haunted One", "Hermit", "Hillsfar Merchant", "Hillsfar Smuggler", "House Agent", "Inheritor", "Initiate", "Inquisitor", "Iron Route Bandit", "Knight of the Order", "Mercenary Veteran", "Mulmaster Aristocrat", "Noble", "Outlander", "Phlan Insurgent", "Phlan Refugee", "Sage", "Sailor", "Secret Identity", "Shade Fanatic", "Soldier", "Stojanow Prisoner", "Ticklebelly Nomad", "Trade Sheriff", "Urban Bounty Hunter", "Urchin", "Uthgardt Tribe Member", "Vizier", "Waterdhavian Noble"]
Background = random.choice(Background)

if Background == "Acolyte":
    SkillProficiencies.extend(["Insight", "Religion"])
    Equipment.extend(["Holy Symbol", random.choice(["Prayer Book", "Prayer Wheel"]), "5 Sticks of Incense", "Vestments", "Common Clothes", "15 gp"])
    
if Background == "Anthropologist":
    SkillProficiencies.extend(["Insight", "Religion"])
    Equipment.extend(["Leather-Bound Diary", "Bottle of Ink", "Ink Pen", "Set of Traveler's Clothes", "One Trinket of Special Significance", "10 gp"])
    
if Background == "Archaeologist":
    SkillProficiencies.extend(["History", "Survival"])
    ToolProficiencies.extend([random.choice(["Cartographer's Tools", "Navigator's Tools"])])
    Equipment.extend([random.choice(["Wooden Case Containing a Map to a Ruin", "Wooden Case Containing a Map to a Dungeon"]), "Bullseye Lantern", "Miner's Pick", "Set of Traveler's Clothes", "Shovel", "Two-Person Tent", "Trinket Recovered from a Dig Site", "25 gp"])

if Background == "Black Fist Double Agent":
    SkillProficiencies.extend(["Deception", "Insight"])
    BlackFistDoubleAgentTool = random.choice([random.choice(GamingSets), random.choice(ArtisanTools)])
    ToolProficiencies.extend(["Disguise Kit", BlackFistDoubleAgentTool])
    Equipment.extend(["Disguise Kit", "Common Clothes", "Tears of Virulence Emblem", "Writ of Free Agency Signed by the Lord Regent", BlackFistDoubleAgentTool, "15 gp"])
    
if Background == "Caravan Specialist":
    SkillProficiencies.extend(["Animal Handling", "Survival"])
    ToolProficiencies.extend(["Land Vehicles"])
    Equipment.extend(["Whip", "Tent", "Regional Map", "Traveling Clothes", "10 gp"])
    
if Background == "Charlatan":
    SkillProficiencies.extend(["Deception", "Sleight of Hand"])
    ToolProficiencies.extend(["Disguise Kit", "Forgery Kit"])
    Equipment.extend(["Fine Clothes", "Disguise Kit", random.choice(["Ten Stoppered Bottles Filled with Coloured Liquid", "Set of Weighted Dice", "Deck of Marked Cards", "Signet Ring of an Imaginary Duke"]), "15 gp"])
    
if Background == "City Watch":
    Background = random.choice(["City Watch Patrol", "City Watch Investigator"])
    SkillProficiencies.extend(["Insight"])
    if Background == "City Watch Patrol":
        SkillProficiencies.extend(["Athletics"])
    if Background == "City Watch Investigator":
        SkillProficiencies.extend(["Investigation"])
    Equipment.extend(["Uniform in the Style of Your Unit and Indicative of Your Rank", "Horn with which to Summon Help", "Set of Manacles", "10 gp"])
    
if Background == "Clan Crafter":
    SkillProficiencies.extend(["History", "Insight"])
    ClanCrafterArtisanTools = random.choice(ArtisanTools)
    ToolProficiencies.extend([ClanCrafterArtisanTools])
    Equipment.extend([ClanCrafterArtisanTools, "Maker's Mark Chisel", "Traveler's Clothes", "Gem Worth 10 gp", "5 gp"])
    
if Background == "Cloistered Scholar":
    SkillProficiencies.extend(["History", random.choice(["Arcana", "Nature", "Religion"])])
    Equipment.extend(["Scholar's Robes of Your Cloister", "Writing Kit", "Borrowed Book on the Subject of Your Current Study", "10 gp"])
    
if Background == "Cormanthor Refugee":
    SkillProficiencies.extend(["Nature", "Survival"])
    CormanthorRefugeeArtisanTools = random.choice(ArtisanTools) # Introducing a temporary variable so the same artisan's tools will be included in the equipment and proficiencies
    ToolProficiencies.extend([CormanthorRefugeeArtisanTools])
    Equipment.extend(["Two-Person Tent", CormanthorRefugeeArtisanTools, "Holy Symbol", "Traveler's Clothes", "5 gp"])
    
if Background == "Courtier":
    SkillProficiencies.extend(["Insight", "Persuasion"])
    Equipment.extend(["Set of Fine Clothes", "5 gp"])
    
if Background == "Criminal":
    Specialty = ["Blackmailer", "Burglar", "Enforcer", "Fence", "Highway Robber", "Hired Killer", "Pickpocket", "Smuggler", "Spy"]
    Background = "Criminal " + random.choice(Specialty)
    SkillProficiencies.extend(["Deception", "Stealth"])
    ToolProficiencies.extend([random.choice(GamingSets), "Thieves' Tools"])

# =============================================================================
# if Background == "Dissenter":  # Don't know what Dissenters get for proficiencies or equipment
#     SkillProficiencies.extend([])
# =============================================================================
    
if Background == "Dragon Casualty": # Tool proficiency is based on origin
    Origin = random.choice(["Dockworker/Fisherman", "Tradesperson/Merchant", "Black Fist Soldier", "Adventurer", "Entertainer", "Scholar/Healer", "Criminal", "Unskilled Labourer"])
    Background = "Dragon Casualty who used to be a " + Origin
    if Origin == "Dockworker/Fisherman":
        ToolProficiencies.extend(["Water Vehicles"])
    if Origin == "Tradesperson/Merchant":
        ToolProficiencies.extend([random.choice(ArtisanTools)])
    if Origin == "Black Fist Soldier":
        ToolProficiencies.extend([random.choice([random.choice(ArtisanTools), "Land Vehicles"])])
    if Origin == "Adventurer":
        ToolProficiencies.extend(["Land Vehicles"])
    if Origin == "Entertainer":
        ToolProficiencies.extend([random.choice(MusicalInstruments)])
    if Origin == "Scholar/Healer":
        ToolProficiencies.extend([random.choice(["Alchemist's Supplies", "Herbalism Kit"])])
    if Origin == "Criminal":
        ToolProficiencies.extend([random.choice(["Thieves' Tools", "Forgery Kit", "Disguise Kit"])])
    if Origin == "Unskilled Labourer":
        ToolProficiencies.extend([random.choice(GamingSets)])
    SkillProficiencies.extend(["Intimidation", "Survival"])
    Equipment.extend(["Dagger", "Tattered Rags", "Loaf of Moldy Bread", "Small Cast-Off Scale Belonging to Vorgansharax - The Maimed Virulence", "5 gp"])

if Background == "Earthspur Miner":
    SkillProficiencies.extend(["Athletics", "Survival"])
    Equipment.extend([random.choice(["Shovel", "Miner's Pick"]), "Block and Tackle", "Climber's Kit", "Set of Common Clothes", "5 gp"])
    
if Background == "Entertainer":
    Routine = random.sample(["an Actor", "a Dancer", "a Fire-Eater", "a Gladiator", "a Jester", "a Juggler", "an Instrumentalist", "a Poet", "a Singer", "a Storyteller", "a Tumbler"], 3) # The handbook says up to 3 routines, going with 3 to spice things up. Gladiator is also included in here for fun
    Background = "Entertainer who is " + ", and ".join(Routine)
    SkillProficiencies.extend(["Acrobatics", "Performance"])
    EntertainerMusicalInstrument = random.choice(MusicalInstruments)  # Introducing a temporary variable so the same instrument will be included in the equipment and proficiencies
    ToolProficiencies.extend(["Disguise Kit", EntertainerMusicalInstrument])
    Equipment.extend([EntertainerMusicalInstrument, random.choice(["Love Letter from an Admirer", "Lock of Hair from an Admirer", "Trinket from an Admirer"]), "Costume", "15 gp"])
    if "a Gladiator" in Routine:
        GladiatorWeapon = random.choice(["Trident", "Net"])
        WeaponProficiencies.extend([GladiatorWeapon])
        Equipment.extend([GladiatorWeapon])
    
if Background == "Faction Agent":
    Faction = random.choice(["The Emerald Enclave", "The Harpers", "The Lord's Alliance", "The Order of the Gauntlet", "The Zhentarim"])
    Background = "Faction Agent of " + Faction
    SkillProficiencies.extend(["Insight"])
    if Faction == "The Emerald Enclave":
        SkillProficiencies.extend(["Nature"])
    if Faction == "The Harpers":
        SkillProficiencies.extend(["Investigation"])
    if Faction == "The Lord's Alliance":
        SkillProficiencies.extend(["History"])
    if Faction == "The Order of the Gauntlet":
        SkillProficiencies.extend(["Religion"])
    if Faction == "The Zhentarim":
        SkillProficiencies.extend(["Deception"])
    Equipment.extend([random.choice(["Badge of " + Faction, "Emblem of " + Faction]), "Set of Common Clothes", "15 gp"])
    if Faction == "The Harpers" or Faction == "The Zhentarim":
        Equipment.extend(["Copy of a Code-Book from " + Faction])
    else: 
        Equipment.extend(["Copy of a Seminal Text from " + Faction])
    
if Background == "Far Traveler":
    Reason = random.choice(["Emissary", "Exile", "Fugitive", "Pilgrim", "Sightseer", "Wanderer"])
    Origin = random.choice(["Evermeet", "Halruaa", "Kara-Tur", "Mulhorand", "Sossal", "Zakhara", "The Underdark"])
    Background = "Far Traveler " + Reason + " from " + Origin
    SkillProficiencies.extend(["Insight", "Perception"])
    FarTravelerTool = random.choice([random.choice(MusicalInstruments), random.choice(GamingSets)])
    ToolProficiencies.extend([FarTravelerTool])
    Equipment.extend([FarTravelerTool, "Poorly Wrought Maps from " + Origin, "Small Piece of Jewelry Worth 10 gp from " + Origin, "5 gp"])
    
if Background == "Folk Hero":
    SkillProficiencies.extend(["Animal Handling", "Survival"])
    FolkHeroTools = random.choice(ArtisanTools)
    ToolProficiencies.extend([FolkHeroTools, "Land Vehicles"])
    Equipment.extend([FolkHeroTools, "Shovel", "Iron Pot", "Set of Common Clothes", "10 gp"])
    
if Background == "Gate Urchin":
    SkillProficiencies.extend(["Deception", "Sleight of Hand"])
    GateUrchinMusicalInstrument = random.choice(MusicalInstruments)
    ToolProficiencies.extend(["Thieves' Tools", GateUrchinMusicalInstrument])
    Equipment.extend(["Battered Alms Box", GateUrchinMusicalInstrument, random.choice(["Cast-Off Military Jacket", "Cast-Off Cap", "Cast-Off Scarf"]), "Set of Common Clothes", "10 gp"])
    
if Background == "Guild Artisan":
    SkillProficiencies.extend(["Insight", "Persuasion"])
    GuildArtisanTools = random.choice(ArtisanTools)
    ToolProficiencies.extend([GuildArtisanTools])
    Equipment.extend([GuildArtisanTools, "Letter of Introduction from Your Guild", "15 gp"])
    
if Background == "Harborfolk":
    SkillProficiencies.extend(["Athletics", "Sleight of Hand"])
    HarborfolkGamingSet = random.choice(GamingSets)
    ToolProficiencies.extend([HarborfolkGamingSet, "Water Vehicles"])
    Equipment.extend([HarborfolkGamingSet, "Fishing Tackle", "Set of Common Clothes", "Rowboat", "5 gp"])
    
if Background == "Haunted One":
    SkillProficiencies.extend(random.choice(["Arcana", "Investigation", "Religion", "Survival"]))
    Equipment.extend(["Monster Hunter's Pack", "Gothic Trinket"])

if Background == "Hermit":
    SkillProficiencies.extend(["Medicine", "Religion"])
    ToolProficiencies.extend(["Herbalism Kit"])
    Equipment.extend(["Scroll Case Stuffed Full of Notes from Your " + random.choice(["Prayers", "Studies"]), "Winter Blanket", "Set of Common Clothes", "Herbalism Kit", "5 gp"])
    
if Background == "Hillsfar Merchant":
    SkillProficiencies.extend(["Insight", "Persuasion"])
    ToolProficiencies.extend(["Land Vehicles", "Water Vehicles"])
    Equipment.extend(["Set of Clothes", "Signet Ring", "Letter of Introduction from Your Family's Trading House", "25 gp"])

if Background == "Hillsfar Smuggler":
    SkillProficiencies.extend(["Perception", "Stealth"])
    ToolProficiencies.extend(["Forgery Kit"])
    Equipment.extend(["Forgery Kit", "Set of Common Clothes", "5 gp"])
    
if Background == "House Agent":
    House = random.choice(["Cannith", "Deneith", "Ghallanda", "Jorasco", "Kundarak", "Lyrandar", "Medani", "Orien", "Phiarlan", "Sivis", "Tharashk", "Thuranni", "Vadalis"])
    Background = "House Agent of the " + House + " House"
    SkillProficiencies.extend(["Investigation", "Persuasion"])
    if House == "Cannith":
        ToolProficiencies.extend(["Alchemist's Supplies", "Tinker's Tools"])
    if House == "Deneith":
        ToolProficiencies.extend([random.choice(GamingSets), "Land Vehicles"])
    if House == "Ghallanda":
        ToolProficiencies.extend(["Brewer's Supplies", "Cook's Utensils"])
    if House == "Jorasco":
        ToolProficiencies.extend(["Alchemist's Supplies", "Herbalism Kit"])
    if House == "Kundarak":
        ToolProficiencies.extend(["Tinker's Tools", "Thieves' Tools"])
    if House == "Lyrandar":
        ToolProficiencies.extend(["Sea Vehicles", "Air Vehicles", "Navigator's Tools"])
    if House == "Medani":
        ToolProficiencies.extend(["Thieves' Tools", "Disguise Kit"])
    if House == "Orien":
        ToolProficiencies.extend(["Land Vehicles", random.choice(GamingSets)])
    if House == "Phiarlan":
        ToolProficiencies.extend(["Disguise Kit", random.choice(MusicalInstruments)])
    if House == "Sivis":
        ToolProficiencies.extend(["Calligrapher's Tools", "Forgery Kit"])
    if House == "Tharashk":
        ToolProficiencies.extend(["Thieve's Tools", random.choice(GamingSets)])
    if House == "Thuranni":
        ToolProficiencies.extend(["Poisoner's Kit", random.choice(GamingSets)])
    if House == "Vadalis":
        ToolProficiencies.extend(["Land Vehicles", "Herbalism Kit"])
    Equipment.extend(["Set of Fine Clothes", House + " Signet Ring", "ID Papers", "20 gp"])
    
if Background == "Inheritor":
    SkillProficiencies.extend(["Survival", random.choice(["Arcana", "History", "Religion"])])
    InheritorTool = random.choice([random.choice(GamingSets), random.choice(MusicalInstruments)])
    ToolProficiencies.extend([InheritorTool])
    Equipment.extend(["Your Inheritance: " + random.choice([random.choice(["A Map", "A Letter", "A Journal"]), "A Trinket", "An Article of Clothing", "A Piece of Jewelry", "An Arcane " + random.choice(["Book", "Formulary"]), "A Written " + random.choice(["Story", "Song", "Poem", "Secret"]), "A Tattoo"]), "Set of Traveler's Clothes", InheritorTool, "15 gp"])
    
if Background == "Initiate":
    SkillProficiencies.extend(["Athletics", "Intimidation"])
    InitiateGamingSet = random.choice(GamingSets)
    ToolProficiencies.extend([InitiateGamingSet, "Land Vehicles"])
    Equipment.extend(["Simple Puzzle Box", "Scroll Containing the Teachings of the Gods", InitiateGamingSet, "Set of Common Clothes", "15 gp"])
    
if Background == "Inquisitor":
    SkillProficiencies.extend(["Investigation", "Religion"])
    ToolProficiencies.extend([random.choice(ArtisanTools), "Thieves' Tools"])
    Equipment.extend(["Holy Symbol", "Set of Traveler's Clothes", "15 gp"])
    
if Background == "Iron Route Bandit":
    SkillProficiencies.extend(["Animal Handling", "Stealth"])
    ToolProficiencies.extend([random.choice(GamingSets), "Land Vehicles"])
    Equipment.extend(["Set of Dark Common Clothes", "Pack Saddle", "Burglar's Pack", "5 gp"])
    
if Background == "Knight of the Order":
    Order = random.choice(["the Unicorn", "Myth Drannor", "the Silver Chalice"])
    Background = "Knight of the Order of " + Order
    SkillProficiencies.extend(["Persuasion"])
    if Order == "the Unicorn":
        SkillProficiencies.extend([random.choice(["Arcana", "Religion"])])
    if Order == "Myth Drannor":
        SkillProficiencies.extend([random.choice(["Nature", "History"])])
    if Order == "the Silver Chalice":
        SkillProficiencies.extend([random.choice(["History", "Religion"])])
    ToolProficiencies.extend([random.choice([random.choice(GamingSets), random.choice(MusicalInstruments)])])
    Equipment.extend(["Set of Traveler's Clothes", random.choice(["Signet", "Banner", "Seal"]) + " Representing Your Rank in the Order of " + Order, "10 gp"])
    
if Background == "Mercenary Veteran":
    Company = random.choice(["The Chill", "Silent Rain", "The Bloodaxes"])
    Background = "Mercenary Veteran from " + Company
    SkillProficiencies.extend(["Athletics", "Persuasion"])
    MercenaryVeteranGamingSet = random.choice(GamingSets)
    ToolProficiencies.extend([MercenaryVeteranGamingSet, "Land Vehicles"])
    Equipment.extend(["Uniform from " + Company, "Insignia of Your Rank from " + Company, MercenaryVeteranGamingSet, "10 gp"])
    
if Background == "Mulmaster Aristocrat":
    SkillProficiencies.extend(["Deception", "Performance"])
    MulmasterAristocratArtisanTool = random.choice(ArtisanTools)
    MulmasterAristocratMusicalInstrument = random.choice(MusicalInstruments)
    ToolProficiencies.extend([MulmasterAristocratArtisanTool, MulmasterAristocratMusicalInstrument])
    Equipment.extend([random.choice([MulmasterAristocratArtisanTool, MulmasterAristocratMusicalInstrument]), "Set of Fine Clothes", "10 gp"])
    
if Background == "Noble":
    SkillProficiencies.extend(["History", "Persuasion"])
    ToolProficiencies.extend([random.choice(GamingSets)])
    Equipment.extend(["Set of Fine Clothes", "Signet Ring", "Scroll of Pedigree", "25 gp"])
    
if Background == "Outlander":
    Origin = random.choice(["Forester", "Trapper", "Homesteader", "Guide", "Exile", "Outcast", "Bounty Hunter", "Pilgrim", "Tribal Nomad", "Hunter-Gatherer", "Tribal Marauder"])
    Background = "Outlander " + Origin
    SkillProficiencies.extend(["Athletics", "Survival"])
    ToolProficiencies.extend([random.choice(MusicalInstruments)])
    Equipment.extend(["Staff", "Hunting Trap", "Trophy from an Animal You Killed", "Set of Traveler's Clothes", "10 gp"])
    
if Background == "Phlan Insurgent":
    SkillProficiencies.extend(["Stealth", "Survival"])
    ToolProficiencies.extend([random.choice(ArtisanTools), "Land Vehicles"])
    Equipment.extend(["Bag of 20 Caltrops", "Small Trinket from Your Home", "Healer's Kit", "Set of Dark Common Clothes", "5 gp"])

if Background == "Phlan Refugee":
    SkillProficiencies.extend(["Athletics", "Insight"])
    PhlanRefugeeTool = random.choice(ArtisanTools)
    ToolProficiencies.extend([PhlanRefugeeTool])
    Equipment.extend([PhlanRefugeeTool, "Token from Home", "Set of Traveler's Clothes", "15 gp"])
    
if Background == "Sage":
    Specialty = random.choice(["Alchemist", "Astronomer", "Discredited Academic", "Librarian", "Professor", "Researcher", "Wizard's Apprentice", "Scribe"])
    Background = "Sage " + Specialty
    SkillProficiencies.extend(["Arcana", "History"])
    Equipment.extend(["Bottle of Black Ink", "Quill", "Small Knife", "Letter from a Dead Colleague Posing a Question You Cannot yet Answer", "Set of Common Clothes", "10 gp"])
    
if Background == "Sailor":
    SkillProficiencies.extend(["Athletics", "Perception"])
    ToolProficiencies.extend(["Navigator's Tools", "Water Vehicles"])
    Equipment.extend(["Belaying Pin (Club)", "50 ft of Silk Rope", "Lucky Charm (Trinket)", "Set of Common Clothes", "10 gp"])
    
if Background == "Secret Identity": # Has to be non human
    SkillProficiencies.extend(["Deception", "Stealth"])
    ToolProficiencies.extend(["Disguise Kit", "Forgery Kit"])
    Equipment.extend(["Disguise Kit", "Forgery Kit", "Set of Common Clothes", "5 gp"])
    
if Background == "Shade Fanatic":
    SkillProficiencies.extend(["Deception", "Intimidation"])
    ToolProficiencies.extend(["Forgery Kit"])
    Equipment.extend(["Forgery Kit", "Transparent Cylinder of Shadow that has no Opening", "Signet Ring", "Set of Fine Clothes", "15 gp"])
    
if Background == "Soldier":
    Specialty = random.choice(["Officer", "Scout", "Infantry", "Cavalry", "Healer", "Quartermaster", "Standard Bearer", "Support Staff"])
    Background = "Soldier " + Specialty
    SkillProficiencies.extend(["Athletics", "Intimidation"])
    ToolProficiencies.extend([random.choice(GamingSets), "Land Vehicles"])
    Equipment.extend(["Insignia of Rank", "Trophy Taken from a Fallen Enemy", random.choice(["Bond Dice Set", "Playing Card Set"]), "Set of Common Clothes", "10 gp"])
    
if Background == "Stojanow Prisoner":
    SkillProficiencies.extend(["Deception", "Perception"])
    ToolProficiencies.extend([random.choice(GamingSets), "Thieves' Tools"])
    Equipment.extend(["Small Knife", "Set of Common Clothes", "Trinket from Home", "10 gp"])
    
if Background == "Ticklebelly Nomad":
    SkillProficiencies.extend(["Animal Handling", "Nature"])
    ToolProficiencies.extend(["Herbalism Kit"])
    Equipment.extend(["Herbalism Kit", "Small Article of Jewelry Distinct to Your Tribe", "Hunting Trap", "Set of Common Clothes", "5 gp"])
    
if Background == "Trade Sheriff":
    SkillProficiencies.extend(["Investigation", "Persuasion"])
    ToolProficiencies.extend(["Thieves' Tools"])
    Equipment.extend(["Thieves' Kit", "Gray Cloak", "Sherrif's Insignia", "Set of Fine Clothes", "17 gp"])
    
if Background == "Urban Bounty Hunter":
    SkillProficiencies.extend(random.sample(["Deception", "Insight", "Persuasion", "Stealth"], 2))
    ToolProficiencies.extend(random.sample([random.choice(GamingSets), random.choice(MusicalInstruments), "Theives' Tools"],2))
    Equipment.extend([random.choice(["Set of Common Clothes", "Set of Traveler's Clothes", "Set of Fine Clothes"]), "20 gp"])
    
if Background == "Urchin":
    SkillProficiencies.extend(["Sleight of Hand", "Stealth"])
    ToolProficiencies.extend(["Disguise Kit", "Thieve's Tools"])
    Equipment.extend(["Small Knife", "Map of Your Home City", "Pet Mouse", "Token to Remember Your Parents", "Set of Common Clothes", "10 gp"])
    
if Background == "Uthgardt Tribe Member":
    SkillProficiencies.extend(["Athletics", "Survival"])
    ToolProficiencies.extend([random.choice([random.choice(ArtisanTools), random.choice(MusicalInstruments)])])
    Equipment.extend(["Hunting Trap", random.choice(["Totemic Token", "Set of Tattoos"]) + " Marking Your Loyalty to Uthgar", "Set of Traveler's Clothes", "10 gp"])
    
if Background == "Vizier":
    SkillProficiencies.extend(["History", "Religion"])
    VizierArtisanTool = random.choice(ArtisanTools)
    VizierMusicalInstrument = random.choice(MusicalInstruments)
    ToolProficiencies.extend([VizierArtisanTool, VizierMusicalInstrument])
    Equipment.extend([random.choice([VizierArtisanTool, VizierMusicalInstrument]), "Scroll of Your God's Teachings", "Vizier's Cartouche", "Set of Fine Clothes", "25 gp"])
    
if Background == "Waterdhavian Noble":
    SkillProficiencies.extend(["History", "Persuasion"])
    ToolProficiencies.extend([random.choice([random.choice(GamingSets), random.choice(MusicalInstruments)])])
    Equipment.extend(["Set of Fine Clothes", random.choice(["Signet Ring", "Brooch"]), "Scroll of Pedigree", "Skin of Fine " + random.choice(["Zzar", "Wine"]), "25 gp"])

Alignment = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "True Neutral", "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil"]
Alignment = random.choice(Alignment)

SkillExpertises = [item for item, count in collections.Counter(SkillProficiencies).items() if count > 1] # I included this so if you get the same skill proficiency from two different sources, it becomes an expertise (it's pretty darn rare)
ToolExpertises = [item for item, count in collections.Counter(ToolProficiencies).items() if count > 1] # You can delete these two rows if you don't want innate expertises

print("Race:", Race)
if Subrace != "N/A":
    print("Subrace:", Subrace)
print("Class:", Class)
if Subclass != "N/A":
    print("Sub-Class:", Subclass)
if FightingStyle != "N/A":
    print("Fighting Style:", FightingStyle)
print("Level:", Level)
print("Alignment:", Alignment)
print("Background:", Background)
print("STR ", STR, " STRMOD: ", STRMOD)
print("DEX ", DEX, " DEXMOD: ", DEXMOD)
print("CON ", CON, " CONMOD: ", CONMOD)
print("INT ", INT, " INTMOD: ", INTMOD)
print("WIS ", WIS, " WISMOD: ", WISMOD)
print("CHA ", CHA, " CHAMOD: ", CHAMOD)
print("Hit Points: ", HP)
if Race == "Dwarf":
    print("Speed:", Speed, "Feet (Your Speed is not Reduced by Wearing Heavy Armour)")
else:
    print("Speed:", Speed, "Feet")
if ArmourProficiencies != []:
    print("Armour Proficiencies:", ", ".join(sorted(RemoveDuplicates(ArmourProficiencies))))
if WeaponProficiencies != []:
    print("Weapon Proficienceis:", ", ".join(sorted(RemoveDuplicates(WeaponProficiencies))))
if ToolProficiencies != []:
    print("Tool Proficiencies:", ", ".join(sorted(RemoveDuplicates(ToolProficiencies))))
if ToolExpertises != []:
    print ("Tool Expertises: ", ", ".join(sorted(RemoveDuplicates(ToolExpertises))))
if SavingThrowProficiencies != []:
    print("Saving Throw Proficiencies:", ", ".join(sorted(RemoveDuplicates(SavingThrowProficiencies))))
if SkillProficiencies != []:
    print("Skill Proficiencies:", ", ".join(sorted(RemoveDuplicates(SkillProficiencies))))
if SkillExpertises != []:
    print ("Skill Expertises: ", ", ".join(sorted(RemoveDuplicates(SkillExpertises))))
if Resistances != []:
    print("Resistances:", ", ".join(sorted(RemoveDuplicates(Resistances))))
if Immunities != []:
    print("Immunities:", ", ".join(sorted(RemoveDuplicates(Immunities))))
if Vulnerabilities != []:
    print("Vulnerabilities:", ", ".join(sorted(RemoveDuplicates(Vulnerabilities))))
if Traits != []:
    print("Traits:", ", ".join(sorted(RemoveDuplicates(Traits))))
if Equipment != []:
    print("Equipment and Weapons:", ", ".join(sorted(RemoveDuplicates(Equipment))))
if Age != "N/A":
    print("Age:", Age, "Years")
else:
    print("Age: N/A")
print("Height: ", (Height//12), "' ", Height%12, '"', sep='')
print("Weight:", Weight, "Pounds")
print("Eye Colour:", Eyes)
print("Skin Colour:", Skin)
print("Hair Colour:", Hair)