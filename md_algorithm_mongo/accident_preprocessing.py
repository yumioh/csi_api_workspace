import pandas as pd

'''
출생년도 : 나이로 수정
발생일자 : 사고날짜 
근무일수 : 근무경력으로 변경
발생일자 : 요일 추출
'''

df = pd.read_csv("./md_algorithm_mongo/data/accidents_20241212.csv", index_col=None)
print(df.head())

