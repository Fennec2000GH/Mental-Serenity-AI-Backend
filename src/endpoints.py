
from flask import Flask, jsonify, make_response, render_template, request

from chatbot import chatbot

app = Flask(__name__)

@app.route('/')
def home():
    """Home page display"""
    return 'Home Page'

@app.route('/chatbot/message=<message>', methods=['GET', 'POST'])
def process_message(message: str):
    """
    Process message from user.

    Args:
        message (str): [description]
    """
    print(message)
    print(type(message))

    response_text = chatbot.get_response(statement=message)

    print(response_text)
    print(type(response_text))

    return make_response(jsonify(dict({'key': 'value',
                                       'message': message,
                                       'response': str(response_text)})),
                         200)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True, load_dotenv=True)
