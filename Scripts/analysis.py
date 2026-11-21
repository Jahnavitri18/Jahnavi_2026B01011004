from pathlib import Path
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

folder = Path(__file__).resolve().parent.parent
df = pd.read_csv(folder / "Data" / "processed" / "cleaned_ecommerce_sales.csv", parse_dates=["order_date"])
sold = df[df["returned"] == False]

sns.set_theme(style="whitegrid")

# ---------- Numbers in terminal (numpy) ----------
print(f"Total Revenue: ₹{np.sum(sold['sales']):,.2f}")
print(f"Average Order: ₹{np.mean(sold['sales']):,.2f}")
print(f"Median Order:  ₹{np.median(sold['sales']):,.2f}")
print("\nRegion-wise sales:")
print(sold.groupby("region")["sales"].sum().sort_values(ascending=False).round(2))

# ---------- Chart 1: Region-wise sales ----------
reg = sold.groupby("region", as_index=False)["sales"].sum().sort_values("sales", ascending=False)
ax = sns.barplot(data=reg, x="region", y="sales", hue="region", palette="viridis", legend=False)
ax.bar_label(ax.containers[0], fmt="₹%.0f")
plt.title("Region-wise Sales", fontsize=16, fontweight="bold")
plt.xlabel("Region")
plt.ylabel("Total Sales (₹)")
plt.tight_layout()
plt.savefig(folder / "Images" / "1_region_sales.png")
plt.show()

# ---------- Chart 2: State-wise sales ----------
st = sold.groupby("state", as_index=False)["sales"].sum().sort_values("sales", ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(data=st, y="state", x="sales", hue="state", palette="mako", legend=False)
plt.title("State-wise Sales", fontsize=16, fontweight="bold")
plt.xlabel("Total Sales (₹)")
plt.ylabel("State")
plt.tight_layout()
plt.savefig(folder / "Images" / "2_state_sales.png")
plt.show()



# ---------- Chart 3: Monthly trend ----------
monthly = sold.set_index("order_date")["sales"].resample("ME").sum().reset_index()
plt.figure(figsize=(10, 5))
sns.lineplot(data=monthly, x="order_date", y="sales", marker="o")
plt.title("Monthly Sales Trend", fontsize=16, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Total Sales (₹)")
plt.tight_layout()
plt.savefig(folder / "Images" / "3_monthly_trend.png")
plt.show()

# ---------- Chart 4: Payment modes ----------
plt.figure(figsize=(8, 5))
ax = sns.countplot(data=sold, x="payment_mode", hue="payment_mode", palette="Set2", legend=False)
ax.bar_label(ax.containers[0])
plt.title("Payment Modes", fontsize=16, fontweight="bold")
plt.xlabel("Payment Mode")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig(folder / "Images" / "4_payment_modes.png")
plt.show()

# ---------- Chart 5: sales by category ------------
sold.groupby("category")["sales"].sum().plot(kind="pie", autopct="%1.0f%%", figsize=(7, 7))
plt.title("Sales by Category", fontsize=16, fontweight="bold")
plt.ylabel("")
plt.savefig(folder / "Images" / "5_sales_by_category.png")
plt.show()
# numpy: correlation between discount and sales
corr = np.corrcoef(sold["discount_pct"], sold["sales"])[0, 1]
print(f"\nCorrelation between discount and sales: {corr:.2f}")
print("\nRevenue by category:")
print(sold.groupby("category")["sales"].sum().sort_values(ascending=False).round(2))

print("\nOrders by category:")
print(sold["category"].value_counts())

print("\nUnits sold by category:")
print(sold.groupby("category")["quantity"].sum().sort_values(ascending=False))