# =========================================================
# PIZZALYTICS DATA ANALYSIS PROJECT
# =========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# ---------------------------------------------------------
# 1. DATA LOADING & CLEANING
# ---------------------------------------------------------

df = pd.read_csv("C://Users//kachireddy.reddy//Desktop//VSCode//Datasets//pizzalytics_orders.csv")

print("First 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

# Fill Missing Values
df["price"] = df["price"].fillna(df["price"].median())
df["quantity"] = df["quantity"].fillna(1)
df["customer_rating"] = df["customer_rating"].fillna(df["customer_rating"].mean())

# Standardize city names
df["city"] = df["city"].str.strip().str.title()

# Convert Date
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month_name()
df["weekday"] = df["date"].dt.day_name()

# Create Revenue Column
df["revenue"] = df["price"] * df["quantity"]

print("\nCleaned Data:")
print(df.head())

# ---------------------------------------------------------
# 2. BASIC ANALYSIS
# ---------------------------------------------------------

# Total Revenue
total_revenue = df["revenue"].sum()
print("\nTotal Revenue:", total_revenue)

# Average Order Value
avg_order_value = df.groupby("order_id")["revenue"].sum().mean()
print("Average Order Value:", avg_order_value)

# Top 5 Pizzas by Quantity
top5_pizzas = df.groupby("pizza_name")["quantity"].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Pizzas by Quantity:")
print(top5_pizzas)

# City with Highest Avg Rating
city_rating = df.groupby("city")["customer_rating"].mean().sort_values(ascending=False)
print("\nCity with Highest Average Rating:")
print(city_rating.head(1))

# Most Profitable Pizza Size
size_profit = df.groupby("size")["revenue"].sum().sort_values(ascending=False)
print("\nMost Profitable Size:")
print(size_profit)

# ---------------------------------------------------------
# 3. VISUALIZATIONS
# ---------------------------------------------------------

# # 1. Bar Plot - Top 5 Pizzas by Revenue
# top5_revenue = df.groupby("pizza_name")["revenue"].sum().sort_values(ascending=False).head(5)

# plt.figure(figsize=(10,6))
# top5_revenue.plot(kind="bar")
# plt.title("Top 5 Pizzas by Revenue")
# plt.xlabel("Pizzas")
# plt.ylabel("Revenue")
# plt.xticks(rotation=45)
# plt.tight_layout()  
# plt.show()

# # 2. Line Chart - Monthly Revenue Trend
# monthly_revenue = df.groupby("month")["revenue"].sum()

# plt.figure()
# monthly_revenue.plot(kind="line", marker="o")
# plt.title("Monthly Revenue Trend")
# plt.xlabel("Months")
# plt.ylabel("Revenue")
# plt.show()

# # 3. Pie Chart - Pizza Size Distribution
# size_distribution = df.groupby("size")["quantity"].sum()

# plt.figure()
# plt.pie(size_distribution, labels=size_distribution.index, autopct="%1.1f%%")
# plt.title("Pizza Size Distribution")
# plt.show()

# # 4. Scatter Plot - Price vs Rating (Color by Size)
# plt.figure()
# sns.scatterplot(data=df, x="price", y="customer_rating", hue="size")
# plt.title("Price vs Customer Rating")
# plt.show()

# # 5. Bar Plot - Revenue by City
# city_revenue = df.groupby("city")["revenue"].sum()

# plt.figure()
# city_revenue.plot(kind="bar")
# plt.title("Revenue by City")
# plt.xlabel("Cities")
# plt.ylabel("Revenue")
# plt.xticks(rotation=45)
# plt.tight_layout()  
# plt.show()

# # ---------------------------------------------------------
# # 4. ADVANCED INSIGHTS
# # ---------------------------------------------------------

# # Weekday Sales
# weekday_sales = df.groupby("weekday")["revenue"].sum()

# avg_sales = weekday_sales.mean()

# above_avg_days = weekday_sales[weekday_sales > avg_sales]

# print("\nWeekdays with Above Average Sales:")
# print(above_avg_days)

# # Marketing Suggestion
# best_day = weekday_sales.idxmax()
# print("\nSuggested Marketing Day:", best_day)

# # ---------------------------------------------------------
# # 5. BUILD THE PIZZA OF THE FUTURE
# # ---------------------------------------------------------

# # Combine Popularity + Revenue + Rating
# pizza_score = df.groupby("pizza_name").agg({
#     "quantity": "sum",
#     "revenue": "sum",
#     "customer_rating": "mean"
# })

# pizza_score["combined_score"] = (
#     pizza_score["quantity"] * 0.4 +
#     pizza_score["revenue"] * 0.4 +
#     pizza_score["customer_rating"] * 0.2
# )

# best_pizza = pizza_score.sort_values("combined_score", ascending=False).head(1)

# print("\nBest Performing Pizza Overall:")
# print(best_pizza)

# print("\n🍕 FUTURE PIZZA RECOMMENDATION 🍕")
# print("Launch a premium XL version of", best_pizza.index[0])
# print("Add trending toppings + combo offers to maximize profit and ratings.")

# # ---------------------------------------------------------
# # FINAL SUMMARY
# # ---------------------------------------------------------

# print("\n========== FINAL RECOMMENDATIONS ==========")
# print("• Focus marketing on", best_day)
# print("• Promote size:", size_profit.idxmax())
# print("• Expand in city:", city_rating.idxmax())
# print("• Feature top pizza:", best_pizza.index[0])
# print("===========================================")


# #average rating vs city
# plt.figure(figsize=(10,6))

# plt.bar(city_rating.index, city_rating.values)

# plt.title("Average Customer Rating vs City", fontsize=14)
# plt.xlabel("City")
# plt.ylabel("Average Rating")
# plt.ylim(0,5)   # Since rating scale is 1-5
# plt.xticks(rotation=45)
# plt.grid(axis="y", linestyle="--", alpha=0.7)

# plt.tight_layout()
# plt.show()


# #total income vs city
# # Total Revenue vs City (All-in-One Professional Version)

# city_revenue = df.groupby("city")["revenue"].sum().sort_values(ascending=False)

# plt.figure(figsize=(12,6))

# plt.plot(city_revenue.index,
#          city_revenue.values,
#          marker="o")

# plt.title("Total Revenue vs City", fontsize=14)
# plt.xlabel("City")
# plt.ylabel("Total Revenue")

# plt.xticks(rotation=45, ha="right")
# plt.grid(axis="y", linestyle="--", alpha=0.6)

# # Add data labels above points
# for i, value in enumerate(city_revenue.values):
#     plt.text(i, value, str(value),
#              ha="center",
#              va="bottom")

# plt.tight_layout()
# plt.show()

#sales vs weekdays

# Ensure datetime
df["date"] = pd.to_datetime(df["date"])

# Extract weekday
df["weekday"] = df["date"].dt.day_name()

# Aggregate revenue by weekday
weekday_sales = df.groupby("weekday")["revenue"].sum().reset_index()

# Correct weekday order
weekday_order = ["Monday","Tuesday","Wednesday",
                 "Thursday","Friday","Saturday","Sunday"]

weekday_sales["weekday"] = pd.Categorical(
    weekday_sales["weekday"],
    categories=weekday_order,
    ordered=True
)

weekday_sales = weekday_sales.sort_values("weekday")

plt.figure(figsize=(12,6))

bars = plt.bar(
    weekday_sales["weekday"],
    weekday_sales["revenue"]
)

# Highlight highest revenue day
max_index = weekday_sales["revenue"].idxmax()
bars[max_index].set_alpha(0.6)

# Add value labels
for i in range(len(weekday_sales)):
    plt.text(
        i,
        weekday_sales["revenue"].iloc[i],
        str(weekday_sales["revenue"].iloc[i]),
        ha="center",
        va="bottom"
    )

plt.title("Total Revenue by Weekday", fontsize=14)
plt.xlabel("Weekday")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()
