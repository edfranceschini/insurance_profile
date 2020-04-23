## INSURANCE PROFILE
<p align="center">
    <img src="https://travis-ci.org/RafaelFTeixeira/risk_profile.svg?branch=master" alt="Build Status">
    <a href="https://codecov.io/gh/RafaelFTeixeira/risk_profile" target="_blank">
        <img src="https://codecov.io/gh/RafaelFTeixeira/risk_profile/branch/master/graph/badge.svg" alt="Coverage">
    </a>
<p>
    Origin take home assigment

# Getting Started
 -  install dependencies
    -	`pip install -r requirements.txt`
 -  run the project
    -  `uvicorn main:app --reload`

# Documentation API
 -  `http://localhost:8000`
 -  `http://localhost:8000/redoc`

# Run tests
 -  install dependencies
    -  `pip install -r requirements/dev.txt`
 - run all tests
    -  `pytest`
-  code coverage:
    -  `pytest --cov=domain --cov=api --cov-report=term-missing ${@}`
