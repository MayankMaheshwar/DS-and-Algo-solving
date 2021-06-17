import re


def decrypt(str):
    alphanumeric = [character for character in str if character.isalnum()]
    alphanumeric = "".join(alphanumeric)

    result = ''.join(w for w in alphanumeric if w.isupper())

    return result

x
s = "KDeoALOklOOHserfL&&oAJSIskdsf"
print(decrypt(s))
