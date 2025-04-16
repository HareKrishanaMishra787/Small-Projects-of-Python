from flask import Flask
import random

# Initialize Flask app
app = Flask(__name__)

# Generate a random number between 0 and 9
num = random.randint(0, 9)
print(f"Random Number (Server): {num}")

# Decorator to check if the guessed number is correct
def number_check_decorator(function):
    def wrapper(number):
        my_number = function(number)
        if num == my_number:
            return ("<h1 style='color: green;'>You chose the correct number! 🎉</h1>"
                    "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>")
        elif num > my_number:
            return ("<h1 style='color: red;'>This is too low Try again. ❌ </h1>"
                    "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>")
        elif num < my_number:
            return ("<h1 style='color: red;'>This is too high Try again. ❌ </h1>"
                    "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>")
    return wrapper

# Home Route
@app.route("/")
def home():
    return "<h1>Welcome to the Number Guessing Game!</h1>" \
           "<p>Enter a number in the URL between 0 and 9 (e.g., /5).</p>"

# Number Guessing Route
@app.route("/<int:number>")
@number_check_decorator
def find_number(number):
    return number

# Run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)


"""this is the link of webstie generated in console  http://127.0.0.1:5000    """
