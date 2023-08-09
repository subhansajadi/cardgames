from random import Random

rng = Random(12345)

suits = ['clubs', 'diamonds', 'hearts', 'spades']
ranks = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
         'nine': 9, 'ten': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}

deck = [(rank, suit) for suit in suits for rank in ranks]


def deal_hand(n, taken=None):
    """Deal a random hand with n cards, without replacement."""
    hand, taken = [], taken if taken else []
    while len(hand) < n:
        c = rng.choice(deck)
        if c not in hand and c not in taken:
            hand.append(c)
    return hand

def blackjack_count_value(hand):
    """Given a blackjack hand, count its numerical value. This
    value is returned as a string to distinguish between blackjack
    and 21 made with three or more cards, and whether the hand is
    soft or hard."""
    total = 0 
    soft = 0  
    for (rank, _) in hand:
        v = ranks[rank]
        if v == 14:  # Treat every ace as 11 to begin with
            total, soft = total+11, soft+1
        else:
            total += min(10, v) 
        if total > 21:
            if soft: 
                soft, total = soft-1, total-10
            else:
                return 'bust'
    if total == 21 and len(hand) == 2:
        return 'blackjack'
    return f"{'soft' if soft else 'hard'} {total}"
