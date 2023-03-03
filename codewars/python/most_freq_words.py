from string import punctuation, whitespace, ascii_lowercase
from collections import Counter
import re


test1 = """In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""

test2 = "'"

def top_3_words(text):
    if not text:
        return []

    mod_punctuation = punctuation.replace("'", "") + whitespace.replace(" ", "")

    for char in text:
        if char in mod_punctuation:
            text = text.replace(char, "")
    
    counts = Counter(text.lower().split()).items()
    return list(dict(sorted(counts, key=lambda x: x[1], reverse=True)))[:3]

# expected out: => ["a", "of", "on"]


def top_3_words(text):
    counts =  Counter(re.sub(r"[^\w]+", text.lower()).split()).items()
    return list(dict(sorted(counts, key=lambda x: x[1], reverse=True)))[:3]

    # return re.findall(r"^[\d\s^,]\w+[\d\s^,]", text)