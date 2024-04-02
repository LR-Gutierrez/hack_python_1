"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    i = 0
    result = [1, 2, 3]
    new_result = []
    while i < len(result):
        new_result.append(result[i])
        new_result.append('@')
        i += 1
    return new_result
print(fn_hack_9())