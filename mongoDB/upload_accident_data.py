import os
import sys
import json
import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
mongo_db = os.getenv('MONGO_DB')

csi_file = "./mongoDB/data/csi_accident_cases_240915.xlsx"
# kosha_file = "./mongoDB/data/kosha_accident_cases.xlsx"

db = MongoClient(mongo_db)

#디비 생성 => 데이터를 삽인 전까지 데이터베이스나 컬렉션 생성이 안됨 
#다만 명시적으로 컬렉션 생성 가능 (create_collection)
accident_collection = db['accident_data']

#테이블 생성
accident_document = accident_collection['accidents']

#파일 읽기 
read_raw_data = pd.read_excel(csi_file, dtype=str)

data_to_insert = read_raw_data.to_dict(orient='records')

accident_document.insert_many(data_to_insert) # 배열형태의 다수의 데이터를 삽입

db.close()
sys.exit()
