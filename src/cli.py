from dotenv import dotenv_values
import core
import json, sys


def help():
    print(
        """
get <api_path>
    example: get /v2/companies/me/
    description: gets the result of the api call and prints it to stdout
\nset-email <email>
    example: set-email simco@simcompanies.com
    description: set the email that will be used to log in
\nset-password <password>
    example: set-password 123456
    description: set the password that will be used to log in 
"""
    )


def handle_cmds(cmd: str):
    if cmd == "help":
        help()
        return
    arg2 = sys.argv[2]
    if cmd == "get":
        print(json.dumps(sim.get_api(arg2), indent=4))
    elif cmd == "set-email":
        with open(".env", "w") as f:
            f.write("EMAIL=" + arg2 + "\nPASSWORD=" + password)
            print('set email to "{}"'.format(arg2))
    elif cmd == "set-password":
        with open(".env", "w") as f:
            f.write("EMAIL=" + email + "\nPASSWORD=" + arg2)
            print('set password to "{}"'.format(arg2))
    else:
        print("command does not exist")


env_data = dotenv_values(".env")
email = env_data["EMAIL"]
password = env_data["PASSWORD"]

sim = core.SimCo(email, password)

num_args = len(sys.argv)

if email == None:
    print('please set the login email using set-email "<email>"')
if password == None:
    print('please set the login email using set-password "<password>"')

if len(sys.argv) > 1:
    cmd = sys.argv[1]
    handle_cmds(cmd)
