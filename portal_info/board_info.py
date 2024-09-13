import requests
from dotenv import load_dotenv
import pandas as pd
import sys, os # add the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules import api_utils

##call api key 
load_dotenv()
bd_api_key = os.getenv('BD_API_KEY')

params = {
    'serviceKey': bd_api_key,
    'pageNo': 2,
    'numOfRows': 100,
    'returnType': 'JSON'
}

url = 'https://api.csi.go.kr/api/service/com/comDataBbsInfo?'
res = requests.get(url, params)
bd_data = res.json()

#total page number
totalcnt = bd_data['response']['body']['totalCount']
page_cnt = api_utils.get_total_page(totalcnt)

for i in range(1,page_cnt+1):
    params = {
        'serviceKey': bd_api_key,
        'pageNo': i,
        'numOfRows': 100,
        'returnType': 'JSON'
    }
    res = requests.get(url, params)
    bd_data = res.json()
    bd_items = bd_data['response']['body']['items']
    bd_df = pd.DataFrame(bd_items)


print(bd_df)

# bd_items = bd_data['response']['body']['items']
# bd_items_df = pd.DataFrame(bd_items)
# bd_items_df.index = bd_items_df.index + 1
# print(bd_items_df.index)
# print(bd_items_df.head())

# #save online edu list : 45
# bd_items_df.to_csv('./portal_info/data/board_info.csv', encoding="utf-8-sig")
