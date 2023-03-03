from functools import reduce

def subtractProductAndSum(n: int) -> int:
    nums = [int(num) for num in list(str(n))]
    prod = reduce(lambda x, y: x * y,  nums)
    sum_ = reduce(lambda x, y: x + y, nums)
    return prod - sum_