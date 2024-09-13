import pandas as pd

data = pd.read_csv('./portal_info/data/board_info.csv', encoding="utf-8-sig")
print(data.shape)