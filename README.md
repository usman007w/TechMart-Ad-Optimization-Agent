# TechMart Ad Optimization Agent 🚀

**AI-powered system that analyzes sales and ad data to automatically recommend which ads to boost, maintain, or discard using Machine Learning.**

---

## 📊 Project Overview

TechMart Ad Optimization Agent is a complete machine learning project that processes real-world sales and advertising data to provide data-driven recommendations for optimizing ad spending and targeting strategies.

![image alt](https://github.com/usman007w/TechMart-Ad-Optimization-Agent/blob/main/Codes/outputs/Screenshot%202026-05-05%20021114.png?raw=true)

![image alt](https://github.com/usman007w/TechMart-Ad-Optimization-Agent/blob/main/Codes/outputs/Screenshot%202026-05-05%20104259.png?raw=true)

![image alt](https://github.com/usman007w/TechMart-Ad-Optimization-Agent/blob/main/Codes/outputs/Screenshot%202026-05-05%20104259.png?raw=true)

![image alt](https://github.com/usman007w/TechMart-Ad-Optimization-Agent/blob/main/Codes/outputs/Screenshot%202026-05-05%20012911.png?raw=true)

### Key Statistics
- **185,686** sales records analyzed
- **1,143** ad campaign records processed
- **19** products evaluated
- **4** ML models trained and compared
- **8** engineered features created
- **Zero** missing values after cleaning

---

## 🎯 Project Goals

1. **Predict Revenue** - Use ML to forecast revenue for each product based on sales patterns
2. **Predict Conversions** - Classify whether an ad will convert or not
3. **Generate Recommendations** - Automatically suggest which ads to BOOST, MAINTAIN, or DISCARD
4. **Provide Strategy** - Deliver complete ad optimization strategy including:
   - Target audience demographics (age, gender, interests)
   - Best timing (months, hours, days)
   - Best locations (cities)
   - Budget allocation percentages

---

## 📁 Project Structure

```
TechMart-Ad-Optimization-Agent/
├── App.py                          # Streamlit web application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── .gitignore                      # Git ignore rules
├── LICENSE                         # MIT License
└── outputs/                        # Generated visualizations
    ├── confusion_matrices.png      # ML model confusion matrices
    ├── ads_decision_tree.png       # Decision Tree visualization
    ├── box_plots.png               # Feature distribution plots
    ├── heatmap.png                 # Correlation heatmap
    ├── chart1_best_selling.png     # Best selling products
    ├── chart2_revenue.png          # Revenue by product
    ├── chart3_peak_month.png       # Peak sales month
    ├── chart4_peak_hour.png        # Peak sales hour
    └── chart5_best_city.png        # Best selling cities
```

---

## 🔧 Technologies Used

### Languages & Libraries
- **Python 3.8+** - Programming language
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine learning models
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical visualizations
- **Streamlit** - Web app framework

### ML Algorithms
- Linear Regression
- Decision Tree Regressor ✅ **Winner**
- kNN Classifier
- Decision Tree Classifier ✅ **Winner**

---

## 📊 Datasets

### Dataset 1: Sales Data (`All_Sales_clean.csv`)
**185,686 records | 8 columns | Zero missing values**

| Column | Type | Description |
|--------|------|-------------|
| Product | String | Product name (19 products) |
| Quantity Ordered | Integer | Units sold per transaction |
| Price Each | Float | Unit price in dollars |
| Month | Integer | Sales month (1-12) |
| Hour | Integer | Sales hour (0-23) |
| Day | String | Day of week |
| City | String | Purchase city (9 cities) |
| Revenue | Float | Quantity × Price (engineered) |

**Answers:** What sells? When? Where?

### Dataset 2: Ads Data (`Ads_clean.csv`)
**1,143 records | 8 columns | Zero missing values**

| Column | Type | Description |
|--------|------|-------------|
| Campaign | String | Campaign ID (A-S, 19 campaigns) |
| Age | Integer | User age (18-65) |
| Gender | Integer | 1=Male, 0=Female |
| Interest | Integer | Interest score (0-130) |
| Impressions | Integer | Ad impressions |
| Clicks | Integer | Ad clicks |
| Spent | Float | Ad spend in dollars |
| Approved Conversion | Integer | Conversions (target variable) |

**Answers:** Who buys? Which campaign converts?

---

## 🤖 Machine Learning Models

### Model 1: Revenue Predictor (Regression)

**Objective:** Predict exact revenue amount for each transaction

#### Results Comparison

| Metric | Linear Regression | Decision Tree | Winner |
|--------|-------------------|---------------|--------|
| MAE | $218.85 | **$52.93** | ✅ DT |
| RMSE | $326.85 | **$107.30** | ✅ DT |
| R² Score | 0.017 | **0.894** | ✅ DT |

**Why Decision Tree Won:**
- Revenue patterns are **non-linear** (not straight-line relationships)
- Product type, location, and time-of-day affect revenue in complex ways
- Decision Trees capture these complex interactions better
- **R² = 0.894** means the model explains **89.4%** of revenue variance

**Prediction Accuracy:** Average error of only **$52.93 per transaction** ✅

---

### Model 2: Conversion Predictor (Classification)

**Objective:** Predict YES/NO conversion for ads (binary classification)

#### Results Comparison

| Metric | kNN (k=5) | Decision Tree | Winner |
|--------|-----------|---------------|--------|
| Accuracy | 59% | **63%** | ✅ DT |
| Precision | 0.59 | **0.67** | ✅ DT |
| Recall | 0.59 | **0.63** | ✅ DT |
| F1 Score | 0.59 | **0.61** | ✅ DT |

**Why Decision Tree Won:**
- Handles imbalanced conversion data better
- Provides **interpretable decision rules** (visible in tree plot)
- More stable predictions on smaller datasets
- **Confusion matrix** shows clear performance metrics

---

## 📈 Key Findings & Business Insights

### Market Analysis
- **Best Revenue Product:** Macbook Pro ($8,032,500)
- **Best Selling Units:** AAA Batteries (31,000 units)
- **Revenue Rank 1:** Macbook Pro Laptop
- **Revenue Rank 2:** iPhone
- **Revenue Rank 3:** ThinkPad Laptop

### Target Audience
- **Best Age Group:** 30-34 years old
- **Best Gender:** Male (slightly higher conversion)
- **Top Interest Groups:** 16, 29, 10

### Timing Strategy
- **Peak Month:** December (holiday season)
- **Peak Hours:** 7PM & 12PM (bimodal distribution)
- **Best Day:** Tuesday
- **Pattern:** Morning lunch spike + evening shopping spike

### Geographic Strategy
- **Top City #1:** San Francisco ($8.25M) - Tech hub
- **Top City #2:** Los Angeles ($5.45M)
- **Top City #3:** New York City ($4.66M)

### Final Recommendations
- **🚀 BOOST (7 products):** Macbook Pro, iPhone, ThinkPad, Google Phone, Airpods, 4K Monitor, Ultrawide Monitor
- **✅ MAINTAIN (4 products):** Bose Headphones, Flatscreen TV, FHD Monitor, Vareebadd Phone
- **❌ DISCARD (8 products):** Batteries, USB-C Cable, Wired Headphones, LG Appliances, Lightning Cable, 20in Monitor

---

## 🚀 How to Run

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- pandas==1.5.0
- numpy==1.23.0
- scikit-learn==1.2.0
- matplotlib==3.7.0
- seaborn==0.12.0
- streamlit==1.51.0

### Step 2: Run the Streamlit App

```bash
streamlit run App.py
```

The app opens automatically in your default browser at:
```
http://localhost:8501
```

### Step 3: Explore the Dashboard

The app has **3 interactive pages:**

#### 📊 Dashboard Page
- View overall sales statistics
- Revenue by product chart
- Sales by city chart
- Peak hour and month charts

#### 🎯 Company Strategy Page
- **Input:** Select product, budget, target city
- **Output:** Complete data-driven ad strategy
  - Market analysis
  - Audience targeting
  - Timing recommendations
  - Budget allocation
  - BOOST/MAINTAIN/DISCARD decision

#### 📋 Final Report Page
- Complete agent recommendations
- All BOOST/MAINTAIN/DISCARD products
- Budget allocation percentages
- Full optimization strategy

---

## 📊 EDA (Exploratory Data Analysis)

### Sales Data Insights
1. **Best Selling Product:** AAA Batteries (31,000 units)
2. **Highest Revenue Product:** Macbook Pro ($8M)
3. **Peak Sales Hour:** 7PM (evening shopping)
4. **Peak Month:** December (holiday sales)
5. **Best City:** San Francisco (tech market)

### Ad Performance Insights
1. **Highest Converting Campaign:** Google Phone (L)
2. **Best ROI:** 2.69%
3. **Average Conversion Rate:** ~50% (binary)
4. **Best Audience Age:** 30-34
5. **Gender Split:** ~55% Male, ~45% Female

### Feature Distributions
- Age follows normal distribution centered at 35
- Gender is nearly balanced
- Interests are highly variable
- Impressions/Clicks are right-skewed (few viral ads)
- Spending follows exponential distribution

---

## 📚 Data Cleaning Process

### Step 1: Removed Duplicates
- Deleted duplicate header rows (1 row)

### Step 2: Fixed Data Types
- Converted `Quantity Ordered` to numeric
- Converted `Price Each` to numeric
- Parsed `Order Date` to datetime

### Step 3: Feature Engineering
- Extracted `Month` from Order Date
- Extracted `Hour` from Order Date
- Extracted `Day` name from Order Date
- Extracted `City` from Purchase Address
- Created `Revenue` = Quantity × Price

### Step 4: Handled Missing Values
- Dropped rows with NULL/missing values
- Result: **Zero missing values** ✅

### Step 5: Data Validation
- Verified all columns have correct types
- Confirmed no NULL values remain
- Final dataset: **185,686 rows × 8 columns**

---

## 🎓 Machine Learning Concepts Used

### Regression Metrics
- **MAE (Mean Absolute Error):** Average prediction error in dollars
- **RMSE (Root Mean Squared Error):** Penalizes large errors more
- **R² Score:** Percentage of variance explained (0-1 scale)

### Classification Metrics
- **Accuracy:** Percentage of correct predictions
- **Precision:** Of predicted conversions, how many correct?
- **Recall:** Of actual conversions, how many found?
- **F1 Score:** Harmonic mean of precision and recall

### Data Leakage Prevention
- Removed `Price Each` and `Quantity Ordered` from revenue prediction features
- These directly calculate revenue, so including them causes artificial high accuracy

### Train-Test Split
- 80% training data (used to learn patterns)
- 20% test data (used to evaluate performance)
- Random seed for reproducibility

---

## 📄 Project Files Description

| File | Purpose |
|------|---------|
| `App.py` | Main Streamlit web application |
| `requirements.txt` | Python package dependencies |
| `README.md` | Project documentation |
| `.gitignore` | Git ignore rules (Python template) |
| `LICENSE` | MIT open-source license |
| `outputs/` | All generated charts and visualizations |

---

## 🔒 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

MIT License allows:
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

Requires:
- ⚠️ License and copyright notice

---

## 👨‍💻 Author

**Muhammad Usman**
- Course: CSC-350 (Machine Learning)
- Project: AI Ad Optimization Agent
- Date: May 2026

---

## 📞 Support & Questions

If you have questions or issues:
1. Check the Streamlit app interface for interactive exploration
2. Review the confusion matrices in `outputs/` folder
3. Examine the decision tree visualization
4. Review the data cleaning steps in the README

---

## 🎯 Future Improvements

Potential enhancements:
- Add more ML algorithms (Random Forest, Gradient Boosting)
- Implement cross-validation for more robust evaluation
- Add interactive parameter tuning in Streamlit
- Include time-series forecasting for future revenue prediction
- Deploy to cloud (Heroku, AWS, Google Cloud)
- Add real-time data integration

---

## 📊 Performance Summary

| Aspect | Result | Status |
|--------|--------|--------|
| Data Cleaning | 100% accuracy | ✅ |
| Revenue Prediction (R²) | 0.894 | ✅ Excellent |
| Conversion Prediction | 63% accuracy | ✅ Good |
| Feature Engineering | 8 features | ✅ Complete |
| Documentation | Complete | ✅ |
| Web App | Fully functional | ✅ |

---

**Thank you for using TechMart Ad Optimization Agent!** 🚀

*Last Updated: May 27, 2026*
