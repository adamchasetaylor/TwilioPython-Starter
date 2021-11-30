from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'twilio'

@app.route('/', methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"