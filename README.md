# Cyber Security Base 2024 Course Project

## Why?

This program is created as a part of the Cyber Security Base 2024 -course. The main reason being the identification and demonstration of OWASP Top 10 security vulnerabilities in a typical web application.  

## Usage

###  Running the program

0. Clone the reository and move to project directory: `git clone <repository_url_goes here>` and `cd project` 
1. Run the server: `python3 manage.py runserver` 
2. Test each vulnerability by setting `PATCHN = False` in the `project/med/views.py`-file. (N is an integer from 0 to 2)

## Vulnerabilities:

### 0. Injection

Client side data is not validated and quering others data is possible. 

Fix: We infer the user id from the request and therefore it is not given by user. 

### 1. Loggin

The program did not log any activity and therefore finding the previous vulnerability (1. Injection) was hard to identify. 

Fix: We created logging for the program. 

### 2. Broken access control

The previous change introduced a vulnerability that allowed anyone with the right request to see the program logs. 

Fix: We added a check to verify that logs are only visible to the admin users. 

   
