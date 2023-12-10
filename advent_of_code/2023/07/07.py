from advent_of_code.decorators import aoc_output
from advent_of_code.utilities import get_puzzle_input

from typing import List
from collections  import Counter
import numpy as np

        
type_values = {
    (5,): 6,
    (4, 1): 5,
    (3, 2): 4,
    (3, 1, 1): 3,
    (2, 2, 1): 2,
    (2, 1, 1, 1): 1,
    (1, 1, 1, 1, 1): 0
}


def camel_card_winnings(lines: List[str], use_jokers: bool = False) -> int:
    # Card order to determine it's value
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    if use_jokers:
        # If we use jokers, the joker is moved to the back
        cards.insert(len(cards), cards.pop(cards.index('J')))
    # Parse the input
    hand_list = [
        (line.split()[0], int(line.split()[1])) 
        for line in lines
    ]

    def _hand_type(game_hand):
        c = Counter(game_hand)
        counts = sorted(list(c.values()), reverse=True)

        if use_jokers:
            if game_hand == 'JJJJJ':
                return 6
            elif 'J' in c:
                best_card = [v for v in c.most_common() if v[0] != 'J'][0]
                c.update({
                    best_card[0]: c['J']
                })
                c.pop('J')
                counts = sorted(list(c.values()), reverse=True)
        return type_values.get(tuple(counts))

    type_bins = [(*hand, _hand_type(hand[0])) for hand in hand_list]
    sorted_hands = sorted(type_bins, key=lambda x: (
        x[2],  # Sort on type
        *((len(cards)+1)-cards.index(v) for v in x[0])  # And break ties based on card index
    ))

    return np.sum(np.array(sorted_hands)[:, 1].astype(int) * np.mgrid[1:len(sorted_hands)+1])

if __name__ == "__main__":
    pi = get_puzzle_input(__file__, block=True)

    solution_1 = aoc_output(title="Day 7 - Camel Cards")(
        camel_card_winnings
    )(pi)
    solution_2 = aoc_output(title="Day 7 - Camel Jokers")(
        lambda x: camel_card_winnings(x, use_jokers=True)
    )(pi)
