test = "G()(al)"

def interpret(command: str) -> str:
    cmds = {"G": "G", "()": "o", "(al)": "al"}
    new_str = ""
    result = []

    for char in command:
        new_str += char

        if new_str in cmds:
            result.append(cmds[new_str])
            new_str = ""

    return "".join(result)

    

print(interpret(test))