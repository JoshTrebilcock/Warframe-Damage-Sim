import math
import random

weaponStats = {"baseDamage":100,
               "multishot":1.9,
               "criticalChance":0.75,
               "criticalMultiplier":4.4,
               "statusChance":0.5,
               "statusDuration":1,
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

weaponDamageValues = {"impact":20,
                      "puncture":40,
                      "slash":40,
                      "corrosive":150,}

enemyStats = {"health":10000,
              "armor":1000,
              "shields":2500,
              "healthType":"clonedFlesh",
              "armorType":"ferriteArmor",
              "shieldsType":"normalShields"}

healthTypes = {"clonedFlesh":{"impact":0.75,"puncture":1,"slash":1.25,"toxin":1,"heat":1.25,"electricity":1,"cold":1,"corrosive":1,"blast":1,"radiation":1,"viral":1.75,"gas":0.5,"magnetic":1}}

shieldTypes = {"normalShields":{"impact":1.5,"puncture":0.8,"slash":1,"toxin":1,"heat":1,"electricity":1,"cold":1.5,"corrosive":1,"blast":1,"radiation":0.75,"viral":1,"gas":1,"magnetic":1.75}}

armorTypes = {"ferriteArmor":{"impact":1,"puncture":1.5,"slash":0.85,"toxin":1,"heat":1,"electricity":1,"cold":1,"corrosive":1.75,"blast":0.75,"radiation":1,"viral":1.75,"gas":0.5,"magnetic":1}}

timePassed = 0.0
timeUntilNextShot = 0.0
timeUntilNextStatusTick = 0.0

"""timeUntilNextToxinTick = 0.0
timeUntilNextHeatTick = 0.0
timeUntilNextGasTick = 999.0
timeUntilNextElectricityTick = 0.0
timeUntilNextCorrosiveExpiry = 0.0
timeUntilNextViralExpiry = 0.0
timeUntilNextMagneticExpiry = 0.0"""

def FireShot():
    totalDamage = 0
    if (enemyStats["shields"] > 0):
        for damageType in weaponDamageValues:
            totalDamage += (weaponDamageValues[damageType]*shieldTypes[enemyStats["shieldsType"]][damageType])
    return

def rollMultishot():
    return

def rollCrit():
    critTier = math.floor(weaponStats["criticalChance"])
    return

def rollStatus():
    return

def StatusTick():
    return

def SlashTick():
    return

def ToxinTick():
    return

def HeatTick():
    return

def GasTick():
    return

def ElectricityTick():
    return

def CorrosiveExpiry():
    return

def ViralExpiry():
    return

def MagneticExpiry():
    return

FireShot()
