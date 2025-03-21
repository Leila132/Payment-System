import requests
from dotenv import dotenv_values

config = dotenv_values()

class UserService:
    @staticmethod
    def get_user_from_token(token_key):
        if not token_key:
            return None
         
        response = requests.post(config['AUTH_API_URL'], json={"token": token_key})
        if response.status_code == 200:
            return response.json()
        return None