import numpy as np
import matplotlib.pyplot as plt
from main import df

df['year_group']=np.where(df['year']<2005,'Before 2005',df['year'])
saleYears=df.groupby('year_group')['sellingprice'].count().sort_index()
plt.figure(figsize=(8,6),dpi=150)
years=saleYears.index.tolist()
counts=saleYears.values.tolist()
saleYears.plot(kind='pie',autopct='%1.1f%%',startangle=90,pctdistance=0.82)
plt.ylabel('')
plt.title('Pie Chart showing the most popular cars based on the model\'s year')
plt.tight_layout()
plt.show()
