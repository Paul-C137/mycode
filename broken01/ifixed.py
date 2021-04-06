#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.
calc1 = 0.0
calc2 = 0.0
operation = ""
while (calc1 != "q"):
    #print("\nWhat is the first operator? Or, enter q to quit: ")
    calc1 = input("\nWhat is the first operator? Or, enter q to quit: ")
    if calc1 == "Q":
        calc1 = float(calc1)
        print("\nWhat is the second operator? Or, enter q to quit: ")
        calc2 = raw_input()
    elif calc2 == "q":
        calc2 = float(calc2)
        print("Enter an operation to perform on the two operators (+ or -): ")
        operation = raw_input()
    elif operation == "+":
        #print("\n" + str(calc1) " + " + str(calc2) + " = " + str(calc1 + calc2))
        print(f"{calc1} + {calc2} = {calc1+calc2}")
    elif operation == "-":
        #print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
        print(f"{calc1} + {calc2} = {calc1-calc2}")
    else:
        print("\n Not a valid entry. Restarting...")