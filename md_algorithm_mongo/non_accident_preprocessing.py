import pandas as pd

'''
출력일자 : yyyy-mm-dd로 수정
요일 : 출력일자로 요일 추출
생년월일 : 나이
건설업근무경력 : 근무경력으로 컬럼 변경
현장규모 : 공사규모로 변경
발생시간 : 동일하게 8시로 변경

'''

df = pd.read_csv("./md_algorithm_mongo/data/non_accidents_20241212.csv", index_col=None)
print(df.head())

