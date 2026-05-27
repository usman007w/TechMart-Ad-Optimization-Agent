# -*- coding: utf-8 -*-
"""
Created on Sun May  3 01:07:05 2026

@author: usman
"""

import pandas as pd 

sales_df = pd.read_csv("All_Sales_clean.csv")
ads_df = pd.read_csv("Ads_clean.csv")
pd.options.display.float_format = '{:,.2f}'.format 

#Product Rankings
product_rank = sales_df.groupby('Product').agg({
    'Quantity Ordered': 'sum',
    'Revenue': 'sum'
}).sort_values('Revenue', ascending=False).reset_index()

product_rank['Rank'] = range(1, len(product_rank) + 1)

# Best Selling Season
best_month = sales_df.groupby('Month')['Quantity Ordered'].sum()
best_hour = sales_df.groupby('Hour')['Quantity Ordered'].sum()
best_day = sales_df.groupby('Day')['Quantity Ordered'].sum()

# Best Cities
city_sales = sales_df.groupby('City').agg({
    'Quantity Ordered': 'sum',
    'Revenue': 'sum'
}).sort_values('Revenue', ascending=False).reset_index()

print("Sales Insights")
print("\nTop 5 Products:")
print(product_rank[['Rank','Product','Revenue']].head())
print("\nBest Month:", best_month.idxmax())
print("Best Hour:", best_hour.idxmax())
print("Best Day:", best_day.idxmax())
print("\nTop 3 Cities:")
print(city_sales[['City','Revenue']].head(3))


# Best Age
best_age = ads_df.groupby('age')['Approved_Conversion'].sum()

# Gender Breakdown
gender_conv = ads_df.groupby('gender')['Approved_Conversion'].sum()

# Best Interest
best_interest = ads_df.groupby('interest')['Approved_Conversion'].sum().sort_values(ascending=False)

# Campaign Performance
campaign_perf = ads_df.groupby('Campaign').agg({
    'Approved_Conversion': 'sum',
    'Spent': 'sum',
    'Clicks': 'sum'
}).reset_index()

# ROI = Revenue per dollar spent
campaign_perf['ROI'] = (
    campaign_perf['Approved_Conversion'] /
    campaign_perf['Spent'] * 100
).round(2)

# Cost per conversion
campaign_perf['Cost_Per_Conversion'] = (
    campaign_perf['Spent'] /
    campaign_perf['Approved_Conversion'].replace(0, 1)
).round(2)

print("Ads Insights Done!")
print("\nBest Age:", best_age.idxmax())
print("Best Gender:", "Male" if gender_conv.idxmax() == 1 else "Female")
print("\nTop 3 Interests:")
print(best_interest.head(3))
print("\nCampaign Performance:")
print(campaign_perf
      [['Campaign','Approved_Conversion','ROI','Cost_Per_Conversion']])


# Merge campaign performance with product names
final_df = campaign_perf.copy()

# Add product names
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

final_df['Product'] = final_df['Campaign'].map(product_map)

# Add sales data
sales_summary = sales_df.groupby('Product').agg({
    'Quantity Ordered': 'sum',
    'Revenue': 'sum'
}).reset_index()

# Merge
final_df = final_df.merge(sales_summary,
                           on='Product',
                           how='left')

def make_decision(row):
    revenue = row['Revenue']
    roi = row['ROI']

    if revenue >= 3000000:
        return 'BOOST'
    elif roi >= 2.0 and revenue >= 2000000:
        return 'BOOST'
    elif revenue >= 500000:
        return 'MAINTAIN'
    else:
        return 'DISCARD'

# Final decision
final_df['Decision'] = final_df.apply(make_decision, axis=1)
print(final_df[['Product', 'ROI', 'Revenue', 'Decision']])


# Final Report
print("\n" + "="*55)
print("   TECHMART AD OPTIMIZATION REPORT")
print("="*55)

print("\n MARKET ANALYSIS")
print("-"*55)
print(f"Total Products Analyzed: {len(final_df)}")
print(f"Best Revenue Product: {final_df.loc[final_df['Revenue'].idxmax(), 'Product']}")
print(f"Best ROI Campaign: {final_df.loc[final_df['ROI'].idxmax(), 'Product']}")

print("\n BEST TARGET AUDIENCE")
print("-"*55)
print(f"Best Age Group  : {best_age.idxmax()}-{best_age.idxmax()+4}")
best_gender = "Male" if gender_conv.idxmax() == 1 else "Female"
print(f"Best Gender     : {best_gender}")
print(f"Top Interests   : {best_interest.head(3).index.tolist()}")

print("\n TIMING STRATEGY")
print("-"*55)
print(f"Best Month : {best_month.idxmax()}")
print(f"Best Hour  : {best_hour.idxmax()}:00")
print(f"Best Day   : {best_day.idxmax()}")

print("\n LOCATION STRATEGY")
print("-"*55)
print(city_sales[['City','Revenue']].head(3).to_string(index=False))

print("\n BOOST THESE ADS")
print("-"*55)
boost = final_df[final_df['Decision'] == 'BOOST']
for _, row in boost.iterrows():
    print(f" {row['Product']:<30} Revenue: ${row['Revenue']:>12,.0f}")

print("\n MAINTAIN THESE ADS")
print("-"*55)
maintain = final_df[final_df['Decision'] == 'MAINTAIN']
for _, row in maintain.iterrows():
    print(f"  {row['Product']:<30} Revenue: ${row['Revenue']:>12,.0f}")

print("\n DISCARD THESE ADS")
print("-"*55)
discard = final_df[final_df['Decision'] == 'DISCARD']
for _, row in discard.iterrows():
    print(f" {row['Product']:<30} Revenue: ${row['Revenue']:>12,.0f}")

print("\n BUDGET STRATEGY")
print("-"*55)
total_revenue = final_df['Revenue'].sum()
for _, row in final_df[final_df['Decision'] == 'BOOST'].iterrows():
    budget_pct = (row['Revenue'] / total_revenue * 100).round(1)
    print(f"  {row['Product']:<30} → {budget_pct}% of budget")

print("\n" + "="*55)
print("   STAGE 5 COMPLETE!")
print("="*55)

