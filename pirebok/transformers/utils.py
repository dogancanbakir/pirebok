import random
import re
import string
from typing import Dict, List


def replace_random(candidate: str, sub: str, wanted: str) -> str:
    occurrences = [m.start() for m in re.finditer(re.escape(sub), candidate)]
    if not occurrences:
        return candidate

    pos = random.choice(occurrences)

    before = candidate[:pos]
    after = candidate[pos:]
    after = after.replace(sub, wanted, 1)

    result = before + after
    return result


def filter_candidates(symbols: Dict, payload: str) -> List[str]:
    return [s for s in symbols.keys() if s in payload]


def random_string(max_len: int = 5, spaces: bool = True):
    return "".join([random_char(spaces=spaces) for i in range(random.randint(1, max_len))])


def random_char(spaces: int = True):
    chars = list(string.printable)
    chars_no_space = [c for c in chars if c not in string.whitespace]
    return random.choice(chars if spaces else chars_no_space)


def tautology():
    value_s = random_string(random.randint(1, 5))
    value_n = random.randint(1, 10000)
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
