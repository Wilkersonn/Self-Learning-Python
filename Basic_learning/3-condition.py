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
# Comparison operator  ➔ == (equal to)
#                      ➔ != (different to)
#                      ➔ < (smaller than)
#                      ➔ > (bigger than)
#                      ➔ <= (smaller or equal to)
#                      ➔ => (bigger or equal to)
#                         allows comparisons between two or more values
# -----------------------------------------------------
# multiple condition   ➔ and
#                      ➔ or
#                      ➔ int / not in
# -----------------------------------------------------
# condition keyword    ➔ if
#                      ➔ elif (otherwise if) (elseif)
#                      ➔ else
# -----------------------------------------------------
# boolean value       ➔ if

# here a basic fake connection to a site

id = "Wilkerson"
password = "helloworld123"

print("Connection Interface")

user_id = input("Enter your ID : ")
user_password = input("Enter your password : ")

print("You are connected, welcome", user_id)

# imagine i want to verify the connection i can use comparison operator

id2 = "Wilkerson"
password2 = "helloworld123"

print("Connection Interface")

user_id2 = input("Enter your ID : ")
user_password2 = input("Enter your password : ")

# everything after ":" in a condition must have a tab to be counted as IN the condition.

if user_id2 == id2 and user_password2 == password2:
	print("You are connected, welcome", user_id2)

# -----------------------------------------------------	
# more info for int    ➔ in this exemple, if the var
#                         letter is IN aeiouy the condition
#                         continue
# -----------------------------------------------------	

letter = "b"

if letter in "aeiouy":
	print("It's a vowel")

if letter not in "aeiouy":
	print("It's not a vowel")

# to avoid multiple conditions on the same variable we can use condition keyword

letter2 = "b"

if letter2 in "aeiouy":
	print("It's a vowel")
else: # no need condition after else so always put a : after else
	print("It's not a vowel")

# condition keyword

age = 24

if age == 18:
	print("You're over 18")
elif age == 50:
	print("Your old ! (50)")
elif age == 55:
	print("Your old ! (55)")
else:
	print("You have", age, "Year Old")

# boolean value

game_load = True # true = 1

if game_load: # if gameload = 1 print 'working' else 'dont work'
	print("The game is working")
else:
	print("The game dont work")

# In this code, the condition may be too long

old = input("How old are you ? ")
old = int(old)

if old > 0 and age <= 100: # omfg too long
	print("You are between 0 and 100")
else:
	print("Your are older than 100 or younger than 0")

# we can use fork

old2 = input("How old are you ? ")
old2 = int(old)

if 0 < old <= 100: # fork
	print("You are between 0 and 100")
else:
	print("Your are older than 100 or younger than 0")
