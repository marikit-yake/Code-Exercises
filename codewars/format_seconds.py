test1 = 60
test2 = 300

def format_duration(seconds):
    durations = {
        "year": seconds // 31536000,
        "day": seconds // 86400 % 365,
        "hour": seconds // 3600 % 24,
        "minute": seconds // 60 % 60,
        "second": seconds % 60
        }
    msg = []

    for dur in durations:
        if durations[dur] == 1:
            msg.append(str(durations[dur]) + " " + dur)
        
        elif durations[dur] > 1:
            msg.append(str(durations[dur]) + " " + dur + "s")

    if len(msg) > 1:
        msg.insert(-1, "and")

        if len(msg) > 2:
            return ", ".join(msg[:-2]) + " and " + msg[-1:][0]
    
    return "".join(msg) if msg else "now"
        

