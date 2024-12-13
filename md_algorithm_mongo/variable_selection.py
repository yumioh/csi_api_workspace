import pandas as pd


non_accidents_df = pd.read_csv("./md_algorithm_mongo/data/non_accidents_preprocessing.csv")
accidents_df = pd.read_csv("./md_algorithm_mongo/data/accidents_preprocessing.csv")

print(accidents_df.describe())
print(accidents_df.head())

# print(non_accidents_df.describe())
# print(non_accidents_df.head())
