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
# loop                 ➔ while
#                      ➔ for
#                      ➔ 
#                      ➔ 
#                      ➔ 
# -----------------------------------------------------
# keyword              ➔ break (break the loop)
#                      ➔ continue (goback to the start of the loop)

# imagin i want to print 5 time "hello world"

print("Hello world")
print("Hello world")
print("Hello world")
print("Hello world")
print("Hello world\n")

# I can use loop

print("With loop")

count = 0
while count < 5:
    print("Hello world")
    count+= 1 # each time count < 5 is verified, count will increment by 1


# infiny loop

continue_game = True
print("")

while continue_game:
    menu = input("> ")

    if menu == "again":
        continue
    elif menu == "quit":
        break # break the loop
    elif menu == "hello":
        print("Hello! type -help for informations")
    else:
        print("command not found")

print("Bye bye!")

# 'for' loop

word = "hello world :)"
for letter in word:
    print(letter)
