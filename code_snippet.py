from application import create_app, db
from flask_migrate import Migrate
import os

app = create_app(os.environ.get('FLASK_ENV'))

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(ssl_context='adhoc')
