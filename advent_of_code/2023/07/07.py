from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input

from typing import List
from collections  import Counter
import numpy as np


cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

@aoc_output(title="Day - ")
def part_1(lines: List[str]) -> int:
    hand_list = [line.split() for line in lines]
    
    def _sorter(game_hand):
        c = sorted(list(Counter(game_hand).values()), reverse=True)
        
        

        if c[0] == 5:
            return 6
        elif c[0] == 4:
            return 5
        elif c[0] == 3 and c[1] == 2:  # Full house
            return 4
        elif c[0] == 3:
            return 3
        elif c[0] == 2 and c[1] == 2:  # Two pair
            return 2
        elif c[0] == 2:
            return 1
        elif c[0] == 1:
            return 0
        return 'Impossible!'
    
    def _calculate_hand_value(game_hand):
        return sum([(len(cards)+1) - cards.index(v) for v in game_hand])

    type_bins = [(*hand, _sorter(hand[0])) for hand in hand_list]
    value_bins = [(*hand, _calculate_hand_value(hand[0])) for hand in type_bins]
    sorted_hands = sorted(value_bins, key=lambda x: (
        x[2],  # Sort on type
        *((len(cards)+1)-cards.index(v) for v in x[0])  # And break ties based on card index
    ))
    
    return np.sum(np.array([int(v[1]) for v in sorted_hands]) * np.mgrid[1:len(sorted_hands)+1])
    #     bin_dict[b[1]].append(b[0])

    # for binnum, b in bin_dict.items():
    #     bin_dict[binnum] = sorted(b, key=lambda x: x[0], reverse=True)
    
    # all_sorted_hands = (bin_dict[0] + bin_dict[1] + bin_dict[2] + bin_dict[3] + bin_dict[4] + bin_dict[5] + bin_dict[6])
    # multiplier = list(range(1, len(all_sorted_hands)+1))
    
    # running_sum = 0
    # for (hand, bid), multi in zip(all_sorted_hands, multiplier):
    #     running_sum += int(bid) * multi

    return running_sum


@aoc_output(title="Day - ")
def part_2(lines: List[str]) -> int:
    hand_list = [line.split() for line in lines]
    
    def _sorter(game_hand):
        c = Counter(game_hand)
        c_vals = sorted(list(c.values()), reverse=True)
        
        if game_hand == 'JJJJJ':
            return 6
        if 'J' in c:
            best_card = [v for v in c.most_common() if v[0] != 'J'][0]
            c.update({
                best_card[0]: c['J']
            })
            c_vals = sorted(list(c.values()), reverse=True)

        if c_vals[0] == 5:
            return 6
        elif c_vals[0] == 4:
            return 5
        elif c_vals[0] == 3 and c_vals[1] == 2:  # Full house
            return 4
        elif c_vals[0] == 3:
            return 3
        elif c_vals[0] == 2 and c_vals[1] == 2:  # Two pair
            return 2
        elif c_vals[0] == 2:
            return 1
        elif c_vals[0] == 1:
            return 0
        return 'Impossible!'
    
    def _calculate_hand_value(game_hand):
        return sum([(len(cards)+1) - cards.index(v) for v in game_hand])

    type_bins = [(*hand, _sorter(hand[0])) for hand in hand_list]
    value_bins = [(*hand, _calculate_hand_value(hand[0])) for hand in type_bins]
    sorted_hands = sorted(value_bins, key=lambda x: (
        x[2],  # Sort on type
        *((len(cards)+1)-cards.index(v) for v in x[0])  # And break ties based on card index
    ))
    
    return np.sum(np.array([int(v[1]) for v in sorted_hands]) * np.mgrid[1:len(sorted_hands)+1])

if __name__ == "__main__":
    pi = get_puzzle_input(__file__, block=True)
    part_2(pi)
