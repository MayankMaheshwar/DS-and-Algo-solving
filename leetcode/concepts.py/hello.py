from flask import Flask
import sys
app = Flask(__name__)
ques = set(['how', 'where', 'what', 'when', 'is', 'can'])

s = ''


@app.route("/<sys.argv[1:]>")
def hello_world(user_input=sys.argv[1:]):
    user_input = user_input.split(' ')
    if user_input[0] in ques:
        s += user_input[0].capitalize() + ' ' + \
            " ".join(user_input[1:])+"?" + " "

    elif user_input[0] == '/end':
        print(s)
        return

    else:
        s += user_input[0].capitalize() + ' ' + \
            " ".join(user_input[1:])+"." + " "
