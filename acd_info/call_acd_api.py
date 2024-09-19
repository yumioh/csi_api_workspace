import requests
from dotenv import load_dotenv
import pandas as pd
import datetime as dt
import sys, os # add the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules import api_utils

'''
사고사례 : 목록 조회
'''

# API 키 불러오기
load_dotenv()
acd_api_key = os.getenv('ACD_API_KEY')

#오늘날짜 불려오기 
date = dt.datetime.now().strftime("%y%m%d")

# 페이지 번호 초기화 및 데이터 저장 리스트 초기화
i = 1
all_data = []
url = 'https://api.csi.go.kr/api/service/com/comDataBbsInfo?'

params = {
        'serviceKey': acd_api_key,
        'pageNo': i,
        'numOfRows': 10,
        'returnType': 'JSON'
    }

res = requests.get(url, params)
bd_data = res.json()
print(bd_data)