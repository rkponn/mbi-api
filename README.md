# MBI Validator and Generator - (Medicare Beneficiary Identifier/Identification)

## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [FAQs](#faqs)

### General Info
***
This project is an API created with Flask and Python. It will host 2 endpoints that can be called
which will validate based on the Jan 2020 standard provided by [CMS (Centers for Medicare and Medicaid Services)](https://www.cms.gov/Medicare/New-Medicare-Card). Generating an MBI will give a random but valid string of characters. Validating will ensure that the standards are used, a user can type in their own characters and it will give a True or False based on the validity of the string.



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
