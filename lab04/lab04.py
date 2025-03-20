import random
print("Welcome to the dice game!")
score = 0
rounds = 0
wins = 0
draws = 0
losses = 0
round_numbers = []
player_totals = []
computer_totals = []
results = []

def roll_dice():
    return random.randint(1,6)

def roll_multiple_dice(num_dice):
    rolls = [roll_dice() for x in range(num_dice)]
    print("Rolled values:", rolls)
    return sum(rolls)

def get_round_result(player_total, computer_total):
    global score, wins, draws, losses
    if player_total > computer_total:
        score += 20
        wins +=1
        return "Win"
    elif player_total < computer_total:
        losses +=1
        return "Loss"
    else:
        score += 10
        draws += 1
        return "Draw"

def shop(score):
    print("Welcome to the shop!")
    print("1. Add +5 points (Cost: 5 points)")
    print("2. Add +15 points (Cost: 10 points)")
    print("3. Exit shop")
    
    choice = input("Choose an option: ")
    if choice == "1" and score >= 5:
        score += 5
        print("5 points added to your score!")
    elif choice == "2" and score >= 10:
        score += 15
        print("15 points added to your score!")
    elif choice == 3:
        print("Exiting shop")
    else:
        print("Not enough points")
    return score
def display_statistics(rounds, wins, draws, losses, score, round_numbers, player_totals, computer_totals, results):
    print("Here are your round results:")
    print("Total rounds:", rounds)
    print("Wins:", wins, "Draws:", draws, "Losses:", losses)
    print("Final score:", score)
    for i in range(rounds):
        print("Round", round_numbers[i],":", "Player", player_totals[i], "Computer", computer_totals[i], "--->", results[i])

random.seed()
while True:
    rounds += 1
    visit_shop = input("Do you want to visit the shops? (yes/no): ")
    if visit_shop == "yes":
        score = shop(score)
    print("Starting round", rounds)
    player_total = roll_multiple_dice(2)
    computer_total = roll_multiple_dice(2)

    round_result = get_round_result(player_total, computer_total)

    round_numbers.append(rounds)
    player_totals.append(player_total)
    computer_totals.append(computer_total)
    results.append(round_result)
    print("Result:", round_result, "Score:", score)

    continue_game = input("Do you want to continue the game? (yes/no): ")
    if continue_game != "yes":
        break

display_statistics(rounds, wins, draws, losses, score, round_numbers, player_totals, computer_totals, results)