# app/__init__.py
fromflaskimportFlask
# Initialize the app
app=Flask(__name__,instance_relative_config=True)
# Load the views
fromappimportviews
# Load the config file
app.config.from_object('config’)
