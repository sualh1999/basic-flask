from flask import Flask

app = Flask(__name__)

@app.route('/')
def ping ():
  return "PONG salih"

@app.route('/abb')
def pong ():
  return "Ping PONG abb"

