import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from main import dfCleaned


#Line Graph to see the trend of how prices change with model year to see the reason behind best selling cars
dfCleaned.info()
sales=dfCleaned.groupby('year')['sellingprice'].mean()
year=sales.index.tolist()
avgPrice=sales.values.tolist()
plt.plot(year,avgPrice,marker='o',color='red',linestyle='dashed')
plt.title('Line graph to find the trend between model year and sold units')
plt.xlabel('Model Year')
plt.ylabel('Average Price')
plt.show()

