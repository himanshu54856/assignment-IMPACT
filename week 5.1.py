#exception in python is to disturb the execution of program while error are those which can stop the execution of program.
#If exception is not handled then the finnaly block can be execute always.
#try and except block can be used to catch and handle statemant.
try:
    10/0
except ZeroDivisionError:
    print("no output")


try:
    10/0
except ZeroDivisionError:
    print("no output")
else:
    print("output")
finally:
    print("good code")               


#custom exception can be used to code much more readble and reduce the amount of code you write and also providr the flexibility to add attributes .
class InvalidAgeException(Exception):
    pass
number=18
try:
    input_num=int(input("enter the number"))
    if input_num<number:
        raise InvalidAgeException
    else:
        print("eligble to vote")
except InvalidAgeException:
    print("exception occured:Invalid Age")                   