suits = ['clubs', 'diamonds', 'hearts', 'spades']
ranks = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
         'nine': 9, 'ten': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}

deck = [(rank, suit) for suit in suits for rank in ranks]

def bridge_score(suit, level, vul, dbl, made):
    mul = {'X': 2, 'XX': 4}.get(dbl, 1)
    score, bonus = 0, 0

    for trick in range(1, made+1):
        if suit == 'clubs' or suit == 'diamonds':
            pts = 20
        elif suit == 'hearts' or suit == 'spades':
            pts = 30
        else:
            pts = 40 if trick == 1 else 30
        # Score from the raw points.
        if trick <= level:  # Part of contract
            score += mul * pts
        elif mul == 1:  # Undoubled overtrick
            bonus += mul * pts
        elif mul == 2:  # Doubled overtrick
            bonus += 200 if vul else 100
        else:  # Redoubled overtrick
            bonus += 400 if vul else 200
    if score >= 100:  # Game bonus
        bonus += 500 if vul else 300
    else:  # Partscore bonus
        bonus += 50
    if level == 6:  # Small slam bonus
        bonus += 750 if vul else 500
    if level == 7:  # Grand slam bonus
        bonus += 1500 if vul else 1000
    score += bonus
    if mul == 2:  # Insult bonus for making a (re)doubled contract
        score += 50
    elif mul == 4:
        score += 100
    return score
