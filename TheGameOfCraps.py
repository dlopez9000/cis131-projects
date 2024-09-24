# Darlene Lopez
# CIS131
# This program simulates the popular dice game known as “craps.”

import random
from collections import defaultdict


# Function to roll two dice and return their face values as a tuple
def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)


# Simulate 1,000,000 games of craps
def simulate_craps(num_games):
    wins = defaultdict(int)  # dictionary to track wins based on number of rolls
    losses = defaultdict(int)  # dictionary to track losses based on number of rolls
    total_wins = 0  # total wins counter
    total_losses = 0  # total losses counter

    for _ in range(num_games):
        game_status = 'CONTINUE'
        roll_count = 1  # track number of rolls for this game
        die_values = roll_dice()
        sum_of_dice = sum(die_values)

        # Determine game outcome after first roll
        if sum_of_dice in (7, 11):
            game_status = 'WON'
        elif sum_of_dice in (2, 3, 12):
            game_status = 'LOST'
        else:
            my_point = sum_of_dice

        # Continue rolling if no immediate win or loss
        while game_status == 'CONTINUE':
            roll_count += 1
            die_values = roll_dice()
            sum_of_dice = sum(die_values)

            if sum_of_dice == my_point:
                game_status = 'WON'
            elif sum_of_dice == 7:
                game_status = 'LOST'

        # Track wins or losses based on roll count
        if game_status == 'WON':
            wins[roll_count] += 1
            total_wins += 1
        else:
            losses[roll_count] += 1
            total_losses += 1

    # Display summary of results
    print(f"Percentage of wins: {100 * total_wins / num_games:.1f}%")
    print(f"Percentage of losses: {100 * total_losses / num_games:.1f}%\n")
    print(f"{'Rolls':<10}{'% Resolved on this roll':<25}{'Cumulative % of games resolved':<30}")

    cumulative_resolved = 0
    for roll_count in sorted(set(wins.keys()).union(losses.keys())):
        resolved_on_roll = wins[roll_count] + losses[roll_count]
        percentage_resolved = 100 * resolved_on_roll / num_games
        cumulative_resolved += percentage_resolved
        print(f"{roll_count:<10}{percentage_resolved:<25.2f}{cumulative_resolved:<30.2f}")


# Run simulation for 1,000,000 games
simulate_craps(1_000_000)
