import requests
from dotenv import load_dotenv
import pandas as pd
import datetime as dt
import sys, os # add the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules import api_utils
'''
통합포털 - 자료실 서비스 : 상세 조회 
=> 현재 요청한 데이터가 없다라고 뜸
'''
# API 키 불러오기
load_dotenv()
acd_api_key = os.getenv('ACD_API_KEY')

#디렉토리값 불려오기 
base_dir = os.getenv('DATA_PATH', './CSI/CSI_API/')

#오늘날짜 불려오기 
date = dt.datetime.now().strftime("%y%m%d")

#게시판 정보 읽기
board_info = pd.read_csv('./portal_info/data/board_info.csv', encoding="utf-8-sig", )

#게시판 아이디 들고 오기 
total_board = board_info["bbtNo"]

# 페이지 번호 초기화 및 데이터 저장 리스트 초기화
i = 1
all_data = []
#url = 'https://api.csi.go.kr/api/service/com/comDataBbsInfo/{bbtNo}?'
for bbtNo in total_board[:10] : 
    url = f'https://api.csi.go.kr/api/service/com/comDataBbsInfo/{bbtNo}?'
    params = {
        'serviceKey': acd_api_key,
        'numOfRows': 100,
        'returnType': 'JSON'
    }
    res = requests.get(url, params)
    detail_data = res.json()
    print(detail_data)

    detail_item = detail_data['response']['body']['items']
    #all_data.extend(detail_item)

print(all_data)
