# from sklearn.datasets import load_iris


# data=load_iris()


# data.target[[10,25,50]]
# t = list(data.target_names)

# print(t)


from sklearn.linear_model import LinearRegression
import pandas as pd

# y = mx + b

df = pd.read_csv("student.csv")



print(df.head())