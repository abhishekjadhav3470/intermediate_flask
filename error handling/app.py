from flask import Flask, render_template

app = Flask(__name__)

# Custom error handlers for 404 and 500 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# A route to intentionally raise a 500 error
@app.route('/raise_error')
def raise_error():
    raise Exception('This is a 500 Internal Server Error.')

@app.route('/')
def home():
    return 'Welcome to the Home Page'

if __name__ == '__main__':
    app.run(debug=True)
