# Lists and modules
# Author: Yeshua
# March 11th 

import random

def coin_flip():
    # Return heads or tails or other?
    # Heads is any number 0 to 0.499999999
    # Tails is any number from 0.5 to 0.999991
    # Other is any number greater than 0.999991
    roll = random.random()

    if roll < 0.5: 
        return "heads"
    elif roll < 0.999991:
        return "tails"
    else: 
        return "other?"
    
def card_reveal():
    # Reveal a "card" from A, Z, ..., Q, K
    roll = random.randrange(1,14)

    if roll == 1:
        return "A"
    elif roll == 11:
        return "J"
    elif roll == 12:
        return "Q"
    elif roll == 13:
        return "K"
    else:
        return str(roll)
    
def main():
    # Keep track of heads and tails
    heads = 0
    tails = 0
    other = 0
    result = coin_flip
    
    cards_drawn = []
    
    for _ in range(1,000,000):
     # Flip coin
     result = coin_flip()
     cards_drawn.append(card_reveal)
    
    if result == "heads":
        heads = heads + 1
    elif result == "tails":
        tails += 1
    else:
        other += 1

        print(cards_drawn)

    print(f"Number of Heads: {heads}")
    print(f"Number of Tails: {tails}")
    print(f"Number of others: {other}")

    main()

    
    


