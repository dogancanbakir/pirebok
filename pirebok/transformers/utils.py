import random
import re
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
