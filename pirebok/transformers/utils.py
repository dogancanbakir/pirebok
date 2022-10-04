import random
import re
import string
from typing import Dict, List


def replace_random(candidate: str, sub: str, wanted: str) -> str:
    occurrences = list(map(lambda x: x.start(), re.finditer(re.escape(sub), candidate)))
    if not occurrences:
        return candidate

    pos = random.choice(occurrences)

    before = candidate[:pos]
    after = candidate[pos:]
    after = after.replace(sub, wanted, 1)

    result = before + after
    return result


def filter_candidates(symbols: Dict, payload: str) -> List[str]:
    return list(filter(lambda x: x in payload, symbols.keys()))


def random_string(max_len: int = 5, spaces: bool = True) -> str:
    return "".join(map(lambda _: random_char(spaces), range(random.randint(1, max_len))))


def random_char(spaces: bool = True) -> str:
    chars = list(string.printable)
    chars_no_space = list(filter(lambda x: x not in string.whitespace, chars))
    return random.choice(chars if spaces else chars_no_space)


def string_tautology() -> str:
    value_s = random_string(random.randint(1, 5))
    tautologies = [
        # Strings - equals
        f"'{value_s}'='{value_s}'",
        f"'{value_s}' LIKE '{value_s}'",
        f'"{value_s}"="{value_s}"',
        f'"{value_s}" LIKE "{value_s}"',
        # Strings - not equal
        f"'{value_s}'!='{value_s + random_string(1, spaces=False)}'",
        f"'{value_s}'<>'{value_s + random_string(1, spaces=False)}'",
        f"'{value_s}' NOT LIKE '{value_s + random_string(1, spaces=False)}'",
        f'"{value_s}"!="{value_s + random_string(1, spaces=False)}"',
        f'"{value_s}"<>"{value_s + random_string(1, spaces=False)}"',
        f'"{value_s}" NOT LIKE "{value_s + random_string(1, spaces=False)}"',
    ]

    return random.choice(tautologies)


def number_tautology():
    value_n = random.randint(1, 10000)
    tautologies = [
        # Numbers - equal
        f"{value_n}={value_n}",
        f"{value_n} LIKE {value_n}",
        # Numbers - not equal
        f"{value_n}!={value_n + 1}",
        f"{value_n}<>{value_n + 1}",
        f"{value_n} NOT LIKE {value_n + 1}",
        f"{value_n} IN ({value_n - 1},{value_n},{value_n + 1})",
    ]

    return random.choice(tautologies)


def string_contradiction() -> str:
    value_s = random_string(random.randint(1, 5))
    contradictions = [
        # Strings - equals
        f"'{value_s}'='{value_s + random_string(1, spaces=False)}'",
        f"'{value_s}' LIKE '{value_s + random_string(1, spaces=False)}'",
        f'"{value_s}"="{value_s + random_string(1, spaces=False)}"',
        f'"{value_s}" LIKE "{value_s + random_string(1, spaces=False)}"',
        # Strings - not equal
        f"'{value_s}'!='{value_s}'",
        f"'{value_s}'<>'{value_s}'",
        f"'{value_s}' NOT LIKE '{value_s}'",
        f'"{value_s}"!="{value_s}"',
        f'"{value_s}"<>"{value_s}"',
        f'"{value_s}" NOT LIKE "{value_s}"',
    ]
    return random.choice(contradictions)


def number_contradiction():
    value_n = random.randint(1, 10000)

    contradictions = [
        # Numbers - equal
        f"{value_n}={value_n + 1}",
        f"{value_n} LIKE {value_n + 1}",
        # Numbers - not equal
        f"{value_n}!={value_n}",
        f"{value_n}<>{value_n}",
        f"{value_n} NOT LIKE {value_n}",
        f"{value_n} NOT IN ({value_n - 1},{value_n},{value_n + 1})",
    ]

    return random.choice(contradictions)
