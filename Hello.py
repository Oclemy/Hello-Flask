# - Our python file.
# - Import flask and render_template
# -Initialize flask
# -Decorate index function with our route

# import flask
from flask import Flask, render_template

# initialize flask
app = Flask(__name__)

# homepage
@app.route('/')
def index():
    return render_template('index.html',site_title="Camposha.info",header="Hello World",sub_header="First Flask app",
                           description="Camposha.info is a programming examples portal. We produce easy to understand programming"
                                       "examples in many dufferent languages. Our examples are practical and beginner friendly.")


# run flask
if __name__ == '__main__':
    app.run(debug=True)
