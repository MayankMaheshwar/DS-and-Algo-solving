def diff(t, s):
    diff = 0
    for i in range(len(s)):
        diff -= ord(s[i])
        diff += ord(t[i])
    diff += ord(t[-1])
    print(chr(diff))
