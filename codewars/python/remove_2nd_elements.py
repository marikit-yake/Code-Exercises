def remove_every_other(my_list):
    return my_list[::2]

def remove_every_other(my_list):
    return [item for idx, item in enumerate(my_list) if idx % 2 == 0]