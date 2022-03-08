import sys


s = ""
ques = set(['how', 'where', 'what', 'when', 'is', 'can'])

user_input = sys.argv[1:]

print(user_input)
if user_input[0] in ques:
    s += user_input[0].capitalize() + ' ' + \
        " ".join(user_input[1:])+"?" + " "
    print(s)
