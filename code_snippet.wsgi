import os
import sys

sys.path.insert(0,'/var/www/code_snippets_api')

activate_this="/var/www/code_snippets_api/venv/bin/activator.py"
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

env_vars=['FLASK_APP', 'FLASK_ENV', 'PROD_SQLALCHEMY_DATABASE_URI']

def application(environ,start_response):
    for env_var in env_vars:
        os.environ[env_var]=environ[env_var]
    from code_snippet import app as _application
    return _application(environ,start_response)