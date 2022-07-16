from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

all_posts = [
    {
        'title': 'Post1',
        'content': 'We have post 1 content here',
        'author': 'Glen Chiridza'
    },
    {
        'title': 'Post2',
        'content': 'We have post 2 content here'
    }
]


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    author = db.Column(db.String(50),nullable=False,default='N/A')
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    def __repr__(self):
        return f'Blog post == {self.title}'


@app.route('/')
@app.route('/home/')
def index():
    if request.method == 'POST':

    return render_template('index.html')


@app.route('/posts/',methods=['GET','POST'])
def posts():
    return render_template('posts.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)
