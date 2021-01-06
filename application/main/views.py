from . import main_bp
from flask import render_template


@main_bp.route('/')
@main_bp.route('/home')
def home():
    return render_template('index.html', page_header_title="Code Snippet Main Page")
