from random import SystemRandom
from string import ascii_uppercase, digits

import numpy as np


def randint(maximum):
    return np.random.randint(0, maximum)


def random_number_str(length=1, minimum=0, maximum=None):
    maximum = maximum or 10 ** length
    return str(np.random.randint(minimum, maximum)).zfill(length)


def random_string(n):
    alphabet = ascii_uppercase + digits
    return "".join(SystemRandom().choice(alphabet) for _ in range(n))


def random_phone(area_code="27"):
    return f"{area_code}{random_number_str(10)}"


def random_birthday():
    return f"{random_number_str(4, 1920, 2021)}-{random_number_str(2, 1, 13)}-{random_number_str(2, 1, 29)}"
