from game_data import data
import random
from art import logo, vs
import os
# {
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#     },
def get_random_account():
    """Get data from random account"""
    return random.choice(data)
# print(get_random_account())

def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess and returns True if they got it right. Or False if they got it wrong.""" 
    if a_followers > b_followers:
        if guess == "a":
            return True
    elif b_followers > a_followers:
        if guess == "b":
            return False
      
def game():
    print(logo)
    score = 0                       #variable to keep the track of the score
    game_should_continue = True

    while game_should_continue == True:
        account_a = get_random_account()
        account_b = get_random_account()

        if account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        # os.system('cls')
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")
        
game()

    


    

















