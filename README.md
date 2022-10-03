# learning-journey-planning-system
IS212 SPM G4T5 Learning Journey Planning System (2022 Semester 1)


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
