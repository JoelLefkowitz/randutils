import numpy as np

from .chance import by_chance
from .exceptions import EmptyListError


def pop_random_entry(lst):
    if not lst:
        raise EmptyListError

    index = np.random.randint(0, len(lst))
    return lst.pop(index)


def pick_random_entry(lst):
    if not lst:
        raise EmptyListError

    index = np.random.randint(0, len(lst))
    return lst[index]


def randomly_filter(lst, weight=0.1):
    return [i for i in lst if by_chance(weight)]


def scramble(lst):
    return sorted(lst, key=lambda x: random.random())
