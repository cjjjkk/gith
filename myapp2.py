file = "mall_customer.csv"

import pandas as pd
df = pd.read_csv(file)

df.head()

df.shape

features = ['Annual_Income_(k$)', 'Spending_Score']
X = df[features]

plt.scatter(X['Annual_Income_(k$)'], X['Spending_Score']);