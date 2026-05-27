# ================================================
# TECHMART AD OPTIMIZATION - STREAMLIT APP
# Author: Muhammad Usman
# ================================================

import streamlit as st
import pandas as pd

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="TechMart Ad Optimizer",
    page_icon="🚀",
    layout="wide"
)

# ---- LOAD DATA ----
@st.cache_data
def load_data():
    sales_df = pd.read_csv("All_Sales_clean.csv")
    ads_df = pd.read_csv("Ads_clean.csv")
    return sales_df, ads_df

sales_df, ads_df = load_data()

# ---- PRODUCT MAP ----
product_map = {
    'A': 'iPhone', 'B': 'Macbook Pro Laptop',
    'C': 'Apple Airpods Headphones', 'D': 'USB-C Charging Cable',
    'E': 'AA Batteries (4-pack)', 'F': 'AAA Batteries (4-pack)',
    'G': 'Wired Headphones', 'H': 'Bose SoundSport Headphones',
    'I': '27in FHD Monitor', 'J': '27in 4K Gaming Monitor',
    'K': '34in Ultrawide Monitor', 'L': 'Google Phone',
    'M': 'Flatscreen TV', 'N': 'ThinkPad Laptop',
    'O': '20in Monitor', 'P': 'Vareebadd Phone',
    'Q': 'LG Washing Machine', 'R': 'LG Dryer',
    'S': 'Lightning Charging Cable'
}

# ---- SIDEBAR ----
st.sidebar.title("🚀 TechMart Optimizer")
st.sidebar.markdown("---")
page = st.sidebar.selectbox("Navigate", [
    "📊 Dashboard",
    "🎯 Company Strategy",
    "📋 Final Report"
])

# ================================================
# PAGE 1 — DASHBOARD
# ================================================
if page == "📊 Dashboard":
    st.title("📊 TechMart Sales Dashboard")
    st.markdown("---")

    # KPI Cards
    total_revenue = sales_df['Revenue'].sum()
    total_orders = sales_df['Quantity Ordered'].sum()
    best_product = sales_df.groupby('Product')['Revenue'].sum().idxmax()
    best_city = sales_df.groupby('City')['Revenue'].sum().idxmax()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("💰 Total Revenue", f"${total_revenue:,.0f}")
    c2.metric("📦 Total Orders", f"{total_orders:,}")
    c3.metric("🏆 Best Product", best_product)
    c4.metric("🌆 Best City", best_city)

    st.markdown("---")

    # Revenue by Product
    st.subheader("💰 Revenue by Product")
    product_rev = sales_df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
    st.bar_chart(product_rev)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌆 Revenue by City")
        city_rev = sales_df.groupby('City')['Revenue'].sum().sort_values(ascending=False)
        st.bar_chart(city_rev)

    with col2:
        st.subheader("📅 Monthly Sales Trend")
        monthly = sales_df.groupby('Month')['Quantity Ordered'].sum()
        st.line_chart(monthly)

    st.subheader("⏰ Sales by Hour of Day")
    hourly = sales_df.groupby('Hour')['Quantity Ordered'].sum()
    st.bar_chart(hourly)

# ================================================
# PAGE 2 — COMPANY STRATEGY
# ================================================
elif page == "🎯 Company Strategy":
    st.title("🎯 Company Ad Strategy Generator")
    st.write("Enter your details below and get a complete advertising strategy!")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        product = st.selectbox("🛍️ Select Product", list(product_map.values()))
    with col2:
        budget = st.number_input("💵 Ad Budget ($)", min_value=100, max_value=10000000, value=1000, step=100)
    with col3:
        city = st.selectbox("🌆 Target City", sorted(sales_df['City'].unique()))

    st.markdown("---")

    if st.button("🔮 GENERATE STRATEGY", use_container_width=True):

        ads_copy = pd.read_csv("Ads_clean.csv")

        # ---- PRODUCT DATA ----
        prod_data = sales_df[sales_df['Product'] == product]
        prod_revenue = prod_data['Revenue'].sum()
        prod_units = prod_data['Quantity Ordered'].sum()
        all_revenues = sales_df.groupby('Product')['Revenue'].sum()
        prod_rank = int(all_revenues.rank(ascending=False)[product])
        avg_order_value = prod_revenue / max(prod_units, 1)

        # ---- PRODUCT TIMING ----
        best_month = prod_data.groupby('Month')['Quantity Ordered'].sum().idxmax()
        best_hour = prod_data.groupby('Hour')['Quantity Ordered'].sum().idxmax()
        best_day = prod_data.groupby('Day')['Quantity Ordered'].sum().idxmax()

        # ---- CITY + PRODUCT DATA ----
        city_prod_data = sales_df[
            (sales_df['City'] == city) &
            (sales_df['Product'] == product)
        ]
        city_product_revenue = city_prod_data['Revenue'].sum()
        city_product_units = city_prod_data['Quantity Ordered'].sum()

        # ---- CITY BUDGET SPLIT ----
        city_total_rev = sales_df[sales_df['City'] == city]['Revenue'].sum()
        total_rev = sales_df['Revenue'].sum()
        city_pct = round(city_total_rev / total_rev * 100, 1)
        city_budget = round(budget * city_pct / 100, 2)
        remaining_budget = round(budget - city_budget, 2)

        # ---- CAMPAIGN ROI ----
        camp_key = [k for k, v in product_map.items() if v == product]
        if camp_key:
            camp_data = ads_copy[ads_copy['Campaign'] == camp_key[0]]
            total_spent = camp_data['Spent'].sum()
            total_conv = camp_data['Approved_Conversion'].sum()
            roi = round(total_conv / total_spent * 100, 2) if total_spent > 0 else 0
            cost_per_conv = round(total_spent / max(total_conv, 1), 2)

            # ---- BUDGET DEPENDENT CALCULATIONS ----
            expected_conv = round(budget / max(cost_per_conv, 1))
            expected_revenue = round(expected_conv * avg_order_value, 2)
            expected_profit = round(expected_revenue - budget, 2)
            actual_roi = round((expected_revenue - budget) / budget * 100, 1)

            # City specific budget calculations
            city_expected_conv = round(city_budget / max(cost_per_conv, 1))
            city_expected_revenue = round(city_expected_conv * avg_order_value, 2)
            city_expected_profit = round(city_expected_revenue - city_budget, 2)
        else:
            roi = cost_per_conv = expected_conv = 0
            expected_revenue = expected_profit = actual_roi = 0
            city_expected_conv = city_expected_revenue = city_expected_profit = 0

        # ---- AUDIENCE ----
        if camp_key:
            camp_ads = ads_copy[ads_copy['Campaign'] == camp_key[0]]
        else:
            camp_ads = ads_copy

        best_age = camp_ads.groupby('age')['Approved_Conversion'].sum().idxmax()
        gender_conv = camp_ads.groupby('gender')['Approved_Conversion'].sum()
        best_gender = "Male" if gender_conv.idxmax() == 1 else "Female"
        best_interest = camp_ads.groupby('interest')['Approved_Conversion'].sum().nlargest(3).index.tolist()

        # ---- DECISION ----
        if prod_revenue >= 3000000:
            decision = "🚀 BOOST"
            decision_msg = "High potential! Increase your ad budget!"
        elif prod_revenue >= 500000:
            decision = "✅ MAINTAIN"
            decision_msg = "Average performer. Keep current budget."
        else:
            decision = "❌ DISCARD"
            decision_msg = "Low revenue. Consider discount or stop ads."

        # ================================================
        # SHOW RESULTS
        # ================================================
        st.success("✅ Strategy Generated!")
        st.markdown("---")

        # ---- MARKET ANALYSIS ----
        st.subheader("📊 Market Analysis")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Product Rank", f"#{prod_rank} of 19")
        c2.metric("Total Revenue", f"${prod_revenue:,.0f}")
        c3.metric(f"Revenue in {city}", f"${city_product_revenue:,.0f}")
        c4.metric(f"Units Sold in {city}", f"{int(city_product_units):,}")

        # ---- TIMING STRATEGY ----
        st.subheader("⏰ Timing Strategy")
        c1, c2, c3 = st.columns(3)
        c1.metric("Best Month", f"Month {best_month}")
        c2.metric("Best Hour", f"{best_hour}:00")
        c3.metric("Best Day", str(best_day))

        # ---- LOCATION & BUDGET ----
        st.subheader("🌆 Location & Budget Strategy")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("City Revenue Share", f"{city_pct}%")
        c2.metric(f"Budget for {city}", f"${city_budget:,.2f}")
        c3.metric(f"Expected Conversions in {city}", f"{city_expected_conv}")
        c4.metric(f"Expected Revenue in {city}", f"${city_expected_revenue:,.0f}")

        # ---- ROI & CONVERSION FORECAST ----
        st.subheader("💰 ROI & Conversion Forecast")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Cost Per Conversion", f"${cost_per_conv}")
        c2.metric("Expected Conversions", f"{expected_conv}")
        c3.metric("Expected Revenue", f"${expected_revenue:,.0f}")
        c4.metric("Expected Profit",
                  f"${expected_profit:,.0f}",
                  delta=f"{actual_roi}% ROI")

        # ---- AUDIENCE STRATEGY ----
        st.subheader("👥 Audience Strategy")
        c1, c2, c3 = st.columns(3)
        c1.metric("Best Age Group", f"{best_age}-{best_age+4}")
        c2.metric("Best Gender", best_gender)
        c3.metric("Top Interests", str(best_interest))

        # ---- FINAL DECISION ----
        st.subheader("🚀 Final Decision")
        if "BOOST" in decision:
            st.success(f"{decision} — {decision_msg}")
            st.balloons()
        elif "MAINTAIN" in decision:
            st.warning(f"{decision} — {decision_msg}")
        else:
            st.error(f"{decision} — {decision_msg}")
            st.info("💡 Suggestion: Add 20-30% discount to boost sales!")


# ================================================
# PAGE 4 — FINAL REPORT
# ================================================
elif page == "📋 Final Report":
    st.title("📋 TechMart Ad Optimization Report")
    st.markdown("---")

    ads_copy = pd.read_csv("Ads_clean.csv")

    # Sales Insights
    best_month = sales_df.groupby('Month')['Quantity Ordered'].sum().idxmax()
    best_hour = sales_df.groupby('Hour')['Quantity Ordered'].sum().idxmax()
    best_day = sales_df.groupby('Day')['Quantity Ordered'].sum().idxmax()
    best_city = sales_df.groupby('City')['Revenue'].sum().idxmax()

    # Ads Insights
    best_age = ads_copy.groupby('age')['Approved_Conversion'].sum().idxmax()
    gender_conv = ads_copy.groupby('gender')['Approved_Conversion'].sum()
    best_gender = "Male" if gender_conv.idxmax() == 1 else "Female"
    best_interest = ads_copy.groupby('interest')['Approved_Conversion'].sum().nlargest(3).index.tolist()

    # Campaign Performance
    campaign_perf = ads_copy.groupby('Campaign').agg({
        'Approved_Conversion': 'sum',
        'Spent': 'sum'
    }).reset_index()
    campaign_perf['ROI'] = (campaign_perf['Approved_Conversion'] /
                            campaign_perf['Spent'] * 100).round(2)
    campaign_perf['Product'] = campaign_perf['Campaign'].map(product_map)

    sales_summary = sales_df.groupby('Product')['Revenue'].sum().reset_index()
    final_df = campaign_perf.merge(sales_summary, on='Product', how='left')

    def make_decision(row):
        revenue = row['Revenue']
        roi = row['ROI']
        if revenue >= 3000000:
            return '🚀 BOOST'
        elif roi >= 2.0 and revenue >= 2000000:
            return '🚀 BOOST'
        elif revenue >= 500000:
            return '✅ MAINTAIN'
        else:
            return '❌ DISCARD'

    final_df['Decision'] = final_df.apply(make_decision, axis=1)

    # KPIs
    st.subheader("🔑 Key Insights")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Best Age Group", f"{best_age}-{best_age+4}")
    c2.metric("Best Gender", best_gender)
    c3.metric("Best City", best_city)
    c4.metric("Best Month", f"Month {best_month}")

    st.subheader("⏰ Timing Strategy")
    c1, c2 = st.columns(2)
    c1.metric("Peak Hour", f"{best_hour}:00")
    c2.metric("Best Day", str(best_day))

    st.subheader("🎯 Top Interest Groups")
    st.info(f"Target these interest groups: {best_interest}")

    st.subheader("📊 Product Decisions")

    boost = final_df[final_df['Decision'] == '🚀 BOOST'][['Product', 'ROI', 'Revenue', 'Decision']]
    maintain = final_df[final_df['Decision'] == '✅ MAINTAIN'][['Product', 'ROI', 'Revenue', 'Decision']]
    discard = final_df[final_df['Decision'] == '❌ DISCARD'][['Product', 'ROI', 'Revenue', 'Decision']]

    st.success(f"🚀 BOOST — {len(boost)} Products")
    st.dataframe(boost, use_container_width=True)

    st.warning(f"✅ MAINTAIN — {len(maintain)} Products")
    st.dataframe(maintain, use_container_width=True)

    st.error(f"❌ DISCARD — {len(discard)} Products")
    st.dataframe(discard, use_container_width=True)

    st.subheader("💰 Budget Allocation")
    total_boost_rev = boost['Revenue'].sum()
    for _, row in boost.iterrows():
        pct = int(round(row['Revenue'] / total_boost_rev * 100))
        st.progress(pct, text=f"{row['Product']} → {pct}% of budget")