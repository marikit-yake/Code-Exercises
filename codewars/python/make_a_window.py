def make_a_window(num): 
    top = f"-" * (2*num+3)
    middle = f"|{'-' * num}+{'-' * num}|"
    glass = [f"|{'.' * num}|{'.' * num}|"] * num
    return "\n".join([top, *glass, middle, *glass, top])