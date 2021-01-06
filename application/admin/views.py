from flask_admin.contrib.sqla import ModelView

from application import db, admin_flask

from application.main.models import CodeCategory

admin_flask.add_view(ModelView(CodeCategory, db.session))

from application.main.models import CodeSnippet

admin_flask.add_view(ModelView(CodeSnippet, db.session))
