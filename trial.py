#print( len( input("What's your name?")))
#print("Hello"[0])

'''two_digit_number = input("Type a two digit number: " )
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
print(first_digit+second_digit)'''






#PEMDASLR





'''height = input("Enter your height in m: ")
weight = input("Enter your weight in Kg: ")
bmi = int(weight) / float(height) ** 2
bmi_int = int(bmi)
print(bmi_int)'''






'''
print(round(8/3))
print(round(8/3,1))
print(round(8/3,2))

print(8//3)
print(type(8//3))'''









'''age = input("What's your current age? ")
age_as_int = int(age)
days_remaining = (90 - age_as_int)*365
weeks_remaining = (90-age_as_int)*52
months_remaining = (90-age_as_int)*12
print(f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months left.")'''








'''print("Welcome to the tip calculator")
bill = int(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
bill_per_person = round((bill*((tip/100)+1))/people,2)
print(f"Each person should pay {bill_per_person}")'''










'''
print("Welcome to Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your name? \n")
combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true_score = t+r+u+e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love_score = l+o+v+e

Total_Score = int(str(true_score) + str(love_score))

if  Total_Score < 10 or Total_Score > 90:
    print(f"Your score is {Total_Score}, you go together like coke and mentos.")
elif Total_Score >= 40 and Total_Score <= 50:
    print(f"Your score is {Total_Score}, you are alright together.")
else:
    print(f"Your score is {Total_Score}") '''





 
'''
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
choice1 = input('You\'re at crossroad, where do you want to go? Type "left" or "right". ').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    if choice2 == "wait":
        choice3 = input("You arrived at the island unharmed. There is a house with 3 doors. One Red, one yellow and one blue. Which color do you choose? ").lower()
        if choice3 == "red":
            print("The room is full of deomons from hell. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("The room is full of ice age monsters. Game Over")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
'''




'''import random

random_integer = random.randint(100,200)
print(random_integer)'''   

'''import my_module
print(my_module.pi)'''

'''random_float = random.random() # getting decimals from  0 to 0.9999999...
print(random_float)

random_float * 5
# now the range can be 0.0000... to 4.9999.....

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")'''







'''import random 

random_side = random.randint(0,1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")'''




'''
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", 
                     "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina",
                       "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
                         "Illinois", "Alabama", "Maine"]

print(states_of_america[10])

states_of_america[1] = "pencilwanya"

states_of_america.append('"Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"')

states_of_america.extend(["KrishnaLand", "KatiyarLand"])

print(states_of_america)'''



'''
import random
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

#num_items = len(names)
#random_choice = random.randint(0, num_items-1)
#person_who_will_pay = names[random_choice]

person_who_will_pay = random.choice(names)

print(person_who_will_pay + " is going to buy the meal today!")'''



'''
fruits = ["mango", "strawberry", "banana"]
vegetables = ["spinach", "tomatoes", "celery"]
dirty_halfdozen = [fruits, vegetables]
print(dirty_halfdozen)'''






'''
row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")'''






'''
students_heights = input("Input a list of students heights ").split()
for n in range(0,len(students_heights)):
    students_heights[n] = int(students_heights[n])
print(students_heights)

# or total_height = sum(students_heights)
total_height = 0
for height in students_heights:
    total_height += height
print(total_height)

number_of_students = len(students_heights)
average_height = round(total_height / number_of_students)
print(average_height)'''










'''
students_score = [54, 67, 89, 44, 65, 85, 91]

highest_score = 0

for score in students_score:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is {highest_score}")
'''



'''
total = 0
for number in range(0,101,2):
    total += number
print(total)

total2 = 0
for number in range(0,101):
    if number % 2 == 0:
        total2 += number
print(total2)'''




'''
for number in range(1,101):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)'''






'''
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")
nr_letters = int(input("How many letters you want in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))'''

'''
password = ""

for char in range(1, nr_letters + 1):
     password += random.choice(letters)
for char in range(1, nr_symbols + 1):
     password += random.choice(symbols)
for char in range(1, nr_numbers + 1):
     password += random.choice(numbers)

print(password)'''

'''
password_list = []
for char in range(1, nr_letters + 1):
     password_list += random.choice(letters)
for char in range(1, nr_symbols + 1):
     password_list += random.choice(symbols)
for char in range(1, nr_numbers + 1):
     password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""

for char in password_list:
     password += char
print(password)
'''

















'''
import my_module

import random

print(my_module.logo)'''


'''
end_of_game = False
word_list = ["advark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)

lives = 6



display = []
word_length = len(chosen_word)
for _ in range(len(chosen_word)):
    display += "_"




while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    print(stages[lives])
'''














'''
student_scores = {"Harry": 81, "Ron": 78, "Hermione": 99, "Draco": "74", "Neville": 62}

students_grades = {}

for student in student_scores:
    score = int(student_scores[student])
    if score > 90:
        students_grades[student] = "Outstanding"
    elif score > 80:
        students_grades[student] = "Exceeds Expectations"
    elif score > 70:
        students_grades[student] = "Acceptable"
    else:
        students_grades[student] = "Fail"
print(students_grades)
'''















'''
#Nesting Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited":["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5} 
}

#Nesting Dictionary in a list
travel_log = [
     {"Country": "France",
       "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
        },
     {"Country": "Germany",
       "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
        } 
]

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["country"] = times_visited
    new_country["country"] = cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "St. Petersburg"])
print(travel_log)'''















'''
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        import os
        os.system('clear')
'''












'''
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap")
    else:
        print("Leap Year")
else:
    print("Not Leap")'''










'''
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid Month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)'''



















#Docstring
'''
def format_name(f_name, l_name):
    #Docstring
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

format_name()'''














'''
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    num1 = float(input("What's the first number? "))
    num2 = float(input("What's the second number? "))

    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue with the {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
        operation_symbol = input("Pick another operation: ")
        num3 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        second_answer = calculation_function(calculation_function(num1, num2), num3)
        print(f"{answer} {operation_symbol} {num3} = {second_answer}")

calculator()'''














'''
import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose!"
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current_score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")
            
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else: 
            user_should_deal= input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card)
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        print(f"    Your final hand: {user_cards}, final_score: {user_score}")
        print(f"    Computer's final hand: {computer_cards}, final_score: {computer_score}")
        print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
'''









# import random
# def deal_card():
#   """Returns a random card from the deck."""
#   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#   card = random.choice(cards)
#   return card

# def calculate_score(cards):
#   """Take a list of cards and return the score calculated from the cards"""
#   if sum(cards) == 21 and len(cards) == 2:
#     return 0
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#   return sum(cards)

# def compare(user_score, computer_score):
#   if user_score > 21 and computer_score > 21:
#     return "You went over. You lose 😤"
#     if user_score == computer_score:
#         return "Draw 🙃"
#   elif computer_score == 0:
#     return "Lose, opponent has Blackjack 😱"
#   elif user_score == 0:
#     return "Win with a Blackjack 😎"
#   elif user_score > 21:
#     return "You went over. You lose 😭"
#   elif computer_score > 21:
#     return "Opponent went over. You win 😁"
#   elif user_score > computer_score:
#     return "You win 😃"
#   else:
#     return "You lose 😤"

# def play_game():
#   user_cards = []
#   computer_cards = []
#   is_game_over = False
#   for _ in range(2):
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())
#     while not is_game_over:
#       user_score = calculate_score(user_cards)
#     computer_score = calculate_score(computer_cards)
#     print(f"   Your cards: {user_cards}, current score: {user_score}")
#     print(f"   Computer's first card: {computer_cards[0]}")

#     if user_score == 0 or computer_score == 0 or user_score > 21:
#       is_game_over = True
#     else:
#        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#        if user_should_deal == "y":
#         user_cards.append(deal_card())
#        else:
#         is_game_over = True
#     while computer_score != 0 and computer_score < 17:
#         computer_cards.append(deal_card())
#         computer_score = calculate_score(computer_cards)

#     print(f"   Your final hand: {user_cards}, final score: {user_score}")
#     print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
#     print(compare(user_score, computer_score))


# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#   play_game()



