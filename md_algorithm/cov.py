import pandas as pd
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules import math_utils
import scipy as stats 
import numpy as np

# 공분산 매트릭스 계산
# gh_robust_cov_matrix, gh_empirical_cov_matrix = math_utils.robust_cov(gh_data)
# filtered_gh_robust_cov_matrix, filtered_gh_empirical_cov_matrix = math_utils.robust_cov(filtered_gh)
# kosha_robust_cov_matrix, kosha_empirical_cov_matrix = math_utils.robust_cov(kosha_data)

# gh 데이터 프레임 생성 및 CSV로 저장
#
# gh_save_df = pd.DataFrame({
#     'MCD (Robust)': gh_robust_cov_matrix,
#     'MLE': gh_empirical_cov_matrix
# })

# # filtering 데이터 프레임 생성 및 CSV로 저장
# filtered_gh_save_df = pd.DataFrame({
#     'MCD (Robust)': filtered_gh_robust_cov_matrix,
#     'MLE': filtered_gh_empirical_cov_matrix
# })

# # kosha 데이터 프레임 생성 및 CSV로 저장
# kosha_save_df = pd.DataFrame({
#     'MCD (Robust)': kosha_robust_cov_matrix,
#     'MLE': kosha_empirical_cov_matrix
# })

# # COV 데이터 저장
# gh_save_df.to_csv("./md_algorithm/data/gh_cov.csv", index=False)
# filtered_gh_save_df.to_csv("./md_algorithm/data/filtered_gh_cov.csv", index=False)
# kosha_save_df.to_csv("./md_algorithm/data/kosha_cov.csv", index=False)


  
#print(kosha_data['calculateMahalanobis'])


