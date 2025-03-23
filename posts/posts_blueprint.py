from flask import Blueprint, render_template

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='tenplates')

