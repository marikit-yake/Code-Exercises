def order(sentence):
    if not sentence:
        return ""
    
    word_dct = dict()
    words = sentence.split(" ")
    for word in words:
        for letter in word:
            if letter.isdigit():
                word_dct[int(letter)] = word
    
    ordered = [word_dct[pos] for pos in sorted(word_dct.keys())]
    return " ".join(ordered)


def order(sentence):
    return " ".join(sorted(sentence.split(), key=min))


test = "4of Fo1r pe6ople g3ood th5e the2"

print(order(test))