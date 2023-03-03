import re

def to_camel_case(text):
    return re.sub(r"[-_](.)", lambda x: x.group(1).capitalize(), text)