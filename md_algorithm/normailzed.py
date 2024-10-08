import pandas as pd
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules import math_utils

#kosha, gh 데이터 들고 오기 
kosha_df = pd.read_csv("./md_algorithm/data/kosha_categorize.csv")
#gh_df = pd.read_csv("./md_algorithm/data/gh_categorize.csv")
gh_df = pd.read_csv("./md_algorithm/data/gh_categorize_random.csv") #랜덤 데이터 파일 불려오기


#마할라로비스 계산한 kosha, gh 데이터 들고 오기
gh_md_df = pd.read_csv("./md_algorithm/data/gh_Mahal_list.csv", header = None)
kosha_md_df = pd.read_csv("./md_algorithm/data/kosha_Mahal_list.csv", header = None)

#컬럼별 항목 나누기
gh_filtered = pd.read_csv("./md_algorithm/data/filtered_gh.csv")

#마할라노비스 비교 데이터 값
test_robust_cov = math_utils.robust_cov(gh_filtered)

#구할 컬럼 
#coulmns = ["근무경력","나이","월별","요일별"]
coulmns = ["공사규모","발생시간","근무경력","나이"]

# print("-------------------kosha Mahalanobis 데이터 프레임으로 만들기--------------------")
# kosha_mal_df = math_utils.calc_mahalanobis_df(kosha_df, gh_filtered, coulmns, test_robust_cov)
# kosha_mal_df.to_csv("./md_algorithm/data/kosha_mahalanobis.csv", index=False)
# print(kosha_mal_df.head())
# print("-------------------gh Mahalanobis 데이터 프레임으로 만들기--------------------")
# gh_mal_df = math_utils.calc_mahalanobis_df(gh_df, gh_filtered, coulmns, test_robust_cov)
# gh_mal_df.to_csv("./md_algorithm/data/gh_mahalanobis.csv", index=False)
# print(gh_mal_df.head())

print("-------------------정규화 하기--------------------")

#컬럼명 들고 오기
#mal_columns = ["근무경력","나이","월별","요일별"] 
md_columns = ["공사규모","발생시간","근무경력","나이"]


#categorize data
gh_normalized = math_utils.normalize_columns(gh_df, coulmns) 
print(gh_normalized)

kosha_normalized = math_utils.normalize_columns(kosha_df, coulmns)
print(kosha_normalized)

#최종파일 만들기
kosha_file_path = "./md_algorithm/data/kosha_normalized.csv"
math_utils.normailzed(kosha_md_df, kosha_normalized, kosha_file_path)

gh_file_path = "./md_algorithm/data/gh_normalized.csv"
math_utils.normailzed(gh_md_df, gh_normalized, gh_file_path)






