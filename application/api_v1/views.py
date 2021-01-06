from . import api_v1_bp
from flask import jsonify
from application.main.models import CodeSnippet


@api_v1_bp.route('/code_snippets/')
def get_code_snippets():
    return jsonify({'code_snippets': [code_snippet.to_json() for code_snippet in CodeSnippet.query.all()]})


@api_v1_bp.route('/code_snippets/<int:id>')
def get_code_snippet(id):
    code_snippet = CodeSnippet.query.get_or_404(id)
    return jsonify(code_snippet.to_json)
