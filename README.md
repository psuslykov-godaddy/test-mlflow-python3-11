# Testing the loading models from MLflow using Python 3.11

1. Clone the repository
2. Install the project dependencies
```poetry install```
3. Log into **Stage** AWS account
```
eval $(aws-okta-processor authenticate --environment --user UPDATE_YOUR_USER --organization godaddy.okta.com)
```
4. Run the script
```
poetry run python test.py
```