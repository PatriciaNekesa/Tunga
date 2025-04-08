from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/post/<int:post_id>')
def view_post(post_id):
    return f'Viewing blog post #{post_id}'

if __name__ == '__main__':
    app.run()