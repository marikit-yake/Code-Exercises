import re

def numDifferentIntegers(word: str) -> int:
    return len(set(map(int, re.findall(r"\d+", word))))