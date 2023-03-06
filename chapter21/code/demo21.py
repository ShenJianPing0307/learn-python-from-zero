import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")

flights_wide = flights.pivot(index="month", columns="year", values="passengers")
print(flights_wide.transpose())  # 横纵坐标改变了方向
# sns.relplot(data=flights_wide, kind="line")
# plt.show()

# sns.relplot(data=flights_wide.transpose(), kind="line")
# plt.show()
#
# data = [{"name": 'zs'}, {''}]
# print(flights_wide.to_dict())
#
# print(flights)
# data1 = []
# for key, value in flights_wide.to_dict().items():
#     d = {}
#     d['year'] = key # {'year':1949}
#     for key1, value1 in value.items():
#         d['month'] = key1
#         d['passengers'] = value1
#         data1.append(d) # [{'year':1949, 'month': 'Jan'},{'year':1949, 'month': 'Feb'}...]
#
# import pandas as pd
#
# df = pd.DataFrame(data=data1)
# print(df)
