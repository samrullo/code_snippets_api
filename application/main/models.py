from application import db


class CodeSnippet(db.Model):
    __tablename__ = 'code_snippets'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    code = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('code_categories.id'))

    def to_json(self):
        json_code_snippet = {'description': self.description,
                             'code': self.code,
                             'category_id': self.category_id}
        return json_code_snippet

    @staticmethod
    def from_json(json_code_snippet):
        return CodeSnippet(description=json_code_snippet.get('description'),
                           code=json_code_snippet.get('code'),
                           category_id=json_code_snippet.get('category_id'))


class CodeCategory(db.Model):
    __tablename__ = 'code_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    description = db.Column(db.Text)
    code_snippets = db.relationship('CodeSnippet', backref='category', lazy='dynamic')

    def to_json(self):
        return {'name': self.name,
                'description': self.description}

    @staticmethod
    def from_json(json_category):
        return CodeCategory(name=json_category.get('name'),
                            description=json_category.get('description'))
