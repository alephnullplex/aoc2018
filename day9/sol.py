#!/usr/bin/env python3

def play(rounds, num_players):
    scores = [0 for _ in range(num_players)]
    game_state = [0]
    position = 0

    for r in range(rounds):
        player = r % len(scores)
        value = r+1
        if (value % 23) == 0:
            position = (position - 7) % len(game_state) 
            scores[player] += (value + game_state[position])
            del game_state[position]
        else:
            position = (position + 1) % len(game_state) + 1
            game_state = game_state[:position] + [value] + game_state[position:]
    return scores

from collections import deque
def playFast(rounds, num_players):
    # this version uses double ended que (doublely linked list)
    # this avoids the enourmous amount of copying the other version does
    scores = [0 for _ in range(num_players)]
    game_state = deque([0])
    position = 0

    for r in range(rounds):
        player = r % len(scores)
        value = r + 1
        if (value % 23) == 0:
            game_state.rotate(7)
            scores[player] += (value + game_state.pop())
            game_state.rotate(-1)
        else:
            game_state.rotate(-1)
            game_state.append(value)
    return scores

print("Winning score: ", max(play(71249, 478)))
print("Winning score: ", max(playFast(71249*100, 478)))

        