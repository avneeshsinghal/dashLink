import os
import sys
import flask

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '../../')))



app = flask.Flask(__name__)
app.config.from_object(__name__)
app.config['MONGODB_SETTINGS'] = {'DB': 'users'}
#app.config['TESTING'] = True

app.debug = True
app.config['DEBUG_TB_PANELS'] = (
    'flask_debugtoolbar.panels.versions.VersionDebugPanel',
    'flask_debugtoolbar.panels.timer.TimerDebugPanel',
    'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
    'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
    'flask_debugtoolbar.panels.template.TemplateDebugPanel',
    'flask_debugtoolbar.panels.logger.LoggingPanel',
    'flask_mongoengine.panels.MongoDebugPanel'
)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

from models import db
db.init_app(app)


from views import viewTodo_name, pagination
app.add_url_rule('/', view_func=viewTodo_name)
app.add_url_rule('/pagination', view_func=pagination)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
