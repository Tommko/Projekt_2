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
player_number = ""

introduction = f"""
Hi there!
{lines}
I've generated a random {length_of_number} digit number for you.
Let's play a bulls and cows game.
{lines}
"""

def generate_number():                                             #generate random number
    digit_choices = range(0,10,1)
    numbers = random.sample(digit_choices,length_of_number)
    generated_number = ""
    if numbers[0] == 0:
        numbers = random.sample(digit_choices,length_of_number)
    
    for X in numbers:
        generated_number = generated_number + str(X)
    return generated_number

def number_check(entry):                                           #checking if the input is right
    for number in entry:
        if str(entry).count(number) > 1 or entry.isnumeric() != True or str(entry[0]) == "0"  or len(entry) != length_of_number:
            decision = print("Warning! Number must be length_of_number digits long, can't contain duplicates, letters or start with 0!")
            break
        else:
            decision = entry
            pass
    return decision
                                 
def plural(word,value):                                            #creates plural
    if value == 1:
        pass
    else:
        if word[-1] == "s":
            word = word + "es"
        else:
            word = word + "s"
    return word

def main_function(bulls, cows, counter):                           #main function of the game
    if player_number != computer_number:
        for index, digit in enumerate(player_number, 0):
            if digit == computer_number[index]:
                bulls = bulls + 1
            elif digit in computer_number:
                cows = cows + 1
                    
        print(bulls, plural("bull",bulls), "," , cows, plural("cow",cows))
        print(lines)
            
    else:
        print("You've won! You've made it in", counter ,plural("guess",counter))
    
if __name__ == "__main__":

    computer_number = str(generate_number())

    print(introduction)

    while player_number != computer_number:
        player_number = str(number_check(input("Insert number please: ")))  
            
        bulls = 0
        cows = 0
            
        main_function(bulls,cows,counter)
        counter = counter + 1