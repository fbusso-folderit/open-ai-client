import os

from dotenv import load_dotenv


class Environment:
    _instance = None

    def __new__(cls):
        if Environment._instance is None:
            Environment._instance = object.__new__(cls)
        return Environment._instance

    def __init__(self):
        if not hasattr(self, 'OPEN_AI_API_KEY'):
            load_dotenv()
            self.OPEN_AI_API_KEY = os.getenv('OPEN_AI_API_KEY')
