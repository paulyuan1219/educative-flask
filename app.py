from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  return("hello world. This is your new world")

if __name__ == "__name__":
  app.run(debug = True, host = "0.0.0.0", port = 5000)

