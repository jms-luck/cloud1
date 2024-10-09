from flask import Flask, render_template, request

app = Flask(__name__)

# Serve the login page
@app.route('/')
def index():
    return render_template('login.html')

# Handle the login form submission
@app.route('/signin', methods=['POST'])
def login():
    # Get the form data
    email = request.form['email']
    password = request.form['password']

    # You can add validation logic here
    if email and password:
        return "Hi Hello, you've logged in!"
    
    # If invalid, return an error
    return "Invalid login credentials."

if __name__ == '__main__':
    app.run(debug=True)
