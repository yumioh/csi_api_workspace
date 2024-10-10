import pandas as pd
import math
from matplotlib import pyplot as plt
from matplotlib import rc
import numpy as np

#척도 적용
#지수는 값이 비슷하게 나와 로그로 척도 사용

rc('font', family='Malgun Gothic')

gh = pd.read_csv("./md_algorithm/data/gh_without_outline.csv")
kosha = pd.read_csv("./md_algorithm/data/kosha_without_outline.csv")

print(gh.head())
print(kosha.head())

print("지수")
print(np.exp(gh))
print(np.exp(kosha))

# #지수 그래프 그리기
# plt.figure()
# plt.title("지수함수 그래프",fontdict={'weight': 'bold', 'size': 20})
# plt.plot(gh.index, np.exp(gh), color='red', label='GH',linestyle=":")
# plt.plot(kosha.index, np.exp(kosha), color='dodgerblue', label='KOSHA', linestyle=":")
# plt.xlabel("MD Value")
# plt.ylabel("Exp Value")
# plt.legend()
# plt.grid(True)
# plt.savefig("./md_algorithm/data/img/gh_kosha_exp_plot.png")
# plt.show()

# print("로그")
# print(np.log(gh))
# print(np.log(kosha))

# #로그 그래프 그리기
# plt.figure()
# plt.title("로그 함수 그래프",fontdict={'weight': 'bold', 'size': 20})
# plt.plot(gh, np.log(gh), color='orange', label='GH', linestyle="-")
# plt.plot(kosha, np.log(kosha), color='pink', label='KOSHA',linestyle="-")
# plt.xlabel("MD Value")
# plt.ylabel("log Value")
# plt.legend()
# plt.grid(True)
# plt.savefig("./md_algorithm/data/img/gh_kosha_log_plot.png")
# plt.show()


#지수 그래프 그리기
plt.figure()
plt.title("지수(MD) 그래프",fontdict={'weight': 'bold', 'size': 20})
plt.scatter(gh.index, np.exp(gh), color='red', label='GH')
plt.scatter(kosha.index, np.exp(kosha), color='dodgerblue', label='KOSHA', s=3)
plt.xlabel("Index")
plt.ylabel("Exp(MD) Value")
plt.legend()
plt.grid(True)
plt.savefig("./md_algorithm/data/img/gh_kosha_exp_plot.png")
plt.show()

print("로그")
print(np.log(gh))
print(np.log(kosha))

#로그 그래프 그리기
plt.figure()
plt.title("GH vs KOSHA 로그(MD)",fontdict={'weight': 'bold', 'size': 20})
plt.scatter(gh.index, np.log(gh), color='orange', label='GH')
plt.scatter(kosha.index, np.log(kosha), color='pink', label='KOSHA')
plt.xlabel("Index")
plt.ylabel("log(MD) Value")
plt.legend()
plt.grid(True)
plt.savefig("./md_algorithm/data/img/gh_kosha_log_plot_1.png")
plt.show()

#지수
gh_exp = np.exp(gh.iloc[:, 0])
kosha_exp = np.exp(kosha.iloc[:, 0])

arranged_gh = gh_exp.sort_values().reset_index(drop=True)
arranged_kosha = kosha_exp.sort_values().reset_index(drop=True)

#지수 그래프 그리기
plt.figure()
plt.title("지수(MD) 그래프",fontdict={'weight': 'bold', 'size': 20})
plt.scatter(arranged_gh.index, arranged_gh, color='red', label='GH')
plt.scatter(arranged_kosha.index, arranged_kosha, color='dodgerblue', s=3,label='KOSHA', alpha=0.4)
plt.xlabel("Index")
plt.ylabel("exp(MD)")
plt.legend()
plt.grid(True)
plt.savefig("./md_algorithm/data/img/gh_kosha_exp_plot.png")
plt.show()


#로그 함수
gh_log = np.log(gh.iloc[:, 0])
kosha_log = np.log(kosha.iloc[:, 0])

arranged_gh = gh_log.sort_values().reset_index(drop=True)
arranged_kosha = kosha_log.sort_values().reset_index(drop=True)

#로그 그래프 그리기
plt.figure()
plt.title("GH vs KOSHA 로그(MD)",fontdict={'weight': 'bold', 'size': 20})
plt.scatter(arranged_gh.index, arranged_gh, color='orange', s=3, label='GH')
plt.scatter(arranged_kosha.index, arranged_kosha, color='pink', s=3, label='KOSHA')
plt.xlabel("Index")
plt.ylabel("log(MD)")
plt.legend()
plt.grid(True)
plt.savefig("./md_algorithm/data/img/gh_kosha_log_plot.png")
plt.show()


