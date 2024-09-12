import requests
import os
from dotenv import load_dotenv

##call api key 
load_dotenv()
token_key = os.getenv('NM_API_KEYS')


url = ""