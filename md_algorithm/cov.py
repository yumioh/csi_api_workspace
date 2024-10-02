import pandas as pd
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules import math_utils
import scipy as stats 
import numpy as np


#공분산에 해당하는 데이터 
gh_df = pd.read_csv("./md_algorithm/data/gh_categorize.csv")
kosha_df = pd.read_csv("./md_algorithm/data/kosha_categorize.csv")

print("-------------------cov값 구하기--------------------")
#라벨은 float type이 아니라서 제외
gh_data = gh_df[["공사규모","발생시간","근무경력","나이","월별","요일별"]]
print(gh_data.shape)

#TODO : 근무경력 5년 이상 공사규모 100인 이상 GH만 필터링 하기 
gh_data_2 = gh_data[gh_data["근무경력"] >= 6]
gh_data_2 = gh_data_2[gh_data["공사규모"] == 1]
print(gh_data_2.shape)
kosha_data = kosha_df[["공사규모","발생시간","근무경력","나이","월별","요일별"]]


# 공분산 매트릭스 계산
gh_robust_cov_matrix, gh_empirical_cov_matrix = math_utils.robust_cov(gh_data)
kosha_robust_cov_matrix, kosha_empirical_cov_matrix = math_utils.robust_cov(kosha_data)

# 데이터 프레임 생성 및 CSV로 저장
gh_save_df = pd.DataFrame({
    'MCD (Robust)': gh_robust_cov_matrix,
    'MLE': gh_empirical_cov_matrix
})

# 데이터 프레임 생성 및 CSV로 저장
kosha_save_df = pd.DataFrame({
    'MCD (Robust)': kosha_robust_cov_matrix,
    'MLE': kosha_empirical_cov_matrix
})

gh_save_df.to_csv("./md_algorithm/data/gh_cov.csv", index=False)
kosha_save_df.to_csv("./md_algorithm/data/kosha_cov.csv", index=False)

#TODO : calculateMahalanobis COV값 넣기 
print("-------------------calculateMahalanobis 구하기--------------------")

def calculateMahalanobis(y=None, data=None, cov=None): 
  
    y_mu = y - np.mean(data) 
    if not cov: 
        cov = np.cov(data.values.T) 
    inv_covmat = np.linalg.inv(cov) 
    left = np.dot(y_mu, inv_covmat) 
    mahal = np.dot(left, y_mu.T) 
    return mahal.diagonal() 
  

print(gh_robust_cov_matrix)
# create new column in dataframe that contains  
# Mahalanobis distance for each row 
# df['calculateMahalanobis'] = stats.mahalanobis(x=gh_df, data=gh_df[['Price', 'Distance', 
#                                                         'Emission','Performance', 
#                                                         'Mileage']])