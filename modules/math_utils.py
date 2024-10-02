from sklearn.covariance import EmpiricalCovariance, MinCovDet

#covariance 계산 방법
def robust_cov(df) :
    # fit a MCD robust estimator to data
    robust_cov = MinCovDet().fit(df)
    # fit a MLE estimator to data
    emp_cov = EmpiricalCovariance().fit(df)
    print(
        "Estimated covariance matrix:\nMCD (Robust):\n{}\nMLE:\n{}".format(
            robust_cov.covariance_, emp_cov.covariance_
        )
    )
    return robust_cov.covariance_.flatten(),emp_cov.covariance_.flatten()