#coding:utf-8

# ▄▄▌ ▐ ▄▌▪  ▄▄▌  ▄ •▄ ▄▄▄ .▄▄▄  .▄▄ ·        ▐ ▄ 
# ██· █▌▐███ ██•  █▌▄▌▪▀▄.▀·▀▄ █·▐█ ▀. ▪     •█▌▐█
# ██▪▐█▐▐▌▐█·██▪  ▐▀▀▄·▐▀▀▪▄▐▀▀▄ ▄▀▀▀█▄ ▄█▀▄ ▐█▐▐▌
# ▐█▌██▐█▌▐█▌▐█▌▐▌▐█.█▌▐█▄▄▌▐█•█▌▐█▄▪▐█▐█▌.▐▌██▐█▌
#  ▀▀▀▀ ▀▪▀▀▀.▀▀▀ ·▀  ▀ ▀▀▀ .▀  ▀ ▀▀▀▀  ▀█▄▀▪▀▀ █▪

# ┌────────────────────────────────────────┐
# │                  Info                  │
# └────────────────────────────────────────┘
#
# Operator in py       ➔ + (addition)
#                      ➔ - (subtraction)
#                      ➔ * (multiplication)
#                      ➔ / (division)
#                      ➔ % (Modulo)
#                         Rest of a division
# -----------------------------------------------------

# exemple of modulo
calculation = 5 / 2
calculation = int(calculation)

print("Result int =", calculation)

# the result of 5 / 2 on an integer is 2
# This leaves 0.5 twice (because divided by 2), so adding them together makes 1. 5 % 2 = 1

modulo = 5 % 2
modulo = int(modulo)

print("Result modulo =", modulo)

# Manual addition for level or else (bad)
LVL = 1
print("Level :", LVL)

print("You win x1 Battle, you gain 2LVL")

LVL = 3
print("Level :", LVL)

# Automatic addition for level or else (cool)

LVL2 = 1
print("\nLevel :", LVL2)

print("You win x1 Battle, you gain 2LVL")

LVL2 = LVL2 + 2 # you can also do : LVL2 += 2
print("Level :", LVL2)



# py 1-operator.py to execute the code