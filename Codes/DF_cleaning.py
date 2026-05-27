# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:53:29 2026

@author: usman
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:27:29 2026

@author: usman
"""

import pandas as pd
import numpy as np


fb_df = pd.read_csv("KAG_conversion_data1.csv")
as_df = pd.read_csv("All Sales Data.csv",low_memory=False)

print("kag Shape",fb_df.shape)
print()
print("all sales shape",as_df.shape)

print("kag Columns",fb_df.columns.tolist())
print()
print("all sales Columns",as_df.columns.tolist())


#drop Extra coloums
as_df = as_df.drop(columns = ['Order ID'])
fb_df = fb_df.drop(columns = ['ad_id', 'fb_campaign_id', 
                             'Total_Conversion'])
print("All sales coloums \n",as_df.columns.tolist())
print("Kag colums \n",fb_df.columns.tolist())

#Data cleaning 

print("Missing values")
print(as_df.isnull().sum())

as_df['Quantity Ordered'] = pd.to_numeric(
                            as_df['Quantity Ordered'], 
                            errors='coerce')
as_df['Price Each'] = pd.to_numeric(
                      as_df['Price Each'], 
                      errors='coerce')
as_df['Order Date'] = pd.to_datetime(
                      as_df['Order Date'], 
                      errors='coerce')

as_df = as_df.dropna(subset=['Order Date'])
as_df['Order Date'] = pd.to_datetime(
                      as_df['Order Date'],
                      errors='coerce')
as_df = as_df.dropna(subset=['Order Date'])

as_df['Month'] = as_df['Order Date'].dt.month
as_df['Hour'] = as_df['Order Date'].dt.hour
as_df['Day'] = as_df['Order Date'].dt.day_name()

as_df['City'] = as_df['Purchase Address'].str.split(
                ',').str[1].str.strip()
#Creating revenue
as_df['Revenue']= as_df['Quantity Ordered'] * as_df['Price Each']

as_df = as_df.drop(columns = ['Order Date','Purchase Address'])

as_df = as_df.dropna()

fb_df['age'] = fb_df['age'].str.split('-').str[0].astype(int)

fb_df['gender'] = fb_df['gender'].map({'M': 1, 'F': 0})

product_map = {
    'A': 'iPhone',
    'B': 'Macbook Pro Laptop',
    'C': 'Apple Airpods Headphones',
    'D': 'USB-C Charging Cable',
    'E': 'AA Batteries (4-pack)',
    'F': 'AAA Batteries (4-pack)',
    'G': 'Wired Headphones',
    'H': 'Bose SoundSport Headphones',
    'I': '27in FHD Monitor',
    'J': '27in 4K Gaming Monitor',
    'K': '34in Ultrawide Monitor',
    'L': 'Google Phone',
    'M': 'Flatscreen TV',
    'N': 'ThinkPad Laptop',
    'O': '20in Monitor',
    'P': 'Vareebadd Phone',
    'Q': 'LG Washing Machine',
    'R': 'LG Dryer',
    'S': 'Lightning Charging Cable'
}
fb_df['Product'] =fb_df['campaign'].map(product_map)
print(fb_df['Product'].value_counts())



#cleaning is over
print("All sales shape \n",as_df.shape)
print("All sales \n",as_df.columns.tolist())
print(as_df.isnull().sum())
print(as_df.dtypes)
print("Kag Shape:", fb_df.shape)
print("Columns:", fb_df.columns.tolist())
print(as_df.isnull().sum())
print(fb_df['campaign'].value_counts())

#Save
as_df.to_csv("All_sales_clean.csv", index=False)
fb_df.to_csv("Ads_clean.csv", index=False)


