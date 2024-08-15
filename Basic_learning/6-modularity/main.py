#coding:utf-8

# ▄▄▌ ▐ ▄▌▪  ▄▄▌  ▄ •▄ ▄▄▄ .▄▄▄  .▄▄ ·        ▐ ▄ 
# ██· █▌▐███ ██•  █▌▄▌▪▀▄.▀·▀▄ █·▐█ ▀. ▪     •█▌▐█
# ██▪▐█▐▐▌▐█·██▪  ▐▀▀▄·▐▀▀▪▄▐▀▀▄ ▄▀▀▀█▄ ▄█▀▄ ▐█▐▐▌
# ▐█▌██▐█▌▐█▌▐█▌▐▌▐█.█▌▐█▄▄▌▐█•█▌▐█▄▪▐█▐█▌.▐▌██▐█▌
#  ▀▀▀▀ ▀▪▀▀▀.▀▀▀ ·▀  ▀ ▀▀▀ .▀  ▀ ▀▀▀▀  ▀█▄▀▪▀▀ █▪

# ┌────────────────────────────────────────┐
# │                  Info                  │
# └────────────────────────────────────────┘
# Module               ➔ modules are files containing collections of global
#                         variables and functions
#                      ➔ to use it name_of_module.name_of_fonction
#                      ➔ 
# -----------------------------------------------------
# Import module        ➔ import <module_name> - Import everything
#                      ➔ from <module_name> import <fonction_name> - import a single fonction of a module
#                      ➔ from <module_name> import * - import all fonction of a module
                        

import math

result = math.sqrt(100)
print(result)

sinus = math.sin(42)
print(sinus)

# use of player.py 

import includes.player as player

player.bye()

player.speak("Wilkerson", "Hello World!")