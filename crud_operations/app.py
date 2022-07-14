from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home/')
def hello():
    return "Hello Flen "+str(id)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)
