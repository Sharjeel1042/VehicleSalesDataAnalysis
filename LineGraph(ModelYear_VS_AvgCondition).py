import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from main import dfCleaned

trend=dfCleaned.groupby('year')['condition'].mean()
modelYear=trend.index.tolist()
avgCond=trend.values.tolist()
plt.plot(modelYear,avgCond)
plt.title('ModelYear VS AverageCondition')
plt.show()