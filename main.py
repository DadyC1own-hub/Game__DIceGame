import random

def roll_dice():
    return random.randint(1, 6)

def get_number_of_players():
    while True:
        try:
            num_players = int(input("Enter the number of players (2-4): "))
            if 2 <= num_players <= 4:
                return num_players
            else:
                print("Number of players must be between 2 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_turn(player_num, player_score):
    print(f'\nPlayer {player_num} turn has just started')
    print(f"Your total score is: {player_score}\n")
    current_score = 0

    while True:
        should_roll = input("Would you like to roll (y/n)? ").lower()
        if should_roll != "y":
            break

        rolled_value = roll_dice()
        if rolled_value == 1:
            print("You rolled a 1! Turn over!")
            current_score = 0
            break
        else:
            current_score += rolled_value
            print(f"You rolled a: {rolled_value}")
            print(f"Your current score is: {current_score}")

    return current_score

def main():
    max_score = 50
    num_players = get_number_of_players()
    players_scores = [0 for _ in range(num_players)]

    while max(players_scores) < max_score:
        for player_idx in range(num_players):
            current_score = play_turn(player_idx + 1, players_scores[player_idx])
            players_scores[player_idx] += current_score
            print(f"Your total score is now: {players_scores[player_idx]}")

            if players_scores[player_idx] >= max_score:
                break

    winner_idx = players_scores.index(max(players_scores))
    print(f"Player {winner_idx + 1} is the winner with a score of: {players_scores[winner_idx]}")

if __name__ == "__main__":
    main()
