import requests
import os
from dotenv import load_dotenv
import pandas as pd
import datetime as dt

'''
사용자교육 - 온라인교육강의서비스 : 목록 조회
'''

#call api key 
load_dotenv()
edu_api_key = os.getenv('EDU_API_KEY')

#디렉토리값 불려오기 
base_dir = os.getenv('DATA_PATH', './CSI/CSI_API/')

#오늘날짜 불려오기 
date = dt.datetime.now().strftime("%y%m%d")


params = {
    'serviceKey': edu_api_key,
    'pageNo': 1,
    'numOfRows': 100,
    'returnType': 'JSON'
}

# 페이지 번호 초기화 및 데이터 저장 리스트 초기화
i = 1
all_data = []
url = "https://api.csi.go.kr/api/service/edu/onlineEduInfo?"


while True:
    params = {
        'serviceKey': edu_api_key,
        'pageNo': i,
        'numOfRows': 100,
        'returnType': 'JSON'
    }
    res = requests.get(url, params)
    edu_data = res.json()

    print(edu_data)

    # 결과 코드 확인
    resultCode = edu_data['response']['header']['resultCode']
    
    # 성공 코드인 "00"이 아닐 경우 반복 중단
    if resultCode != "00":
        print(f"Error: resultCode {resultCode}. Stopping the loop.")
        break

    # 현재 페이지 출력
    print("------------------------------------")
    print(f'현재 PAGE : {i}')

    # 데이터 가져오기
    edu_items = edu_data['response']['body']['items']
    all_data.extend(edu_items)  # 리스트에 데이터 추가

    # 다음 페이지로 넘어가기
    i += 1

# 최종 DataFrame으로 변환 후 CSV 저장
edu_df = pd.DataFrame(all_data)
print(f'board info shape  : {edu_df.shape}')

edu_df.to_csv(f'./portal_info/data/board_info_{date}.csv', encoding="utf-8-sig")
print("데이터 수집 완료 및 저장")

#파일로 저장
file_path = os.path.join(base_dir, 'edu_list_info.csv')
edu_df.to_csv(file_path, encoding="utf-8-sig")

