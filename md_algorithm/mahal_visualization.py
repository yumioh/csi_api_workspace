import matplotlib.pyplot as plt
import pandas as pd

kosha_data= pd.read_csv("./md_algorithm/data/kosha_Mahal_list.csv", header=None)
kosha_df = pd.read_csv("./md_algorithm/data/kosha_categorize.csv")

gh_data= pd.read_csv("./md_algorithm/data/gh_Mahal_list.csv", header=None)
gh_df = pd.read_csv("./md_algorithm/data/gh_categorize.csv")


# plt.scatter(kosha_df['나이'], kosha_data[0])
# plt.scatter(gh_df['나이'], gh_data[0])
plt.boxplot([gh_data,kosha_data])
plt.title('scatter')
plt.savefig("./md_algorithm/data/img/gh_scatter_column_comparison.png")
plt.show()




# for col in gh_data.columns:
#     plt.scatter(gh_data.index, kosha_data[col], label=f'Column {col}')

# plt.title('Scatter Plot of Data')
# plt.xlabel('Index')
# plt.ylabel('Values')
# plt.savefig("./md_algorithm/data/img/gh_scatter.png")
# plt.show()
