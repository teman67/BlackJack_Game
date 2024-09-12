### Description
###""""
###Our Blackjack Game House Rules
###The deck is unlimited in size.
###There are no jokers.
###The Jack/Queen/King all count as 10.
###The Ace can count as 11 or 1.
###Use the following list as the deck of cards:
###cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

###The cards in the list have equal probability of being drawn.
###Cards are not removed from the deck as they are drawn.
###The computer is the dealer.

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# cards=[11,10]

user = [random.choice(cards), random.choice(cards)]

dealer = [random.choice(cards), random.choice(cards)]



# print(user, dealer)
# print(sum(user), sum (dealer))

if sum(user) == 21 or sum(dealer) == 21:
    if sum(user)==21  and sum(dealer) == 21:
        print ("dealer won!")
    elif sum(user) == 21:
        print("user won!")
    else:
        print("dealer won!")

sum_user = sum(user)
sum_dealer = sum(dealer)

for item in cards:
    if sum(user) > 21 and 11 in user:
        sum_user -= 10
    if sum(dealer) > 21 and 11 in dealer:
        sum_dealer -= 10

# print(sum_user,sum_dealer)

print(dealer[0])

extra_cards = input("do you want new card?\n").lower()
if extra_cards == 'y':
    user = [random.choice(cards)]
    for item in cards:
        if sum(user) > 21 and 11 in user:
            sum_user -= 10
    if sum(user) > 21:
        print("user lost! Dealer Won!")

