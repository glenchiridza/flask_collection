from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home/')
def index():
    return render_template('index.html')


@app.route('/posts/')
def posts():
    return render_template('posts.html')


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)
