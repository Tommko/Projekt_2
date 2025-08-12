"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Tomáš Kolárik
email: kolarik-tomas@seznam.cz
"""
import random

lines = "_"*47

length_of_number = 4
bulls = 0
cows = 0
counter = 1

introduction = f"""
Hi there!
{lines}
I've generated a random {length_of_number} digit number for you.
Let's play a bulls and cows game.
{lines}
"""

# def all_functions():
#     generate_number()
#     check_uniqueness(variable_1)
#     player_number_check()
#     bulls_numnber()
#     cows_number()
#     guesses_number()


def generate_number():                                             #generate random number
    digit_choices = range(0,10,1)
    numbers = random.sample(digit_choices,4)
    generated_number = ""
    if numbers[0] == 0:
        numbers = random.sample(digit_choices,4)
    
    for X in numbers:
        generated_number = generated_number + str(X)
    return generated_number

def check_uniqueness(entry):
    
    for A in entry:
        if str(entry).count(A) > 1:
            uniqueness_help.append(False)
        else:
            uniqueness_help.append(True)
    
    return uniqueness_help

def player_number_check(variable_1):                               #checks if digits in players number are unique
    global uniqueness_help

    uniqueness_help = []

    check_uniqueness(variable_1)  

    if uniqueness_help.count(True) < length_of_number:
        unique_number_output = False
    else:
        unique_number_output = True
        
    X = [len(variable_1) == length_of_number, variable_1.isnumeric(), str(variable_1[0]) != "0", unique_number_output]

    while X.count(True) != length_of_number:
        
        uniqueness_help = []

        variable_1 = input("Warning! Number must be length_of_number digits long, can't contain duplicates, letters or start with 0!: ")
        
        check_uniqueness(variable_1)

        if uniqueness_help.count(True) < length_of_number:
            unique_number_output = False
        else:
            unique_number_output = True
        X = [len(variable_1) == length_of_number, variable_1.isnumeric(), str(variable_1[0]) != "0", unique_number_output]

    return variable_1
                                 
def bulls_numnber(bulls_input):                                    #decision about singular or plural of bulls
    if bulls_input > 1:
        bulls_count = "bulls"
    else:
        bulls_count = "bull"
    return bulls_count

def cows_number(cows_input):                                       #decision about singular or plural of cows
    if cows_input > 1:
        cows_count = "cows"
    else:
        cows_count = "cow"
    return cows_count

def guesses_number(guesses_input):                                 #decision about singular or plural of guesses
    if guesses_input > 1:
        guesses_count = "gueses!"
    else:
        guesses_count = "guess!"
    return guesses_count

def main_function():                                               #main function of the game
    global player_number
    global bulls
    global cows
    global counter
    for i, A in enumerate(player_number, 0):
        if A == computer_number[i]:
            bulls = bulls + 1
        elif A in computer_number:
            cows = cows + 1
        
    print(bulls, bulls_numnber(bulls), "," , cows, cows_number(cows))
    print(lines)
    
    
    if bulls < length_of_number:
        variable_1 = input("Insert number please: ")

        player_number = str(player_number_check(variable_1))
        counter = counter + 1
    
    return bulls, cows, counter

if __name__ == "__main__":

    computer_number = str(generate_number())

    print(introduction)

    variable_1 = input("Insert number please: ")         

    player_number = str(player_number_check(variable_1))  


    while bulls < length_of_number:
        
        bulls = 0
        cows = 0
        
        main_function()
        
    else:
        print("You've won! You've made it in", counter ,guesses_number(counter))
