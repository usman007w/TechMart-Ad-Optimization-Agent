# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:06:19 2026

@author: usman
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



fb_df = pd.read_csv("Ads_clean.csv")
as_df = pd.read_csv("All_sales_clean.csv")

#1Plot Best selling product
product_sales = as_df.groupby('Product')['Quantity Ordered'].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x=product_sales.values, 
            y=product_sales.index,
            palette='Blues')
plt.title("Best Selling Products",fontsize=16)
plt.xlabel("Total Units Sold",fontsize=12)
plt.ylabel("Product",fontsize=12)
plt.tight_layout()
plt.savefig("chart1_best_selling.png")

#2Plot Total revenue
product_revenue = as_df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=product_revenue.values,
            y=product_revenue.index,
            palette='Blues',
            ax=ax)

ax.set_title("Most Revenue by Product",fontsize=16)
ax.set_xlabel("Total Revenue ($)",fontsize=12)
ax.set_ylabel("Product",fontsize=12)

plt.tight_layout()
plt.savefig("chart2_revenue.png")

#3Plot peak selling month

monthly_sales = as_df.groupby('Month')['Quantity Ordered'].sum()
monthly_names = ['jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

fig,ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x=monthly_sales.index,
             y=monthly_sales.values,
             marker='o',
             linewidth=2.5,
             color='steelblue',
             ax=ax)

ax.set_xticks(range(1, 13))
ax.set_xticklabels(monthly_names)
ax.set_title("Peak Selling Month",fontsize=16)
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Total Units Sold",fontsize=12)
plt.tight_layout()
plt.savefig("chart3_peak_month.png")

#4Plot peak Hour
hourly_sales = as_df.groupby('Hour')['Quantity Ordered'].sum()
fig,ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x=hourly_sales.index,
             y=hourly_sales.values,
             marker='o',
             linewidth=2.5,
             color='steelblue',
             ax=ax)

ax.set_title("Peak Selling Hour",fontsize=16)
ax.set_xlabel("Hour of Day (24hr)",fontsize=12)
ax.set_ylabel("Total Units Sold",fontsize=12)
ax.set_xticks(range(0, 24))
plt.tight_layout()
plt.savefig("chart4_peak_hour.png")

#5Plot Top city for sell

city_sales = as_df.groupby('City')['Quantity Ordered'].sum().sort_values(ascending=False)

fig,ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=city_sales.values,
            y=city_sales.index,
            palette='Blues',
            ax=ax)
ax.set_title("Best Cities for Sales",fontsize=16)
ax.set_xlabel("Total Units Sold",fontsize=12)
ax.set_ylabel("City",fontsize=12)
plt.tight_layout()
plt.savefig("chart5_best_city.png")

#6Plot Top Succesful Campaign   

camp_conv = fb_df.groupby('Product')['Approved_Conversion'].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(14, 8))
sns.barplot(x=camp_conv.values,
            y=camp_conv.index,
            palette='Blues',
            ax=ax)
ax.set_title("Product Campaign Conversions",fontsize=16)
ax.set_xlabel("Total Approved Conversions",fontsize=12)
ax.set_ylabel("Product",fontsize=12)
plt.tight_layout()
plt.savefig("chart6_campaign_performance.png")

#7 Age Group Converstion
age_conv = fb_df.groupby('age')['Approved_Conversion'].sum().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=age_conv.index,
            y=age_conv.values,
            palette='Blues',
            ax=ax)

ax.set_title("Age Group vs Conversions", fontsize=16)
ax.set_xlabel("Age Group", fontsize=12)
ax.set_ylabel("Total Conversions", fontsize=12)

plt.tight_layout()
plt.savefig("chart7_age_conversions.png")


#8plot Top Gendar convertion

gender_conv = fb_df.groupby('gender')['Approved_Conversion'].sum()
gender_conv.index = ['Female','Male']

fig,ax = plt.subplots(figsize=(7, 6))
sns.barplot(x=gender_conv.index,
            y=gender_conv.values,
            palette='Blues',
            ax=ax)
ax.set_title("Gender vs Conversions",fontsize=16)
ax.set_xlabel("Gender",fontsize=12)
ax.set_ylabel("Total Conversions",fontsize=12)
plt.tight_layout()
plt.savefig("chart8_gender_conversions.png")

#9plot Click convertion

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x=fb_df['Clicks'],
                y=fb_df['Approved_Conversion'],
                hue=fb_df['Campaign'],
                ax=ax)
ax.set_title("Clicks vs Conversions by Campaign",fontsize=16)
ax.set_xlabel("Clicks",fontsize=12)
ax.set_ylabel("Approved Conversions",fontsize=12)
plt.tight_layout()
plt.savefig("chart9_clicks_conversions.png")

#10plot HeatMap

numeric_cols = fb_df[['age', 'gender', 'interest',
                       'Impressions', 'Clicks',
                       'Spent', 'Approved_Conversion']]

corr_matrix = numeric_cols.corr()

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr_matrix,
            annot=True,
            fmt='.2f',
            cmap='Blues',
            linewidths=0.5,
            linecolor='white',
            ax=ax)

ax.set_title("Correlation Heatmap — Ads Data", fontsize=16)
plt.tight_layout()
plt.savefig("chart10_heatmap.png")

























