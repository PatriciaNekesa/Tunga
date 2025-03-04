from flask import Flask, render_template
app = Flask(__name__)



# Dummy blog posts
posts = [
    {"title": "First Blog Post", "content": "This is my first blog post!", "author": "Jane Doe"},
    {"title": "Second Blog Post", "content": "This is another blog post!", "author": "John Doe"}
]

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

# Dynamic routes
@app.route('/post/<int:post_id>')
def view_post(post_id):
    # Logic to view a given post by post_id
    if 0 <= post_id < len(posts):
        return render_template('post.html', post=posts[post_id])
    
if __name__ == '__main__':
    app.run()