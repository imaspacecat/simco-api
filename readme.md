# simco-api
## Description
allows one to programmatically log into [simco](https://www.simcompanies.com/) and make calls to the api through a layer of abstraction

in addition, there is a simple cli that allows making direct requests to the api through the commandline


## Installation
1. clone the repo
```shell
git clone https://github.com/imaspacecat/simco-api
```
2. make a virtual environment
```shell
python3 -m venv venv
```

3. install the requirements
```shell
pip -r requirements.txt 
```
4. create .env with login info in the root of the project
```env
EMAIL= # my simco email here
PASSWORD= # my simco password here
```

## How to use the library
```python
# import SimCo
from core import SimCo
from dotenv import dotenv_values
import json
# get login info from .env as a dict
# this can be hard coded but is generally considered a bad practice
env_data = dotenv_values(".env")

email = env_data["EMAIL"]
password = env_data["PASSWORD"]

# create SimCo object to perform api calls with. 
# multiple SimCo objects can be created with independant user sessions
sim = SimCo(email, password)

# make call to the api providing the path as a param
data = sim.get_api("/v2/companies/me/")
# print the newly acquired response to stdout with pretty printing
print(json.dumps(data, indent=4))
```

## How to use the cli
### command definition
- get \<api_path>
    - example: `get /v2/companies/me/`
    - description: gets the result of the api call and prints it to stdout

- set-email \<email>
    - example: `set-email simco@simcompanies.com`
    - description: set the email that will be used to log in

- set-password \<password>
    - example: `set-password 123456`
    - description: set the password that will be used to log in 

all commands must be passed as arguments to python. examples:
```shell
python cli.py set-password shrekforlife
python cli.py get /v2/companies/me/
```


