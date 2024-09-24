import requests
import os
from dotenv import load_dotenv

'''
아차사고 : 현재 CALL할 데이터가 없음
'''

##call api key 
load_dotenv()
nm_api_key = os.getenv('NM_API_KEY')

params = {
    'serviceKey': nm_api_key,
    'pageNo': 1,
    'numOfRows': 10,
    'returnType': 'JSON'
}

url = 'https://api.csi.go.kr/api/service/nms/nmsInfo?'
r = requests.get(url, params=params)

print(r.text)