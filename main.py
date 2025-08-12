import numpy as np
import pandas as pd

df=pd.read_csv('car_prices.csv')
if __name__ == "__main__":
 print(df)

 df.info()
#Cleaning Column Names
 df.columns=df.columns.str.strip()
 df.columns=df.columns.str.lower()
#Handling missing data
 df=df.sort_values(['vin','saledate'])
 df['make']=df['make'].ffill()
 df['model']=df['model'].ffill()
 df['trim']=df['trim'].ffill()
 df['body']=df['body'].ffill()
 df['transmission']=df['transmission'].ffill()
 df['condition']=df['condition'].fillna(df['condition'].median())
 df['odometer']=df['odometer'].fillna(df['odometer'].median())
 df['color']=df['color'].fillna('Unknown')
 df['interior']=df['interior'].fillna('Unknown')
 df['mmr']=df['mmr'].fillna('Unknown')
 df['sellingprice']=df['sellingprice'].fillna(0)
 df['sold']=df['saledate'].notnull()#Creating a new column to show that whether a car hs been sold yet ot not
 df=df.dropna(subset=['vin'])
#DataType Conversion
 df['saledate'] = df['saledate'].str.replace(r'\s*\(.*\)', '', regex=True)
 df['saledate'] = pd.to_datetime(df['saledate'], errors='coerce',utc=True)
#Removing duplicates
 
#1-Find if there are any duplicates to begin with
 duplicates=df[df.duplicated(keep=False)]
 print(duplicates)
 numDuplicates=df.duplicated().sum()
 print("Number of duplicates: ",numDuplicates)
 df.to_csv("cleaned_car_prices.csv", index=False)














