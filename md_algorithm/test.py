import matplotlib.pyplot as plt

# 예제 데이터: 0.5와 1의 값들
data = [0.5, 1, 0.5, 1, 1, 1, 0.5, 1, 0.5, 1, 0.5, 1]

# 박스 플롯 생성
plt.boxplot(data)
plt.title("Box Plot of Data with 0.5 and 1")
plt.ylabel("Value")
plt.show()
