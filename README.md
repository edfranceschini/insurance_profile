## INSURANCE PROFILE
<p align="center">
    <img src="https://travis-ci.com/edfranceschini/insurance_profile.svg?branch=master" alt="Build Status">
    <a href="https://codecov.io/gh/edfranceschini/insurance_profile" target="_blank">
        <img src="https://codecov.io/gh/edfranceschini/insurance_profile/branch/master/graph/badge.svg" alt="Coverage">
    </a>
<p>
    Origin take home assigment

# Getting Started
 -  install requirements
    -	`pip install -r requirements.txt`
 -  run the project
    -  `uvicorn main:app `

# Documentation API
 -  `http://localhost:8000`
 -  `http://localhost:8000/redoc`

# Run tests
 -  install dependencies
    -  `pip install -r requirements/development.txt`
 - run all tests
    -  `pytest`
-  code coverage:
    -  `pytest --cov=domain --cov=api --cov-report=term-missing ${@}`
