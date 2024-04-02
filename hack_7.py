"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    i = 0
    result = []
    while i < 6:
        result.append(i)
        i += 1
    return list(reversed(result))
print(fn_hack_7())