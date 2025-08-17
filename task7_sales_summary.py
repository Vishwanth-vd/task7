import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite DB
conn = sqlite3.connect("sales_data.db")

# Run basic SQL (quantity & revenue per product)
query = """
SELECT 
  product, 
  SUM(quantity) AS total_qty, 
  ROUND(SUM(quantity * price), 2) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC
"""
df = pd.read_sql_query(query, conn)

# Print results
print(df.to_string(index=False))

# Optional grand totals
print("\nTOTAL QUANTITY SOLD:", int(df["total_qty"].sum()))
print("TOTAL REVENUE:", float(df["revenue"].sum()))

# Plot simple bar chart
plt.figure()
plt.bar(df["product"], df["revenue"])
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()