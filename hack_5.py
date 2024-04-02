"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    vowels = "aeiou"
    signs = "@310$"
    new_result = ''
    for text in result:
        if text.lower() in vowels:
            new_result += signs[vowels.index(text.lower())]
        else:
            new_result += text
    return new_result
print(fn_hack_5())