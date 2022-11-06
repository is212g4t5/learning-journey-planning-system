# learning-journey-planning-system
IS212 SPM G4T5 Learning Journey Planning System (2022 Semester 1)

## Before Starting: 
Make sure the following requirements are installed on your machine:
1. Python
https://www.python.org/downloads/
2. Node.js
https://nodejs.org/en/

## To run the backend file:
0. `cd backend`
1. `pip install -r requirements.txt` //install all dependencies required
2. open WAMP/MAMP and start the server
3. go to localhost/phpmyadmin to check on the database if required
4. `python request_handler.py` //to run the file

## To test API:
5. make sure request handler is up and running 
6. open Postman
7. set the method(POST/GET/UPDATE/DELETE etc.) and use the host address, e.g. 127.0.0.1:5000/<api endpoint> from running local server to make a request. make sure any neccessary body is added

## To Load and Run Database: 
1. Make sure you have WAMP installed (for Windows) or MAMP (for MacOS)
2. Start WAMP/MAMP and turn it on
3. Access either localhost/phpmyadmin/ on your browser or MySQLWorkBench and load SQL script from "dumpV3 with LMS data.sql"
4. Check that data is loaded in the 'ljps' database
  
## To run automated tests (Pytest):
0. `pip install pytest` //if not previously installed
1. `cd backend`
2. `Pytest tests` or `python -m pytest tests` //run all tests in test folder, `python -m pytest tests/functional` to run files in functional folder only etc.
Some important notes:
- `conftest.py` includes fixtures which can be added as params in test functions, they are typically configurations that are repeatedly used and have scopes `function`,`module`,`session`.
- each and all test cases should be inside a def test_function() with prefix `test` //test is a identifier keyword in pytest, don't add test_ in front of utility functions
- db data cleanup is required before/after each test, improper db handling may crash the test on 2nd run or affect other tests. To test get/delete/update, we need to load data into db using db insert methods and NOT post api to add data as it will affect reliability of API test
- scopes: function = 1 function, module = 1 file, session = entire round of tests.  
    
Some materials for reference:  
https://testdriven.io/blog/flask-pytest/  
https://circleci.com/blog/testing-flask-framework-with-pytest/

## To run frontend files:
0. `cd frontend`
1. `npm i` OR `npm install` //install all dependencies required
2. `npx quasar dev`

## Troubleshooting package installation(requirements.txt) issues:
1. if `pip install -r requirements.txt` throws error about mysql configs
2. try checking versions of packages in requirements.txt using the `pip show <package>` command
3. try checking flask version with `pip show flask`
4. if version is older than the one in requirements.txt, try `pip install flask==2.2.2` //or whichever version is in the requirements.txt
5. now try `pip install -r requirements.txt` again //this was resolved for me after updating flask
you may want to try updating pip `pip install --upgrade pip` as well

## Troubleshooting API issues:
postman or API call gives some SQL error about "trailing /"
1. try following the instructions above about package issues
2. try adding a `/` to your call url, i.e. `/api/skills/` instead of `/api/skills`
  
