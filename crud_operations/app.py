from flask import Flask, render_template

app = Flask(__name__)

all_posts = [
    {
        'title': 'Post1',
        'content': 'We have post 1 content here',
        'author':'Glen Chiridza'
    },
    {
        'title': 'Post2',
        'content': 'We have post 2 content here'
    }
]


@app.route('/')
@app.route('/home/')
def index():
    return render_template('index.html')


@app.route('/posts/')
def posts():
    return render_template('posts.html',posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)
