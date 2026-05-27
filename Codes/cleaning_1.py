# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:27:29 2026

@author: usman
"""

import pandas as pd
import numpy as np


fb_df = pd.read_csv("KAG_conversion_data.csv")
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
#cleaning is over
print("All sales shape \n",as_df.shape)
print("All sales \n",as_df.columns.tolist())
print(as_df.isnull().sum())
print(as_df.dtypes)

as_df.to_csv("All_Sales_clean.csv", index=False)






