from random import randint
import time


def main():
    player_hand, computer_hand = setup_game()

    player_under_22 = player_turn(player_hand)

    if player_under_22:
        computer_turn(computer_hand)

    determine_winner(player_hand, computer_hand)


def deal_card(hand=None, times=1):
    if hand is None:
        hand = []
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for _ in range(times):
        hand.append(cards[randint(0, 12)])
    return hand


def under_22_check(hand):
    if sum(hand) < 22:
        return True
    else:
        return False


def under_17_check(hand):
    if sum(hand) < 17:
        return True
    else:
        return False


def setup_game():
    player_hand = deal_card(times=2)
    player_under_22 = under_22_check(player_hand)
    if not player_under_22:
        player_hand = [1, 11]

    computer_hand = deal_card(times=2)
    computer_under_22 = under_22_check(computer_hand)

    if not computer_under_22:
        computer_hand = [1, 11]

    return player_hand, computer_hand


def player_turn(player_hand):
    player_under_22 = under_22_check(player_hand)
    player_final_hand = False
    while player_under_22 and not player_final_hand:
        print(f"Your hand: {player_hand}, current score: {sum(player_hand)}")
        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if choice == "y":
            deal_card(player_hand)
            player_under_22 = under_22_check(player_hand)
        elif choice == "n":
            player_final_hand = True
        else:
            print("Please re-type\n")
    return player_under_22


def computer_turn(computer_hand):
    print(f"\nComputers hand: {computer_hand}, current score: {sum(computer_hand)}")
    computer_under_17 = under_17_check(computer_hand)
    while computer_under_17:
        print("Computer must draw another card....")
        time.sleep(1)

        deal_card(computer_hand)
        computer_under_17 = under_17_check(computer_hand)
        print(f"Computers hand: {computer_hand}, current score: {sum(computer_hand)}")


def determine_winner(player_hand, computer_hand):
    time.sleep(1)
    print(f"\n\nYour hand: {player_hand}    VS    Computers hand: {computer_hand}")
    player_under_22 = under_22_check(player_hand)
    computer_under_22 = under_22_check(computer_hand)
    if player_under_22 and computer_under_22:
        if sum(player_hand) > sum(computer_hand):
            print("You won!")
        elif sum(player_hand) == sum(computer_hand):
            print("Draw")
        else:
            print("You lost")
    elif computer_under_22:
        print("You lost")
    else:
        print("You won!")


main()
