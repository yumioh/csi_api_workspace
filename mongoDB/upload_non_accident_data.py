import os
import sys
import json
import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime

load_dotenv()
mongo_db = os.getenv('MONGO_DB')

boryeong_file = "./mongoDB/data/boryeong_nonaccident_cases.xlsx"

db = MongoClient(mongo_db)

# 디비생성 => 데이터를 삽인 전까지 데이터베이스나 컬렉션 생성이 안됨 
# 다만 명시적으로 컬렉션 생성 가능 (create_collection)
accident_collection = db['accident_data']
#테이블 생성
non_accident_document = accident_collection['non_accidents']

#파일 문자열로 읽기 
read_raw_data = pd.read_excel(boryeong_file, dtype=str) 

# MongoDB에 데이터 삽입 (DataFrame을 딕셔너리 리스트로 변환)
data_to_insert = read_raw_data.to_dict(orient='records') 

#mongoDB에 데이터 넣기
non_accident_document.insert_many(data_to_insert)

db.close()
sys.exit()
