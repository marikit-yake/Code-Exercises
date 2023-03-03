from string import punctuation

def pig_it(text):
    output = []
    
    for t in text.split(" "):
        if t not in punctuation:
            output.append(t[1:] + t[0] + "ay")
            
        else:
            output.append(t)

    return " ".join(output)