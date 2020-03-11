weaponStats = {"baseDamage":100,
               "multishot":1.9,
               "criticalChance":0.75,
               "criticalMultiplier":4.4,
               "statusChance":0.5,
               "impactDamage":20,
               "punctureDamage":40,
               "slashDamage":40,
               "toxinDamage":0,
               "heatDamage":0,
               "electricityDamage":0,
               "coldDamage":0,
               "corrosiveDamage":150,
               "blastDamage":0,
               "radiationDamage":0,
               "viralDamage":0,
               "gasDamage":0,
               "magneticDamage":0,
               "heatModifier":0,
               "toxinModifier":0,
               "electricityModifier":0,
               "fireRate":10.00,
               "magazineCapacity":100,
               "reload":2.0}

enemyStats = {"health":10000,
              "armor":1000,
              "shields":2500,
              "healthType":"clonedFlesh",
              "armorType":"ferriteArmor",
              "shieldsType":"standardShields"}

timePassed = 0.0
timeUntilNextShot = 0.0
timeUntilNextStatus = 0.0

def FireShot():
    return

def SlashTick():
    return

def ToxinTick():
    return

def HeatTick():
    return

def ElectricityTick():
    return

def CorrosiveExpire():
    return

def ViralExpire():
    return

def MagneticExpire():
    return

FireShot()
while(enemyStats["health"]>0):
    enemyStats["health"] -= 499
    print(enemyStats["health"])
    

print(weaponStats)
print(enemyStats)
