from flask import Flask

# Create a Flask app instance (like an object of the Flask class)
app = Flask(__name__)

# Define a route (a URL path) and what it does
@app.route('/about')
def about():
    return "This is the About page."

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
