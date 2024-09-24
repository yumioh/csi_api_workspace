import pandas as pd

'''
kosah (사고데이터)
- 공사 규모 => 5~9 : 소소, 10~50: 소, 100~500: 중, 500이상 :대
- 발생일자 => 요일 추출 
- 시간
- 출생년도 => 나이로 변경
- 근무일수
- 기상청 지점번호
- 월
'''


data = pd.read_excel("./md_algorithm/data/kosha_accident_cases_240924.xlsx")
print(data)