from typing import List

string = "codeleet"
idx = [4,5,6,7,0,2,1,3]

def restoreString(s: str, indices: List[int]) -> str:
    # String and indices are 1:1 so I created a dictionary
    dct = {index: s for s, index in zip(s, indices)}
    new_str = ""

    # Sort the dictionary's keys; ie by indices
    # add values by ordered index
    for k in sorted(dct):
        new_str += dct[k]

    return new_str
    
print(restoreString(string, idx)) # Output: 'leetcode'