
from dotenv import load_dotenv
import os
import requests
import json
import uuid

# Load environment variables from .env file
load_dotenv()

class Auth:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.device_id = self.generate_device_id()
        self.token = None

    @staticmethod
    def generate_device_id():
        return str(uuid.uuid4()).upper()

    def create_token(self):
        request_data = {
            "email": self.email,
            "password": self.password,
            "clientType": "CLIENT_TYPE_IOS",
            "returnSecureToken": True
        }

        url = os.getenv("GOOGLE_AUTH_URL")
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "User-Agent": "FirebaseAuth.iOS/10.23.1 com.locket.Locket/1.82.0 iPhone/18.0 hw/iPhone12_1",
            "X-Client-Version": "iOS/FirebaseSDK/10.23.1/FirebaseCore-iOS",
            "X-Firebase-AppCheck": os.getenv("FIREBASE_APPCHECK"),
            "X-Firebase-GMPID": os.getenv("FIREBASE_GMPID"),
            "X-Ios-Bundle-Identifier": os.getenv("IOS_BUNDLE_IDENTIFIER")
        }

        response = requests.post(url, headers=headers, json=request_data)

        if response.ok:
            self.token = response.json().get('idToken')
            return self.token
        else:
            raise Exception('Failed to login')

    def get_token(self):
        if not self.token:
            self.create_token()
        return self.token

class LocketAPI:
    def __init__(self, token):
        self.token = token
        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-GB,en;q=0.9',
            'Authorization': f'Bearer {self.token}',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'X-Client-Version': 'iOS/FirebaseSDK/10.23.1/FirebaseCore-iOS',
            'X-Firebase-GMPID': os.getenv("FIREBASE_GMPID"),
            'X-Ios-Bundle-Identifier': os.getenv("IOS_BUNDLE_IDENTIFIER"),
            'X-Firebase-AppCheck': os.getenv("FIREBASE_APPCHECK")
        }

    def getUserByUsername(self, username):
        if not username:
            raise ValueError("Username is required")

        request_payload = {
            "data": {
                "username": username,
            }
        }

        response = requests.post(
            'https://api.locketcamera.com/getUserByUsername',
            headers=self.headers,
            json=request_payload
        )

        if response.ok:
            return response.json()
        else:
            raise Exception(f'API request failed with status code {response.status_code}: {response.text}')

    def changeNameAccount(self, last="", first=""):
        request_payload = {
            "data": {
                "last_name": last,
                "first_name": first,
            }
        }

        response = requests.post(
            'https://api.locketcamera.com/changeProfileInfo',
            headers=self.headers,
            json=request_payload
        )

        if response.ok:
            return response.json()
        else:
            raise Exception(f'API request failed with status code {response.status_code}: {response.text}')

    def GetAccountInfo(self):
        url = os.getenv("GOOGLE_ACCOUNT_INFO_URL")
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en",
            "Content-Type": "application/json",
            "User-Agent": "FirebaseAuth.iOS/10.23.1 com.locket.Locket/1.82.0 iPhone/18.0 hw/iPhone12_1",
            "X-Client-Version": "iOS/FirebaseSDK/10.23.1/FirebaseCore-iOS",
            "X-Firebase-GMPID": os.getenv("FIREBASE_GMPID"),
            "X-Ios-Bundle-Identifier": os.getenv("IOS_BUNDLE_IDENTIFIER")
        }
        request_payload = {
            "idToken": self.token
        }

        response = requests.post(url, headers=headers, json=request_payload)

        if response.ok:
            return response.json()
        else:
            raise Exception(f'API request failed with status code {response.status_code}: {response.text}')

    def getLastMoment(self):
        request_payload = {
            "data": {
                "excluded_users": [],
                "fetch_streak": False,
                "should_count_missed_moments": True
            }
        }

        response = requests.post(
            'https://api.locketcamera.com/getLatestMomentV2',
            headers=self.headers,
            json=request_payload
        )

        if response.ok:
            return response.json()
        else:
            raise Exception(f'API request failed with status code {response.status_code}: {response.text}')

if __name__ == "__main__":
    email = os.getenv("USER_EMAIL")
    password = os.getenv("USER_PASSWORD")

    auth = Auth(email, password)
    token = auth.get_token()

    api = LocketAPI(token)

    account_info = api.GetAccountInfo()
    # print(json.dumps(account_info, indent=4))
    moment = api.getLastMoment()
    print(moment)
