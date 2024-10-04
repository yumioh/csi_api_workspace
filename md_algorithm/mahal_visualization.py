import matplotlib.pyplot as plt
import pandas as pd

kosha_data= pd.read_csv("./md_algorithm/data/kosha_Mahal.csv")
gh_data= pd.read_csv("./md_algorithm/data/gh_Mahal.csv")

print("-------------------kosha calculateMahalanobis 선 그래프 그리기-------------------")
# kosha_data에서 'calculateMahalanobis' 열 가져오기
mahalanobis_distances = kosha_data['calculateMahalanobis']

# 선 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(mahalanobis_distances, color='green', marker='o', linestyle= '-', markersize=5, label='Mahalanobis Distance')
plt.title('Mahalanobis Distance Line Plot')
plt.xlabel('Index')
plt.ylabel('Mahalanobis Distance')
plt.grid(True)
plt.legend()
plt.savefig("./md_algorithm/data/img/kosha_line.png")
plt.show()

print("-------------------kosha calculateMahalanobis 산점도 그래프 그리기-------------------")

# 산점도 그리기 (index와 mahalanobis distance 간의 관계)
plt.figure(figsize=(8, 6))
plt.scatter(range(len(mahalanobis_distances)), mahalanobis_distances, color='red', alpha=0.5)
plt.title('Mahalanobis Distance Scatter Plot')
plt.xlabel('Index')
plt.ylabel('Mahalanobis Distance')
plt.grid(True)
plt.savefig("./md_algorithm/data/img/kosha_scatter.png")
plt.show()

print("-------------------gh calculateMahalanobis 선 그래프-------------------")
# kosha_data에서 'calculateMahalanobis' 열 가져오기
mahalanobis_distances_gh = gh_data['calculateMahalanobis']

# 선 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(mahalanobis_distances_gh, color='green', marker='o', linestyle= '-', markersize=5, label='Mahalanobis Distance')
plt.title('Mahalanobis Distance Line Plot')
plt.xlabel('Index')
plt.ylabel('Mahalanobis Distance')
plt.grid(True)
plt.legend()
plt.savefig("./md_algorithm/data/img/gh_line.png")
plt.show()

print("-------------------gh calculateMahalanobis 산점도 그래프-------------------")

mahalanobis_distances_gh = gh_data['calculateMahalanobis']

plt.figure(figsize=(8, 6))
plt.scatter(range(len(mahalanobis_distances_gh)), mahalanobis_distances_gh, color='red', alpha=0.5)
plt.title('Mahalanobis Distance Scatter Plot')
plt.xlabel('Index')
plt.ylabel('Mahalanobis Distance')
plt.grid(True)
plt.savefig("./md_algorithm/data/img/gh_scatter.png")
plt.show()