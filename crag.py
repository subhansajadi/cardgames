def crag_score(dice):
  score_dict = {}

  if dice[0] == dice[1] == dice[2]:
    score_dict[25] = 1

  if (dice[0] == dice[1] or dice[1] == dice[2] or dice[0] == dice[2]) and sum(dice) == 13:
    score_dict[50] = 1

  if sum(dice) == 13:
    score_dict[26] = 1

  if sorted(dice) == [1, 2, 3] or sorted(dice) == [4, 5, 6]:
    score_dict[20] = 1
    
  if sorted(dice) == [1, 3, 5] or sorted(dice) == [2, 4, 6]:
    score_dict[20] = 1

  dice_counts = {i: dice.count(i) for i in range(1, 7)}
  for i in range(1, 7):
    if dice_counts[i] >= 1:
      score_dict[dice_counts[i] * i] = 1
  return max(score_dict)
