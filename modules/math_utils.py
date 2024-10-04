from sklearn.covariance import EmpiricalCovariance, MinCovDet
import numpy as np

#covariance 계산 방법
#2차원 행렬로 반환해야 공분산 계산이 가능
#데이터에 이상치가 많을때 MinCovDet()
#데이터가 정규 분포를 따르고 이상치가 적을때 EmpiricalCovariance
def robust_cov(df) :
    #이상치를 배제한 후 데이터의 일부를 사용하여 공분산 행렬을 계산
    robust_cov = MinCovDet().fit(df)
    return robust_cov.covariance_

#마할라노비스 거리 구하기
def calculateMahalanobis(y=None, data=None, cov=None): 
  
    y_mu = y - np.mean(data, axis=0)  # 각 열(특성)의 평균으로 계산
    if cov is None: 
        cov = np.cov(data.T)
    else:
        cov = cov.T  # 공분산 계산

    # 공분산 행렬이 2차원인지 확인
    if cov.ndim == 1:
        raise ValueError("covariance matrix is 1-dimensional")

    # 공분산 행렬의 역행렬 계산
    inv_covmat = np.linalg.inv(cov)

    # 마할라노비스 거리 계산
    left = np.dot(y_mu, inv_covmat)
    mahal = np.dot(left, y_mu.T)
    
    return mahal
