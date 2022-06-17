# MBI Validator and Generator - (Medicare Beneficiary Identifier/Identification)

## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [FAQs](#faqs)

### General Info
***
- This project is an API created with Flask and Python.
- There will be 2 endpoints, one will generate and one will validate an MBI number.
- url//generate_mbi/ will generate a valid MBI number following the MBI format since Jan 2020.
- url//validate_mbi/"mbi-num-to-validate" will validate that the characters follow the format

## Technologies
***
A list of technologies used within the project:
* [Flask](https://flask.palletsprojects.com)
* [Python](https://www.python.org/)


## Installation
***
May vary on system - This will be for MacOs 
```
$ git clone https://github.com/rkponn/mbi-api.git 
$ cd ../path/to/the/file
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python app.py
```

## FAQs
***
A list of frequently asked questions
1. **How do I generate a MBI Number?**
Go to url provided by your terminal, add */generate_mbi/*. 
2. **How do I validate a MBI Number?**
Go to url provided by your terminal, add */validate_mbi/number-To-validate*. 
