import numpy as np
import pandas as pd
import sys, os
from modules import math_utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules import math_utils

#공분산에 해당하는 데이터 
gh_df = pd.read_csv("./md_algorithm/data/gh_categorize.csv")
kosha_df = pd.read_csv("./md_algorithm/data/kosha_categorize.csv")

print("-------------------cov값 구하기--------------------")
#라벨은 float type이 아니라서 제외
gh_data = gh_df[["공사규모","발생시간","근무경력","나이","월별","요일별"]]
print("gh data : ", gh_data.shape)

#근무경력 5년 이상만 필터링 : 535개
# 2-4시로 변경
filtered_gh = gh_data[gh_data["근무경력"] >= 7]
filtered_gh["발생시간"] = 1
print("filtered gh data : ", filtered_gh.shape)
print("filtered gh data :", filtered_gh.head())

#필터링한 개수랑 맞춰주기 위함 
gh_data = gh_data.sample(n=535)
print("gh sample data : ", gh_data.shape)

#kosha data
kosha_data = kosha_df[["공사규모","발생시간","근무경력","나이","월별","요일별"]]
print("kosha data : ", kosha_data.shape)

print("-------------------kosha calculateMahalanobis 구하기--------------------")

kosha_data['calculateMahalanobis']= math_utils.calculateMahalanobis(kosha_data, kosha_data)
kosha_data.to_csv("./md_algorithm/data/kosha_Mahal.csv", encoding="utf-8")

print("-------------------gh calculateMahalanobis 구하기--------------------")

print("filterd_gh : ", filtered_gh.shape)
print("gh_data : ", gh_data.shape)

gh_data['calculateMahalanobis']= math_utils.calculateMahalanobis(gh_data[["근무경력","나이","월별","요일별"]], filtered_gh[["근무경력","나이","월별","요일별"]])
gh_data.to_csv("./md_algorithm/data/gh_Mahal.csv", encoding="utf-8")

mahalanobis_distances_gh = gh_data['calculateMahalanobis']