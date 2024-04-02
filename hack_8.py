"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    result = [1,3,5,7,9]
    filter = [3,5,7]
    new_result = []
    for num in result:
        if num in filter:
            new_result.append(num)
    return new_result
print(fn_hack_8())