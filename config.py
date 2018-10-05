'''
This extracts variables from the code base to one file.
To replace variables with environment variables
- remove static value with `os.environ['ENV_VARIABLE_NAME']`
- add an environment variable to your host
    export ENV_VARIABLE_NAME='value'
EX.
environment = os.environ['PLEX_AUTOCOLLECTIONS_ENV']
username = os.environ['PLEX_AUTOCOLLECTIONS_USER']
password = os.environ['PLEX_AUTOCOLLECTIONS_PASSWORD']
''' 

environment = 'dev'
username = 'myusername'
password = 'mypassword'
