#regression & classification





from sklearn.linear_model import LinearRegression
import pandas as pd

# y = ax + b


df = pd.read_csv('Student_Marks.csv')

y=df[['Marks']]
x=df[["number_courses","time_study"]]
print(df.head)
l = LinearRegression()

model = l.fit(x,y) #machine learn
x_=model.coef_
y_=model.intercept_

predict = model.predict([[10,4]])
print(model.score(x,y))
print(predict)

