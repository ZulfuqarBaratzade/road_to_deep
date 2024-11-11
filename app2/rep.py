import pandas as pd
from sklearn.linear_model import LinearRegression
df = pd.read_csv('audi.csv')

# Preprocessing
new_df = df.drop(columns=["index", "href", "MileageRank", "PriceRank", "PPYRank", "Score"])

int_df = pd.get_dummies(new_df, columns=["Engine","Type", "Transmission", "Fuel"])

int_df = int_df.astype(float)

print(int_df.head())
y=int_df
x=int_df.drop("Price(£)",axis=1)
lm=LinearRegression()
model = lm.fit(x,y)
print(model.predict(x,y))