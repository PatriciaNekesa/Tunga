from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

# Simulate a simple in-memory blog post store
posts = [
    {"id": 1, "title": "First Post", "content": "Welcome to my blog!"},
    {"id": 2, "title": "Another Post", "content": "Flask is awesome!"}
]

@app.route('/')
def home():
    return render_template("home.html", posts=posts)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if not post:
        return "Post not found", 404
    return render_template("post.html", post=post)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if title and content:
            new_id = posts[-1]['id'] + 1 if posts else 1
            posts.append({"id": new_id, "title": title, "content": content})
            return redirect(url_for('home'))
    return '''
        <form method="post">
            Title: <input type="text" name="title"><br>
            Content:<br>
            <textarea name="content"></textarea><br>
            <input type="submit" value="Create Post">
        </form>
    '''

@app.route('/api/posts')
def api_posts():
    return jsonify(posts)

if __name__ == '__main__':
    app.run(debug=True)
