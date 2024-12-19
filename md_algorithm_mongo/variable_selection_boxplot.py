import pandas as pd
import matplotlib.pyplot as plt
from data_processor import DataProcessor

accident_df = pd.read_csv("./md_algorithm_mongo/data/accidents_preprocessing.csv")
non_accident_df = pd.read_csv("./md_algorithm_mongo/data/non_accidents_preprocessing.csv")

accident_df = accident_df[['나이','발생시간','근무경력','공사규모','발생요일','발생월']]
non_accident_df = non_accident_df[['나이','발생시간','근무경력','공사규모','발생요일','발생월']]

#이상치 제거
for col in accident_df.columns:
    accident_df = DataProcessor.remove_outliers_zcore(accident_df, col)
    non_accident_df = DataProcessor.remove_outliers_zcore(non_accident_df, col)

print("사고 데이터:")
print(accident_df.head())
print("\n비사고 데이터:")
print(non_accident_df.head())

non_accident_df.to_csv("./md_algorithm_mongo/data/non_accidents_outline.csv")

accident_df.to_csv("./md_algorithm_mongo/data/accidents_outline.csv")

for col in accident_df.columns:
    plt.rcParams['font.family'] ='Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['boxplot.flierprops.markersize'] = 3

    plt.figure(figsize=(5, 4))
    plt.boxplot(accident_df[col].tolist(), labels=["Accident"])
    plt.title(f'{col} 박스플롯')
    plt.ylabel("values")
    plt.savefig(f"./md_algorithm_mongo/data/img/accident_boxplot_{col}")
    plt.show()

    plt.figure(figsize=(5, 4))
    plt.boxplot(non_accident_df[col].tolist(), labels=["Non-Accident"])
    plt.title(f'{col} 박스플롯')
    plt.ylabel("values")
    plt.savefig(f"./md_algorithm_mongo/data/img/non_accident_boxplot_{col}")
    plt.show()

