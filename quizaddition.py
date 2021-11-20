import random
def add_quiz():

    print("\033[91m\033[1mWELCOME TO CARLITO'S ADDITION QUIZ!\033[0m\033[0m\n")
    name = input("Please enter your \033[4m\033[1mname\033[0m\033[0m to start the game:\n-> ")
    print(f"Hello \033[96m\033[1m{name}\033[0m\033[0m. Let's start the quiz! Good luck and have fun! ")
    rating = 0
    for i in range(10):
        correct = question()
        if correct:
            rating += 1
            print('Your answer is \033[33m\033[1mCorrect\033[0m\033[0m!.')
            print (f"The score you have in the moment is \033[95m\033[1m{rating}\033[0m\033[0m.\n")
        else:
            print('Im sorry to say that your answer is \033[31m\033[1mWrong\033[0m\033[0m.')
            print (f"The score you have in the moment is \033[95m\033[1m{rating}\033[0m\033[0m.\n")
    print (f'Your \033[4maccumulated score\033[0m is \033[95m\033[1m{rating}/10\033[0m\033[0m.\n\n\n')
    print('\033[1m+++++PROGRAM FINISHED++++++\033[0m')

def question():
    answer = additioncalcu()
    predicted = float(input())
    return predicted == answer

def additioncalcu():
    num1 = random.randint(0,99)
    num2 = random.randint(0,99)   
    answer = (num1 + num2)
    print(f'What is \033[92m\033[1m{num1}\033[0m\033[0m added to \033[92m\033[1m{num2}\033[0m\033[0m?')
    return answer
    
add_quiz()