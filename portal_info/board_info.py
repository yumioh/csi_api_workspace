import requests
from dotenv import load_dotenv
import pandas as pd
import sys, os # add the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules import api_utils

# API 키 불러오기
load_dotenv()
bd_api_key = os.getenv('BD_API_KEY')

# 페이지 번호 초기화 및 데이터 저장 리스트 초기화
i = 1
all_data = []
url = 'https://api.csi.go.kr/api/service/com/comDataBbsInfo?'

# 무한 루프 시작
while True:
    params = {
        'serviceKey': bd_api_key,
        'pageNo': i,
        'numOfRows': 100,
        'returnType': 'JSON'
    }
    res = requests.get(url, params)
    bd_data = res.json()

    # 결과 코드 확인
    resultCode = bd_data['response']['header']['resultCode']
    
    # 성공 코드인 "00"이 아닐 경우 반복 중단
    if resultCode != "00":
        print(f"Error: resultCode {resultCode}. Stopping the loop.")
        break

    # 현재 페이지 출력
    print("------------------------------------")
    print(f'현재 PAGE : {i}')

    # 데이터 가져오기
    bd_items = bd_data['response']['body']['items']
    all_data.extend(bd_items)  # 리스트에 데이터 추가

    # 다음 페이지로 넘어가기
    i += 1

# 최종 DataFrame으로 변환 후 CSV 저장
bd_df = pd.DataFrame(all_data)
print(bd_df.shape)
bd_df.to_csv('./portal_info/data/board_info.csv', encoding="utf-8-sig")

print("데이터 수집 완료 및 저장.")
