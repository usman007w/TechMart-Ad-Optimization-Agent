# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:58:32 2026

@author: usman
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

sales_df = pd.read_csv("All_Sales_clean.csv")
ads_df = pd.read_csv("Ads_clean.csv")

le_product = LabelEncoder()
le_city = LabelEncoder()
le_day = LabelEncoder()

sales_df['Product'] = le_product.fit_transform(sales_df['Product'])
sales_df['City'] = le_city.fit_transform(sales_df['City'])
sales_df['Day'] = le_day.fit_transform(sales_df['Day'])

#Regression
#Target
X_sales = sales_df.drop(columns=['Revenue'])
y_sales = sales_df['Revenue']
print("Sales Features:", X_sales.columns.tolist())
print("Target is Revenue")

#Leakage problem
X_sales = sales_df.drop(columns=[
    'Revenue',
    'Price Each',        # Leakage!
    'Quantity Ordered'   # Leakage!
])
y_sales = sales_df['Revenue']
print("Sales Features:", X_sales.columns.tolist())

#split in to 20% , 80%
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X_sales, y_sales,
    test_size=0.2,
    random_state=42
)
print(f"Training rows: {X_train_s.shape[0]:,}")
print(f"Testing rows:  {X_test_s.shape[0]:,}")

#Model 1:Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train_s, y_train_s)
lr_pred = lr_model.predict(X_test_s)

# Model 2: Decision Tree Regressor
dt_reg = DecisionTreeRegressor(max_depth=5, random_state=42)
dt_reg.fit(X_train_s, y_train_s)
dt_reg_pred = dt_reg.predict(X_test_s)

# accuracy of Regression model
for name, pred in [('Linear Regression', lr_pred),
                   ('Decision Tree Regressor', dt_reg_pred)]:
    print(f"\n{name}:")
    print(f"MAE  : ${mean_absolute_error(y_test_s, pred):,.2f}")
    print(f"RMSE : ${np.sqrt(mean_squared_error(y_test_s, pred)):,.2f}")
    print(f"R²   : {r2_score(y_test_s, pred):.4f}")
    
    
#Classification
le_campaign = LabelEncoder()
le_product = LabelEncoder()

ads_df['Campaign'] = le_campaign.fit_transform(ads_df['Campaign'])
ads_df['Product'] = le_product.fit_transform(ads_df['Product'])

X_ads = ads_df.drop(columns=['Approved_Conversion'])
y_ads = ads_df['Approved_Conversion']

print("Ads Features:", X_ads.columns.tolist())   

#Split 20% ,80%
X_train_a, X_test_a, y_train_a, y_test_a = train_test_split(
    X_ads, y_ads,
    test_size=0.2,
    random_state=42
)

print(f"Training rows: {X_train_a.shape[0]}")
print(f"Testing rows:  {X_test_a.shape[0]}") 

#training Classification Models 

# Model 1 Knn
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train_a, y_train_a)
knn_pred = knn_model.predict(X_test_a)

# Model 2 Decision Tree
dt_clf = DecisionTreeClassifier(max_depth=5, random_state=42)
dt_clf.fit(X_train_a, y_train_a)
dt_clf_pred = dt_clf.predict(X_test_a)

#Accuracy of Classification Models
for name, pred in [('kNN', knn_pred),
                   ('Decision Tree', dt_clf_pred)]:
    print(f"\n{name}:")
    print(classification_report(y_test_a, pred))

#imbalance problem
ads_df['Approved_Conversion'] = (
    ads_df['Approved_Conversion'] > 0
).astype(int)
print("Conversion counts:")
print(ads_df['Approved_Conversion'].value_counts())

# CONFUSION MATRIX
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
for idx, (name, pred) in enumerate({
    'kNN': knn_pred,
    'Decision Tree': dt_clf_pred
}.items()):
    cm = confusion_matrix(y_test_a, pred)
    sns.heatmap(cm,
                annot=True,
                fmt='d',
                cmap='Blues',
                ax=axes[idx])
    axes[idx].set_title(f'{name} Confusion Matrix')
    axes[idx].set_xlabel('Predicted')
    axes[idx].set_ylabel('Actual')

plt.tight_layout()


# DECISION TREE PLOT
plt.figure(figsize=(20, 10))
plot_tree(dt_clf,
          feature_names=X_ads.columns.tolist(),
          class_names=['No Convert', 'Convert'],
          filled=True,
          rounded=True,
          fontsize=8)
plt.title("Ad Conversion Decision Tree", fontsize=16)
plt.tight_layout()

# Box plot
cols = ['age', 'gender', 'interest',
        'Impressions', 'Clicks', 'Spent',
        'Approved_Conversion']

fig, axes = plt.subplots(2, 4, figsize=(20, 12))
axes = axes.flatten()

for idx, col in enumerate(cols):
    axes[idx].boxplot(ads_df[col],
                      patch_artist=True,
                      boxprops=dict(facecolor='steelblue'))
    axes[idx].set_title(col, fontsize=14)
    axes[idx].set_ylabel("Value", fontsize=12)
    axes[idx].set_xticks([])

axes[7].set_visible(False)

plt.suptitle("Feature Distribution", fontsize=18)
plt.tight_layout()

#HeatMap
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(ads_df.corr(),
            annot=True,
            fmt='.2f',
            cmap='YlGnBu',
            ax=ax)
ax.set_title("Correlation Heatmap", fontsize=16)
plt.tight_layout()





















