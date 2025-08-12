import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from main import df

carsSold=df.groupby('make')['saledate'].count()
carMake=carsSold.index.tolist()
numSold=carsSold.values.tolist()


fig, ax=plt.subplots(figsize=(18,6))
bars=ax.bar(carMake,carsSold,width=0.5)
plt.xticks(rotation=90)
for bar in bars:
    height=bar.get_height()
    ax.set_xticks(np.arange(len(carMake)))
    ax.set_xticklabels(carMake, fontdict={'fontsize': 7})
    plt.ylabel('Units Sold',fontdict={'fontsize':10})
    ax.text(
        bar.get_x()+bar.get_width()/2,
        height,
        f'{height}',
        ha='center',
        va='bottom',
        fontdict={'fontsize':5}

    )
plt.show()
fig.savefig('BarGraph(CarMake_VS_Sales).png', dpi=200)
