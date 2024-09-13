import requests
import os
from dotenv import load_dotenv
import pandas as pd

#call api key 
load_dotenv()
edu_api_key = os.getenv('EDU_API_KEYS')

params = {
    'serviceKey': edu_api_key,
    'pageNo': 1,
    'numOfRows': 100,
    'returnType': 'JSON'
}

url = "https://api.csi.go.kr/api/service/edu/onlineEduInfo?"

res = requests.get(url, params)
edu_data = res.json()
edu_items = edu_data['response']['body']['items']
edu_list_df = pd.DataFrame(edu_items)
edu_list_df.index = edu_list_df.index + 1
print(edu_list_df.index)
print(edu_list_df.head())

#save online edu list : 45
edu_list_df.to_csv('./edu_info/data/edu_info.csv', encoding="utf-8-sig")