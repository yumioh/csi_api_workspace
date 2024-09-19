import pandas as pd
import datetime as dt
import re

board_info_df = pd.read_csv('./portal_info/data/board_info.csv', encoding="utf-8-sig")
print(f'공백 처리 전 : {board_info_df.shape}')
print(f'공백 처리 전 : {board_info_df["bbtContent"][:10]}')

#str인 type만 \n,\r이 포함된 경우 공백으로 처리
board_info_df["bbtContent"] = board_info_df["bbtContent"].apply(lambda x: re.sub(r'[\r\n]+', ' ', x) if isinstance(x, str) else x)

#공백 여러개인 경우 제거 
board_info_df["bbtContent"] = board_info_df["bbtContent"].apply(lambda x: re.sub(' +', ' ', x) if isinstance(x, str) else x)

print(f'공백 처리 후 : {board_info_df["bbtContent"][:10]}')

#공백 처리한 파일 저장
board_info_df.to_csv('./portal_info/data/board_info.csv', encoding="utf-8-sig")
