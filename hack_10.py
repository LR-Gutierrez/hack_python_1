"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    vowels = "aeiou"
    signs = "@310$"
    new_result = []
    for text in result:
        if text.lower() in vowels:
            new_result += signs[vowels.index(text.lower())].upper()
        else:
            new_result += text.upper()
    return new_result  
print(fn_hack_10())