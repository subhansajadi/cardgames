from random import Random
from itertools import combinations

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


def poker_has_flush(hand):
    """Determine if the five card poker hand has a flush."""
    look_for = None
    for (_, suit) in hand:
        if look_for is None:  
            look_for = suit
        elif look_for != suit:
            return False
    return True


def count_rank_pairs(hand):
    count = 0
    for ((r1, _), (r2, _)) in combinations(hand, 2):
        if r1 == r2:
            count += 1
    return count
  

# The previous function makes all the following functions trivial.


def poker_four_of_kind(hand):
    return count_rank_pairs(hand) == 6


def poker_full_house(hand):
    return count_rank_pairs(hand) == 4


def poker_three_of_kind(hand):
    return count_rank_pairs(hand) == 3


def poker_two_pair(hand):
    return count_rank_pairs(hand) == 2


def poker_one_pair(hand):
    return count_rank_pairs(hand) == 1


def poker_has_straight(hand):
    if count_rank_pairs(hand) > 0:
        return False
    hand_ranks = [ranks[rank] for (rank, _) in hand]
    min_rank, max_rank = min(hand_ranks), max(hand_ranks)
    if max_rank == 14:  # Special cases for straights with an ace
        if min_rank == 10:
            return True  # AKQJT, Broadway straight
        return sorted(hand) == [2, 3, 4, 5, 14]  # A2345, bicycle straight
    else:
        return max_rank-min_rank == 4


def poker_flush(hand):
    return poker_has_flush(hand) and not poker_has_straight(hand)


def poker_straight(hand):
    return poker_has_straight(hand) and not poker_has_flush(hand)


def poker_straight_flush(hand):
    return poker_has_straight(hand) and poker_has_flush(hand)


def poker_high_card(hand):
    return count_rank_pairs(hand) == 0 and not poker_has_flush(hand) and not poker_has_straight(hand)


def evaluate_all_poker_hands():
    funcs = [poker_one_pair, poker_two_pair, poker_three_of_kind,
             poker_straight, poker_flush, poker_full_house,
             poker_four_of_kind, poker_straight_flush, poker_high_card]
    counters = [0 for _ in funcs]
    for hand in combinations(deck, 5):
        for (i, f) in enumerate(funcs):
            if f(hand):
                counters[i] += 1
                break
    return [(f.__name__, counters[i]) for (i, f) in enumerate(funcs)]
