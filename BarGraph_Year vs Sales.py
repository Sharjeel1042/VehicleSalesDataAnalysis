from matplotlib import pyplot as plt
from main import df

sales=df.groupby('year')['saledate'].count()
years = sales.index.tolist()
counts = sales.values.tolist()
sales=df.groupby('year')['saledate'].count()
fig, ax=plt.subplots()
bars=ax.bar(years,counts,width=0.9)
plt.title('Bar Graph showing the most popular cars based on the model\'s year')
plt.ylabel("Number Of Cars")
plt.xlabel("Car Model Year")
plt.xticks(rotation=45)
for bar in bars:
        height=bar.get_height()
        ax.text(
                bar.get_x()+bar.get_width()/2,
                height,
                f'{height}',
                ha='center',
                va='bottom',
                fontdict={'fontsize':7}
        )


plt.show()
fig.savefig('BarGraph(Year_VS_Sales).png',dpi=200)
