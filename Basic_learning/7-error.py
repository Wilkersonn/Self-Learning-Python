#coding:utf-8

# ▄▄▌ ▐ ▄▌▪  ▄▄▌  ▄ •▄ ▄▄▄ .▄▄▄  .▄▄ ·        ▐ ▄ 
# ██· █▌▐███ ██•  █▌▄▌▪▀▄.▀·▀▄ █·▐█ ▀. ▪     •█▌▐█
# ██▪▐█▐▐▌▐█·██▪  ▐▀▀▄·▐▀▀▪▄▐▀▀▄ ▄▀▀▀█▄ ▄█▀▄ ▐█▐▐▌
# ▐█▌██▐█▌▐█▌▐█▌▐▌▐█.█▌▐█▄▄▌▐█•█▌▐█▄▪▐█▐█▌.▐▌██▐█▌
#  ▀▀▀▀ ▀▪▀▀▀.▀▀▀ ·▀  ▀ ▀▀▀ .▀  ▀ ▀▀▀▀  ▀█▄▀▪▀▀ █▪

# ┌────────────────────────────────────────┐
# │                  Info                  │
# └────────────────────────────────────────┘
# errors               ➔ try - try a code 
#                      ➔ except - what the code do if try return 0 (dont work)
#                      ➔ You can use else after except to put what the code do if the try return 1 (work)
#                      ➔ finally - Is executed a the very end of a try, so whatever the result is, finally gonna be executed 
#                      ➔ Raise - Manually triggers a specified exception when a certain condition is met.
# -----------------------------------------------------
# Type of exception    ➔ ValueError - Raised when a function receives an argument of the right type but an inappropriate value.
#                      ➔ NameError - Occurs when a variable or function name is not found.
#                      ➔ TypeError - Happens when an operation is applied to an object of inappropriate type.
#                      ➔ ZeroDivisionError - Raised when dividing a number by zero.
#                      ➔ OSError - Related to system errors, like file not found.
#                      ➔ AssertionError - Triggered when an "assert" statement fails, indicating a condition is not met. 
#                         assert statement is to verify if a condition is true, if its false then there is a "AssertionError"
#                         For example, if a function assumes a variable is always positive, you can use assert to check this. 
#                         If the variable isn't positive, an AssertionError is raised.


# here, if the use type something else than a int, thecode return an "unreadable" error for the user.
UserAge = input("How Old Are You ? : ")
UserAge = int(UserAge)

print("You have", UserAge, "Year Old")


# here how to handle with this

UserAge2 = input("How Old Are You ? : ")
try:
    UserAge2 = int(UserAge2)
    print("You have", UserAge2, "Year Old")
except:
    print("Use number only !")


# better one

UserAge3 = input("How Old Are You ? : ")
try:
    UserAge3 = int(UserAge3)
except:
    print("Use number only !")
else:
    print("You have", UserAge3, "Year Old")
finally:
    print("end of prog")

# type of exception

number1 = 150
number2 = input("Choose a number to divi : ")

try:
    number2 = int(number2)
    print("Result = {}".format(number1 / number2))
except ValueError:
    print("Pleaser enther number ONLY")
except ZeroDivisionError:
    print("You cant divide by zero")
except:
    print("An error has occured")
else:
    print("Thanks god you enter a correct value")
finally:
    print("End of prog")


# raise exemple. In this program, if are younger than 21, we raise a YoungerThan21Error
class YoungerThan21Error(Exception):
    pass

try:
    age = input("How Old Are You : ")
    age = int(age)
    if age < 21: # "verification", if the user is 21 we raise the error for this case
        raise YoungerThan21Error
except YoungerThan21Error:
    print("Oops ! You are younger than 21.. Kiddo!")

# assertion exemple. ee

try:
    age2 = input("How Old Are You : ")
    age2 = int(age2)

    assert age > 25
except AssertionError:
    print("You are younger ")



