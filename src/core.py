from dotenv import dotenv_values
import requests as req
from datetime import datetime, timedelta
from tzlocal import get_localzone
import pytz, json
from utils import *


# gets the time offset of local from utc
def get_time_offset() -> timedelta:
    tz = get_localzone()
    d = datetime.now(tz)  # or some other local date
    utc_offset = d.utcoffset()
    return utc_offset


class SimCo:
    session = req.Session()

    def __init__(self, email, password):
        self._email = email
        self._password = password
        if not self.login():
            logc("a problem occured logging in. please verify the login info")
        else:
            logi("login successful")

    # return: success or failure of login operation
    def login(self) -> bool:
        login_url = "https://www.simcompanies.com/signin/"
        api_login_url = "https://www.simcompanies.com/api/v2/auth/email/auth/"

        self.session.get(login_url)
        csrftoken = self.session.cookies["csrftoken"].strip()
        login_data = json.dumps(
            dict(
                email=self._email,
                password=self._password,
                timezone_offset=get_time_offset().seconds / -60,
            )
        )

        headers = {
            "X-CSRFToken": csrftoken,
            "Host": "www.simcompanies.com",
            "Referer": "https://www.simcompanies.com/",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        }

        login_req = self.session.post(api_login_url, data=login_data, headers=headers)

        logi("login request status code: {}".format(login_req.status_code))
        return login_req.status_code == 200

    def get_cookies(self) -> dict:
        return self.session.cookies.get_dict()

    # param path: path of api call
    # example: v2/resources/
    def get_api(self, path: str) -> dict:
        root_api_url = "https://www.simcompanies.com/api/"
        if path.startswith("/"):
            path = path.removeprefix("/")
        r = self.session.get(root_api_url + path)
        return json.loads(r.text)

    def set_password(self, password: str):
        self._password = password

    def set_email(self, email: str):
        self._email = email
