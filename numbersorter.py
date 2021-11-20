#Create a program that ask 4 numbers. 
#Print the 4 numbers from highest to lowest using only if-else statement.

print('Welcome to \033[31m\033[1mCarlito Number Sorter\033[0m\033[0m!')

def high_low(num1, num2, num3, num4):
    if num1 >= num2 and num1 >= num3 and num1 >= num4:
        if num2 >= num3 and num2 >= num4:
            if num3 >= num4:
                ascending_num = [num1 , num2, num3, num4]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
            else:
                ascending_num = [num1 , num2, num4, num3]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
        elif num3 >= num2 and num3 >= num4:
            if num2 >= num4:
                ascending_num = [num1 , num3, num2, num4]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
            else:
                ascending_num = [num1 , num3, num4, num2]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
        elif num4 >= num2 and num4 >= num3:
            if num3 >= num2:
                ascending_num = [num1 , num4, num3, num2]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
            else:
                ascending_num = [num1 , num4, num2, num3]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
    elif num2 >= num1 and num2 >= num3 and num2 >= num4:
        if num3 >= num1 and num3 >= num4:
            if num1 >= num4:
                ascending_num = [num2 , num3, num1, num4]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
            else:
                ascending_num = [num2 , num3, num4, num1]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
        elif num4 >= num3 and num4 >= num1:
            if num3 >= num1:
                ascending_num = [num2 , num4, num3, num1]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
            else:
                ascending_num = [num2 , num4, num3, num1]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
        elif num1 >= num3 and num1 >= num4:
            if num3 >= num4:
                ascending_num = [num2 , num1, num3, num4]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
            else:
                ascending_num = [num2 , num1, num4, num3]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
    elif num3 >= num1 and num3 >= num2 and num3 >= num4:
        if num4 >= num1 and num4 >= num2:
            if num1 >= num2:
                ascending_num = [num3 , num4, num1, num2]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
            else:
                ascending_num = [num3 , num4, num2, num1]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
        elif num1 >= num2 and num1 >= num4:
            if num2 >= num4:
                ascending_num = [num3 , num1, num2, num4]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
            else:
                ascending_num = [num3 , num1, num4, num2]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
        elif num2 >= num1 and num2 >= num4:
            if num1 >= num4:
                ascending_num = [num3 , num2, num1, num4]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
            else:
                ascending_num = [num3 , num2, num1, num4]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
    elif num4 >= num1 and num4 >= num2 and num4 >= num3:
        if num1 >= num2 and num1 >= num3:
            if num2 >= num3:
                ascending_num = [num4 , num1, num2, num3]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
            else:
                ascending_num = [num4 , num1, num3, num2]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
        elif num2 >= num1 and num2 >= num3:
            if num1 >= num3:
                ascending_num = [num4 , num2, num1, num3]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
            else:
                ascending_num = [num4 , num2, num3, num1]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
        elif num3 >= num1 and num3 >= num2:
            if num1 >= num2:
                ascending_num = [num4 , num3, num1, num2]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')
            else:
                ascending_num = [num4 , num3, num2, num1]
                print(f'\033[34m\033[1m\nThe ascending order of the four numbers are : {ascending_num}\n\033[0m\033[0m')

dig1 = float(input("Please Enter your \033[1mFirst Number\033[0m:\n-> "))
dig2 = float(input("\nPlease Enter your \033[1mSecond Number\033[0m:\n-> "))
dig3 = float(input("\nPlease Enter your \033[1mThird Number\033[0m:\n-> "))
dig4 = float(input("\nPlease Enter your \033[1mFourth Number\033[0m:\n-> "))
high_low(dig1, dig2, dig3, dig4)