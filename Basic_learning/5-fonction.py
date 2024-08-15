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
# fonction alr seen    ➔ print()
#                      ➔ input()
#                      ➔ cast fonction (str, int, bool)
# -----------------------------------------------------
# fonction             ➔ one function = one task at a time
#                      ➔ avoids repeating code



# fonction with no parameters

def say_hello():
    print("Hello everyone!")

say_hello()

# fonction with parameters

def say(name_human, message_human):
    print("{} : {}".format(name_human, message_human))

say("Wilkerson", "Hello everyone!")
say("Jason", "Hello Wilkerson!")

# In the parameters, you can set default values if it's never used.

def say2(name_human2="Stranger", message_human2="No message"):
    print("{} : {}".format(name_human2, message_human2))

say2()
say2("Wilkerson")
say2("Jason", "Hello Wilkerson!")

# It is also possible to set parameters when calling the fonction

def say3(name_human3="Stranger", message_human3="No message", age_human=18):
    print("{} : {} ({} Y.O)".format(name_human3, message_human3, age_human))

say3()
say3("Wilkerson")
say3("Jason", "Hello Wilkerson!")
say3(message_human3="Hello", age_human=28)
say3(message_human3="Wosso foo'!", name_human3="PythonUser", age_human=28)

# * for infinity list of parameters

def show_inv(*list_items):
    for item in list_items:
        print(item)


show_inv("sword")
show_inv("sword", "bow", "gun", "ammo")

# return value (only one return by fonction)

def calcul_value(number1, number2):
    result = number1 + number2 # you can also just return number1 + number2.
    return result

print(calcul_value(5, 16))

# here several possible returns because there is only one possible answer 

def compare_number(n1, n2):
    if n1 > n2:
        return n1
    elif n1 < n2:
        return n2
    else:
        return "EQUALITY!"

# lamba fonction (a fonction that do one thing)

lambdafonction = lambda:print("Hello")

lambdafonction()



