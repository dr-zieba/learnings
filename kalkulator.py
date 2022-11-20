import math

while True:
    print("Choose operation\n\n0 - Addition\n1 - Substract\n2 - Multiplication\n3 - Division\n4 - Modula\n5 - Raising to power\n6 - Square root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n\n")

    user_input = input("Choose option: ")

    #addition
    if user_input == "0":
        first_number = input("Type first number: ")
        second_number = input("Type second number ")
        result = float(first_number) + float(second_number)
        print(f"Math operation: {first_number} + {second_number} = {result}\n")

        back = input("Go back to main menu?(y/n)")

        if back == "y":
            continue
        else:
            break
        
    #Substraction
    elif user_input == "1":
        first_number = input("Type first number: ")
        second_number = input("Type second number ")
        result = float(first_number) - float(second_number)
        print(f"Math operation: {first_number} - {second_number} = {result}\n")

        back = input("Go back to main menu?(y/n)")

        if back == "y":
            continue
        else:
            break

    #Multiplication
    elif user_input == "2":
        first_number = input("Type first number: ")
        second_number = input("Type second number ")
        result = float(first_number) * float(second_number)
        print(f"Math operation: {first_number} * {second_number} = {result}\n")

        back = input("Go back to main menu?(y/n)")

        if back == "y":
            continue
        else:
            break

    #Division
    elif user_input == "3":
        first_number = input("Type first number: ")
        second_number = input("Type second number ")
        result = float(first_number) / float(second_number)
        print(f"Math operation: {first_number} / {second_number} = {result}\n")

        back = input("Go back to main menu?(y/n)")

        if back == "y":
            continue
        else:
            break
