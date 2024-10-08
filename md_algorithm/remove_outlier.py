import pandas as pd
import matplotlib.pyplot as plt

gh_df = pd.read_csv("./md_algorithm/data/gh_categorize_random.csv")
kosha_df = pd.read_csv("./md_algorithm/data/kosha_categorize.csv")

gh_md_df = pd.read_csv("./md_algorithm/data/gh_Mahal_list.csv", header = None)
kosha_md_df = pd.read_csv("./md_algorithm/data/kosha_Mahal_list.csv", header = None)

print(gh_md_df.head())

#이상치 범위 설정
# Q3 + 1.5 * IQR은 '상한선
# Q1 - 1.5 * IQR은 '하한선'
def findOutliers(x,column): #이상치 개수 확인 함수
    # Q1, Q3 계산
    q1 = x[column].quantile(0.25)
    q3 = x[column].quantile(0.75)
    iqr = q3 - q1
    print("iqr : ", iqr)
    y = x[(x[column] > (q3 + 1.5*iqr)) | (x[column] < (q1 - 1.5*iqr))]
    print(f"{column} shape : ", y.shape)
    return y

#GH 이상치 제거 : 근무경력 (공사규모, 나이, 발생시간은 이상치가 발견되지 않음)
print("kosha shape : ",gh_df.shape)
age_gh = findOutliers(gh_df,'나이') 
scale_gh = findOutliers(gh_df,'공사규모')
work_gh = findOutliers(gh_df,'근무경력') # 637개
hour_gh = findOutliers(gh_df,'발생시간')
md_gh = findOutliers(gh_md_df, 0) #637개

#KOSHA 이상치 제거 : 근무경력, 발생시간(공사규모, 나이는 이상치가 발견되지 않음)
print("kosha shape : ",kosha_df.shape)
age_kosha = findOutliers(kosha_df, "나이")
scale_kosha = findOutliers(kosha_df, "공사규모")
work_kosha = findOutliers(kosha_df, "근무경력") # 7989개
hour_kosha = findOutliers(kosha_df, "발생시간") # 696개
md_kosha = findOutliers(kosha_md_df, 0) # 3189개

print("------------------이상치 제거----------------")
# 신뢰도 95% 기준 이상치 Index 추출
outlier = gh_df[(abs((gh_df['근무경력']-gh_df['근무경력'].mean())/gh_df['근무경력'].std()))>1.96].index
clean_df = gh_df.drop(outlier)
print(clean_df.shape)

plt.boxplot([md_gh[0], md_kosha[0]])
plt.show()
