"""Validator and Genrator of MBIs"""
import os
import re
from distutils.log import debug
from sre_parse import DIGITS
from flask import Flask
from flask_cors import CORS
from random import choice
from string import digits, ascii_uppercase

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

# Allow access from frontend
CORS(app)

# Constant Variables
LETTERS = "".join(set(ascii_uppercase) - {"B", "I", "L", "O", "S", "Z"})
NON_ZERO_DIGITS = digits[1:]
DIGIT_LETTERS = digits + LETTERS
DIGITS = digits

# Pattern MBI follows
MBI_PATTERN = [
    NON_ZERO_DIGITS,
    LETTERS,
    DIGIT_LETTERS,
    DIGITS,
    LETTERS,
    DIGIT_LETTERS,
    DIGITS,
    LETTERS,
    LETTERS,
    DIGITS,
    DIGITS,
]

# Helpers
def validator(mbi):
    """Validate if MBI follows standards."""
    # For readability type variables are added as this is the standard and names used for MBI
    typeC = NON_ZERO_DIGITS
    typeA = LETTERS
    typeAN = DIGIT_LETTERS
    typeN = digits

    # MBI pattern being checked
    matched = re.match(
        f"[{typeC}][{typeA}][{typeAN}][{typeN}][{typeA}][{typeAN}][{typeN}][{typeA}][{typeA}][{typeN}][{typeN}]",
        mbi,
    )
    # True or False if pattern matches
    return bool(matched)


# Api Routes
@app.route("/generate_mbi/")
def generate_mbi():
    """Will Generate an MBI based on MBI_PATTERN"""
    return "".join(choice(char) for char in MBI_PATTERN)


@app.route("/validate_mbi/<mbi>")
def validate_mbi(mbi):
    """Will MBI and return a string of True or False."""
    if validator(mbi) == True:
        return "True"
    else:
        return "False"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)
