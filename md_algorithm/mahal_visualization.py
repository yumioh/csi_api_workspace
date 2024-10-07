import matplotlib.pyplot as plt
import pandas as pd

kosha_data= pd.read_csv("./md_algorithm/data/kosha_Mahal_list.csv", header=None)
kosha_df = pd.read_csv("./md_algorithm/data/kosha_categorize.csv")

gh_data= pd.read_csv("./md_algorithm/data/gh_Mahal_list.csv", header=None)
gh_df = pd.read_csv("./md_algorithm/data/gh_categorize.csv")

print("-------------------산점도 그리기 --------------------")

# plt.scatter(kosha_df['나이'], kosha_data[0])
# plt.scatter(gh_df['나이'], gh_data[0])
# plt.title('scatter')
# plt.savefig("./md_algorithm/data/img/gh_scatter.png")
# plt.show()

print("-------------------박스플롯 그리기 --------------------")

coulmns = ["근무경력","나이","월별","요일별"]

for column in coulmns : 
    kosha_mahal = pd.read_csv(f"./md_algorithm/data/kosha_Mahal_{column}.csv",header=None)
    gh_mahal = pd.read_csv(f"./md_algorithm/data/gh_Mahal_{column}.csv",header=None)
    print(kosha_mahal)

    plt.rcParams['font.family'] ='Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] =False
     
    #boxplot 그리기
    plt.boxplot([gh_mahal[0], kosha_mahal[0]])
    #제목 및 라벨 설정
    plt.title(f'{column} Box Plot')
    plt.ylabel('Values')
    plt.xticks([1, 2], ['GH Data', 'Kosha Data']) 
    plt.savefig(f"./md_algorithm/data/img/gh_kosha_boxplot_{column}.png")
    plt.show()
