import pandas as pd
import math
import sys, os
import csv
import matplotlib.pyplot as plt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules import math_utils


kosha_df = pd.read_csv("./md_algorithm/data/kosha_categorize.csv")
gh_df = pd.read_csv("./md_algorithm/data/gh_categorize.csv")

#컬럼별 항목 나누기
gh_filtered = pd.read_csv("./md_algorithm/data/filtered_gh.csv")

print("-------------------kosha 항목별 Mahalanobis 구하기--------------------")

coulmns = ["근무경력","나이","월별","요일별"]

#마할라노비스 비교 데이터 값
test_robust_cov = math_utils.robust_cov(gh_filtered)

#values 인덱스나 컬럼 이름 없이 순수한 데이터 값만 포함
for column in coulmns:
    kosha_list = []
    kosha = kosha_df[column].values
    for kosha_value in kosha:
        kosha_data = math_utils.calculateMahalanobis(kosha_value, gh_filtered.values, test_robust_cov)
        kosha_list.append(kosha_data)

 # 결과를 컬럼 이름에 맞춰 파일로 저장
    file_name = f"./md_algorithm/data/kosha_Mahal_{column}.csv"
    with open(file_name, "w", newline='') as file:
        writer = csv.writer(file)
        for item in kosha_list:
            writer.writerow([item])
        print(kosha_list[:10])

print("-------------------gh Mahalanobis 구하기--------------------")

for column in coulmns:
    gh_list = []
    gh = gh_df[column].values
    for gh_value in gh:
        gh_data = math_utils.calculateMahalanobis(gh_value, gh_filtered.values, test_robust_cov)
        gh_list.append(gh_data)

    #결과 파일 저장
    file_name = f"./md_algorithm/data/gh_Mahal_{column}.csv"
    with open(file_name, "w", newline='') as file:
        writer = csv.writer(file)
        for item in gh_list:
            writer.writerow([item])
    print(gh_list[:10])