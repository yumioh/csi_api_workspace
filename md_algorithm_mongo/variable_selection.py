import pandas as pd
from scipy.stats import ttest_ind
from scipy.stats import mannwhitneyu
from statsmodels.multivariate.manova import MANOVA
from sklearn.ensemble import RandomForestClassifier


non_accidents_df = pd.read_csv("./md_algorithm_mongo/data/non_accidents_preprocessing.csv")
accidents_df = pd.read_csv("./md_algorithm_mongo/data/accidents_preprocessing.csv")

print(non_accidents_df.describe())
print(accidents_df.describe())
# print(non_accidents_df.head())

variables = ['나이', '근무경력', '발생시간', '공사규모', "발생월", "발생요일"]

#t검정 하기 : 두 집단의 평균 비교하여 유의미한 변수 추출
selected_vars = []
for var in variables:
    t_stat, p_value = ttest_ind(accidents_df[var], non_accidents_df[var], equal_var=False)
    if p_value < 0.05:  # 유의 수준 5%
        selected_vars.append(var)
        print(f"{var}: t-stat = {t_stat:.2f}, p-value = {p_value:.3f} (유의미)")
    else:
        print(f"{var}: t-stat = {t_stat:.2f}, p-value = {p_value:.3f} (유의미하지 않음)")

print("유의미한 변수:", selected_vars)


#윌콕스 부호 순위 검정 : 비모수검정으로 두 집단 간 순위 차이 비교
results = {}
for var in variables:
    try:
        # 두 그룹의 해당 변수 추출
        non_accident_group = non_accidents_df[var].dropna()
        accident_group = accidents_df[var].dropna()

        # Wilcoxon Rank-Sum Test
        stat, p = mannwhitneyu(non_accident_group, accident_group)
        results[var] = {'U-statistic': stat, 'p-value': p}

        # 결과 출력
        print(f"변수: {var}")
        print(f"  U-statistic: {stat:.2f}, p-value: {p:.3f}")
        if p < 0.05:
            print("유의미한 차이가 있습니다.")
        else:
            print("유의미한 차이가 없습니다.")
    except KeyError:
        print(f"변수 '{var}'가 데이터에 없습니다.")
    except Exception as e:
        print(f"변수 '{var}' 처리 중 오류: {e}")


# 다변량 분석(MANOVA): 여러변수를 한번에 비교
combined_df = accidents_df.copy()
combined_df['사고여부'] = 1
non_accidents_df['사고여부'] = 0
combined_df = pd.concat([combined_df, non_accidents_df])

manova = MANOVA.from_formula(f"{'+'.join(variables)} ~ 사고여부", data=combined_df)
print(manova.mv_test())


#랜덤포레스트 : 사고/비사고 데이터를 예측하는데 기여도가 높은 변수 평가
X = combined_df[variables]
y = combined_df['사고여부']

# 랜덤포레스트 모델 학습
rf = RandomForestClassifier()
rf.fit(X, y)

# 변수 중요도 출력 
importances = rf.feature_importances_
for var, imp in zip(variables, importances):
    print(f"{var}: 중요도 = {imp:.3f}")

#나이, 근무경력, 발생시간, 발생월