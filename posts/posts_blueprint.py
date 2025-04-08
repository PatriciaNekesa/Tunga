from flask import Blueprint, render_template

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='tenplates')

# Dummy blog posts
posts = [
    {"title": "First Blog Post", "content": "This is my first blog post!", "author": "Jane Doe"},
    {"title": "Second Blog Post", "content": "This is another blog post!", "author": "John Doe"}
]


# Dynamic routes
@posts_blueprint.route('/post/<int:post_id>')
def view_post(post_id):
    # Logic to view a given post by post_id
    if 0 <= post_id < len(posts):
        return render_template('post.html', post=posts[post_id])