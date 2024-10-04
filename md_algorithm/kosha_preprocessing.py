import pandas as pd
import datetime as dt
import sys, os # add the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules import category_utils

'''
kosah (사고데이터)
- 공사 규모 => 5~9 : 소소, 10~50: 소, 100~500: 중, 500이상 :대
- 발생일자 => 요일 추출 
- 발생시간
- 출생년도 => 나이로 변경
- 근무일수
- 기상청 지점번호
- 월
'''

kosha_df = pd.read_excel("./md_algorithm/data/kosha_accident_cases_240924.xlsx")
print("KOSHA DATA", kosha_df)
print("KOSHA DATA INFO : ", kosha_df.info())

#NA값 제거 
kosha_df = kosha_df.dropna(axis=0)
print("KOSHA DATA", kosha_df)
print("KOSHA DATA INFO : ", kosha_df.info())

#공사규모 변환1992
kosha_df["공사규모"] = kosha_df["공사규모"].apply(category_utils.convert_scale_to_person_range)
print("공사규모 : ", kosha_df[:10])

#날짜 데이터 요일로 변환
kosha_df["날짜"] = pd.to_datetime(kosha_df["날짜"])
kosha_df["요일별"] = kosha_df["날짜"].dt.day_name()
kosha_df["요일별"] = kosha_df["요일별"].apply(category_utils.day_to_korean)

#날짜 데이터 mon만 추출
kosha_df["월별"] = kosha_df["날짜"].dt.month

#사고 발생일자 기준으로 나이 계산
kosha_df["나이"] = kosha_df["발생일자"].dt.year - kosha_df["출생년도"].astype(int)
#print(kosha_df.head())

#레이블 값 추가 
kosha_df["라벨"] = "label2"

#컬럼명 변경
kosha_df.rename(columns={'경력일수':'근무경력'}, inplace=True)

#데이터 저장
kosha_df[["공사규모","발생시간","근무경력","나이","월별","요일별","라벨"]].to_csv("./md_algorithm/data/kosha_preprocessing.csv", encoding="utf-8",index=False)
print("저장할 데이터 head :", kosha_df.head())
print("저장할 데이터 shape :", kosha_df.shape)