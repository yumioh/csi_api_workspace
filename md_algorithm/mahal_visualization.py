import matplotlib.pyplot as plt
import pandas as pd

print("-------------------산점도 그리기 --------------------")

# plt.scatter(kosha_df['나이'], kosha_data[0])
# plt.scatter(gh_df['나이'], gh_data[0])
# plt.title('scatter')
# plt.savefig("./md_algorithm/data/img/gh_scatter.png")
# plt.show()

coulmns = ["근무경력","나이","월별","요일별"]

print("-------------------kosha 박스플롯 그리기 --------------------")  
kosha = pd.read_csv("./md_algorithm/data/kosha_normalized.csv")
kosha_mal = pd.read_csv("./md_algorithm/data/kosha_normalized.csv")

for column in coulmns : 
    plt.rcParams['font.family'] ='Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['boxplot.flierprops.markersize'] = 3
     
    #boxplot 그리기
    plt.boxplot([kosha[column], kosha_mal["mahal"]])
    #제목 및 라벨 설정
    plt.title(f'KOSHA {column}',fontdict={'weight': 'bold', 'size' : "15"})
    plt.ylabel('Values')
    plt.xticks([1, 2], ['KOSHA Data', 'MD Data']) 
    plt.savefig(f"./md_algorithm/data/img/kosha_boxplot_{column}.png")
    plt.show()

print("-------------------gh 박스플롯 그리기 --------------------")  
gh = pd.read_csv("./md_algorithm/data/gh_normalized.csv")
gh_mal = pd.read_csv("./md_algorithm/data/gh_normalized.csv")

for column in coulmns : 
    plt.rcParams['font.family'] ='Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['boxplot.flierprops.markersize'] = 3
     
    #boxplot 그리기
    plt.boxplot([gh[column], gh_mal["mahal"]])
    #제목 및 라벨 설정
    plt.title(f'GH {column}', fontdict={'weight': 'bold', 'size' : "15"})
    plt.ylabel('Values')
    plt.xticks([1, 2], ['GH Data', 'MD Data']) 
    plt.savefig(f"./md_algorithm/data/img/gh_boxplot_{column}.png")
    plt.show()
