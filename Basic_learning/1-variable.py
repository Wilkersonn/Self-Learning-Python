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
# Name a variable      ➔ must start with a letter or _
#                      ➔ No special char.
#                      ➔ no space
#                      ➔ You can use "_" (underscore)
# -----------------------------------------------------
# Here some exemple    ➔ ageHuman (the best)
#                      ➔ age_human
#                      ➔ _agehuman
#                      ➔ Always use in your code the same "style"
#                         do not create a first var name age_human
#                         then a second name AgeDog, use "age_dog"
#                         for a beater readability
# -----------------------------------------------------
# Standard Type        ➔ Integer numeric     (int)
#                      ➔ Floating numbers    (float)
#                      ➔ chains of character (str)
#                      ➔ Booleen (bool)
#                      ➔ and very very more...
# -----------------------------------------------------
# More informations    ➔ Python supports "Dynamic Type"
#                         no need to put "int", "str"
#                         before your variable. Just
#                         make sure you spell it right
#
# age_human = 14       ➔ Here, it will be counted as an "int".

# age_human = "14"     ➔ Here, it will be counted as a "str".
#                      ➔ "But why ?" : Because there is "".
# -----------------------------------------------------


age_human = 14
age_humanstr = "14"
age_humanfloat = 14.3
deadornot_bool = True 

print(type(age_human))
print(type(age_humanstr))

print("I have", age_human, "Year Old")

# -----------------------------------------------------
# Print multiple var   ➔ In a string variable, put "{}"
#                      ➔ Inside, a variable will be displayed.
#                      ➔ Finally use print(NameOfStrVar.format(FirstVarToDisplay, SecondVarToDisplay))



age_of_human = "Human have {} year old, but exatly he have {} year old."
print(age_of_human.format(age_human, age_humanfloat))

# -----------------------------------------------------
# Input Variable       ➔ You can also ask to the "user" of
#                      ➔ your code to put his own information
#                      ➔ in a variable with VariableName = input("Your Text :")
#                      ➔ The variable will be modified dynamically
#                      ➔ according to user input.


NamePlayer = "Wilkerson"

print("Welcome,", NamePlayer)


NamePlayerCustom = input("Choose a name : ")

print("Welcome,", NamePlayerCustom)

# py 1-variable.py to execute the code