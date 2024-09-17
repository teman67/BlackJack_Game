import random

# Define the deck of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Draw initial cards for the user and the dealer
user = [random.choice(cards), random.choice(cards)]
dealer = [random.choice(cards), random.choice(cards)]

# Function to calculate the current sum of cards with Ace adjustment
def calculate_sum(hand):
    total = sum(hand)
    # Adjust for Aces if total > 21
    while total > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        total = sum(hand)
    return total

# Initial sums
sum_user = calculate_sum(user)
sum_dealer = calculate_sum(dealer)

print(f"User cards: {user}, User sum: {sum_user}")
print(f"Dealer's visible card: {dealer[0]}")

# Check for initial Blackjack
if sum_user == 21 or sum_dealer == 21:
    if sum_user == 21 and sum_dealer == 21:
        print("It's a draw!")
    elif sum_user == 21:
        print("User won with a Blackjack!")
    else:
        print("Dealer won with a Blackjack!")
else:
    # User's turn
    while True:
        extra_card = input("Do you want a new card? (y/n): ").lower()
        if extra_card == 'y':
            user.append(random.choice(cards))
            sum_user = calculate_sum(user)
            print(f"User cards: {user}, User sum: {sum_user}")
            
            # Check if the user busts
            if sum_user > 21:
                print("User busted! Dealer wins!")
                exit()
        else:
            break

    # Dealer's turn: Dealer must draw until sum is at least 17
    while sum_dealer < 17:
        dealer.append(random.choice(cards))
        sum_dealer = calculate_sum(dealer)

    print(f"Dealer cards: {dealer}, Dealer sum: {sum_dealer}")

    # Determine the winner
    if sum_dealer > 21:
        print("Dealer busted! User wins!")
    elif sum_user > sum_dealer:
        print("User wins!")
    elif sum_user < sum_dealer:
        print("Dealer wins!")
    else:
        print("It's a draw!")

# Final sums
print(f"Final sums -> User: {sum_user}, Dealer: {sum_dealer}")
