import pandas as pd
import sys, os
import numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules import math_utils

#kosha, gh 데이터 들고 오기 
kosha_df = pd.read_csv("./md_algorithm/data/kosha_categorize.csv")
#gh_df = pd.read_csv("./md_algorithm/data/gh_categorize.csv")
gh_df = pd.read_csv("./md_algorithm/data/gh_categorize_random.csv") #랜덤 데이터 파일 불려오기

#마할라로비스 계산한 kosha, gh 데이터 들고 오기
gh_md_df = pd.read_csv("./md_algorithm/data/gh_Mahal_list.csv", header = None)
kosha_md_df = pd.read_csv("./md_algorithm/data/kosha_Mahal_list.csv", header = None)
#print(gh_md_df)

#이상치 제거
outlier_gh_md = gh_md_df[(abs((gh_md_df[0] - gh_md_df[0].mean()) / gh_md_df[0].std()) > 1.96)].index
gh_md_filtered = gh_md_df.drop(outlier_gh_md)
print(gh_md_filtered)

outlier_kosha_md = kosha_md_df[(abs((kosha_md_df[0] - kosha_md_df[0].mean()) / kosha_md_df[0].std()) > 1.96)].index
kosha_md_filtered = kosha_md_df.drop(outlier_kosha_md)
print(kosha_md_filtered)


#컬럼별 항목 나누기
gh_filtered = pd.read_csv("./md_algorithm/data/filtered_gh.csv")

print("-------------------MD 데이터 정규화 하기--------------------")

#gh normalize 
gh_normalized = math_utils.normalize(gh_md_df, kosha_md_df)
gh_normalized.to_csv("./md_algorithm/data/gh_normalized.csv", index=False)
#print(gh_normalized.shape)                                                                                                                                                                                                                                                            

#kosha normalize
kosha_normalized = math_utils.normalize(kosha_md_df, gh_md_df)
kosha_normalized.to_csv("./md_algorithm/data/kosha_normalized.csv", index=False)
#print(kosha_normalized.shape)

print("-------------------이상치 제거한 MD 데이터 정규화 하기--------------------")

#gh normalize 
gh_oustline_normalized = math_utils.normalize(gh_md_filtered, kosha_md_filtered)
gh_oustline_normalized.to_csv("./md_algorithm/data/gh_outline_normalized.csv", index=False)
#print(gh_oustline_normalized)                                                                                                                                                                                                                                                            

#kosha normalize
kosha_oustline_normalized = math_utils.normalize(kosha_md_filtered, gh_md_filtered)
kosha_oustline_normalized.to_csv("./md_algorithm/data/kosha_outline_normalized.csv", index=False)
#print(kosha_oustline_normalized.shape)


print("-------------------log 데이터 정규화 하기--------------------")

gh_log = np.log(gh_md_df)
kosha_log = np.log(kosha_md_df)

gh_log_normalized = math_utils.normalize(gh_log, kosha_log)
kosha_log_normalized = math_utils.normalize(kosha_log, gh_log)

gh_log_normalized.to_csv("./md_algorithm/data/gh_normalized_log.csv", index=False)
kosha_log_normalized.to_csv("./md_algorithm/data/kosha_normalized_log.csv", index= False)


print("-------------------이상치 제거한 log 데이터 정규화 하기--------------------")

gh_log = np.log(gh_md_filtered)
kosha_log = np.log(kosha_md_filtered)
print(gh_log.head())
print(kosha_log.head())

gh_log_normalized = math_utils.normalize(gh_log, kosha_log)
kosha_log_normalized = math_utils.normalize(kosha_log, gh_log)

gh_log_normalized.to_csv("./md_algorithm/data/gh_outline_normalized_log.csv", index=False)
kosha_log_normalized.to_csv("./md_algorithm/data/kosha_outline_normalized_log.csv", index= False)


