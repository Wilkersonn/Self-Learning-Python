#coding:utf-8

# ▄▄▌ ▐ ▄▌▪  ▄▄▌  ▄ •▄ ▄▄▄ .▄▄▄  .▄▄ ·        ▐ ▄ 
# ██· █▌▐███ ██•  █▌▄▌▪▀▄.▀·▀▄ █·▐█ ▀. ▪     •█▌▐█
# ██▪▐█▐▐▌▐█·██▪  ▐▀▀▄·▐▀▀▪▄▐▀▀▄ ▄▀▀▀█▄ ▄█▀▄ ▐█▐▐▌
# ▐█▌██▐█▌▐█▌▐█▌▐▌▐█.█▌▐█▄▄▌▐█•█▌▐█▄▪▐█▐█▌.▐▌██▐█▌
#  ▀▀▀▀ ▀▪▀▀▀.▀▀▀ ·▀  ▀ ▀▀▀ .▀  ▀ ▀▀▀▀  ▀█▄▀▪▀▀ █▪

# ┌────────────────────────────────────────┐
# │                  Info                  │
# └────────────────────────────────────────┘
# Module               ➔ player module for main.py
#                      ➔ to use it type : import includes.player
#                      ➔ or import includes.player as player
#                      ➔ if __name__ == "__main__": for testing

def speak(human, message):
    print("{} : {}".format(human, message))

def bye():
    print("Bye !")

if __name__ == "__main__":
    print("TEST PLAYER.PY\n")
    speak("HumanTest", "Test of speak fonction")
    bye()

