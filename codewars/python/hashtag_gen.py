def generate_hashtag(s):
    if s == "" or len(s) > 140:
        return False
    
    result = [word.title() for word in s.split()]
    return "#" + "".join(result)