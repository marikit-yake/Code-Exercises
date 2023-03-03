def rgb(r, g, b):
    bounds = range(0, 255)
    
    rgb = []
    # Bring values into bounds
    for color in (r, g, b):
        if color not in bounds and color > max(bounds):
            color = 255
            rgb.append(color)
        elif color not in bounds and color < min(bounds):
            color = 0
            rgb.append(color)
        else:
            rgb.append(color)
    
    return "%02x%02x%02x".upper() % (rgb[0], rgb[1], rgb[2])


def rgb(r, g, b):
    bounds = lambda x: min(255, max(x, 0))
    return ("%02X" * 3) % (bounds(r), bounds(b), bounds(g))