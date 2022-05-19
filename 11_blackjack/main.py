"""
Capstone Project: BlackJack Console MiniGame

Author: Mateus Cichelero
Date: May 2022
"""

import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play_blackjack():
    """Gameflow function"""
    continue_playing = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()

    # First level gameflow loop, controls new game and restart game scenarios.
    while continue_playing == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)

        your_cards = random.choices(cards, k=2)
        your_score = sum(your_cards)
        pc_cards = random.choices(cards, k=1)

        while sum(pc_cards) < 17:
            pc_cards.append(random.choice(cards))

        pc_score = sum(pc_cards)

        print(f"    Your cards: {your_cards}, current score: {your_score}")
        print(f"    Computer's first card: {pc_cards[0]}")
        another_card = input(
            "Type 'y' to get another card, type 'n' to pass: ").lower()

        # Second level gameflow loop, controls picking new cards until the game
        # is finished
        while (another_card == 'y') and (your_score <= 21):
            your_cards.append(random.choice(cards))
            your_score = sum(your_cards)
            print(f"    Your cards: {your_cards}, current score: {your_score}")
            print(f"    Computer's first card: {pc_cards[0]}")
            if your_score <= 21:
                another_card = input(
                    "Type 'y' to get another card, type 'n' to pass: ").lower()

        # Finished game final scores possibilities:
        if (your_score > 21) and (pc_score <= 21):
            print(
                f"    Your final hand: {your_cards}, final score: {your_score}")
            print(
                f"    Computer's final hand: {pc_cards}, final score: {pc_score}")
            print("You went over. You lose 😭")

        elif (your_score < pc_score) and (pc_score <= 21):
            print(
                f"    Your final hand: {your_cards}, final score: {your_score}")
            print(
                f"    Computer's final hand: {pc_cards}, final score: {pc_score}")
            print("You went over. You lose 😭")


        elif (your_score > 21 and pc_score > 21) or (your_score == pc_score):
            print(
                f"    Your final hand: {your_cards}, final score: {your_score}")
            print(
                f"    Computer's final hand: {pc_cards}, final score: {pc_score}")
            print("It's a draw!. Better luck next time 😑")

        elif (your_score > pc_score) or (pc_score > 21 and your_score <= 21):
            print(
                f"    Your final hand: {your_cards}, final score: {your_score}")
            print(
                f"    Computer's final hand: {pc_cards}, final score: {pc_score}")
            print("You win 😃")

        continue_playing = input(
            "Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()


def main():
    """Main function to play blackjack"""
    play_blackjack()


if __name__ == "__main__":
    main()
