from pathlib import Path
import pandas as pd
import numpy as np
folder = Path(__file__).resolve().parent.parent
df = pd.read_excel(folder / "Data" / "raw" / "Indian_Ecommerce_Sales Entries.xlsx")
print("Original shape:", df.shape)

# ---------- 2. Clean column names ----------
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(r"[\s\-]+", "_", regex=True)
)

# ---------- 3. Drop fully empty columns ----------
df = df.dropna(axis=1, how="all")   # removes internal_notes

# ---------- 4. Remove duplicates ----------
df = df.drop_duplicates()

# ---------- 5. Trim spaces in text columns ----------
for col in df.columns:
    if pd.api.types.is_string_dtype(df[col]) or pd.api.types.is_object_dtype(df[col]):
        df[col] = df[col].astype("string").str.strip()

# ---------- 6. Fix numbers stored as text ("33,070.00") ----------
for col in ["list_price", "sales"]:
    df[col] = pd.to_numeric(df[col].astype(str).str.replace(",", ""), errors="coerce")

# ---------- 7. Fix dates (DD-MM-YYYY) ----------
for col in ["order_date", "ship_date"]:
    df[col] = pd.to_datetime(df[col], format="%d-%m-%Y", errors="coerce")

# ---------- 8. Handle missing values ----------
for col in ["city", "order_priority", "gift_wrap", "warehouse_code"]:
    df[col] = df[col].fillna("Unknown")
df["sales_rep_id"] = df["sales_rep_id"].fillna("Unassigned")
# customer_feedback_score is left as NaN on purpose

# ---------- 9. Yes/No -> True/False ----------
df["returned"] = df["returned"].map({"Yes": True, "No": False})

# ---------- 10. New columns for analysis ----------
df["order_year"] = df["order_date"].dt.year
df["order_month"] = df["order_date"].dt.month
df["month_name"] = df["order_date"].dt.month_name()
df["ship_days"] = (df["ship_date"] - df["order_date"]).dt.days
df["gross_sales"] = df["list_price"] * df["quantity"]
df["discount_pct"] = ((1 - df["sales"] / df["gross_sales"]) * 100).round(1)

# ---------- 11. Quick checks ----------
print("Missing values:\n", df.isnull().sum())
print("Duplicate order IDs:", df["order_id"].duplicated().sum())
print("Negative ship days:", (df["ship_days"] < 0).sum())

# numpy: label each order by size
df["order_size"] = np.where(df["sales"] > 10000, "Large", "Small")

# numpy: round values
df["discount_pct"] = np.round(df["discount_pct"], 1)

# ---------- 12. Save ----------
df.to_csv(folder / "Data" / "processed" / "cleaned_ecommerce_sales.csv", index=False)
print("Saved to:", folder / "Data" / "processed" / "cleaned_ecommerce_sales.csv")
print("Cleaned shape:", df.shape)
print(df.head())