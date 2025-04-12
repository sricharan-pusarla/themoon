# import pandas as pd  # Import pandas

# # 1️⃣ Create DataFrame from Dictionary
# data = {
#     "Name": ["Alice", "Bob", "Charlie", "David"],
#     "Age": [25, 30, 35, None],  # None represents missing data
#     "City": ["New York", "Los Angeles", "Chicago", "Houston"],
#     "Salary": [50000, 60000, 70000, 80000]
# }
# df = pd.DataFrame(data)

# # 2️⃣ Display Basic Information
# print("\n📌 Data Overview")
# print(df.head())  # First 5 rows
# print("\nData Shape:", df.shape)  # Rows, Columns
# print("\nColumn Names:", df.columns.tolist())  # List of columns
# print("\nSummary Statistics:\n", df.describe())  # Numeric summary

# # 3️⃣ Handle Missing Data
# df["Age"].fillna(df["Age"].mean(), inplace=True)  # Replace NaN with column mean

# # 4️⃣ Data Selection & Filtering
# print("\n📌 Select Single Column:")
# print(df["Name"])  # Select one column

# print("\n📌 Select Multiple Columns:")
# print(df[["Name", "Salary"]])  # Select multiple columns

# print("\n📌 Select Rows Where Age > 30:")
# print(df[df["Age"] > 30])  # Filter rows based on condition

# # 5️⃣ Modify Data
# df["Salary"] = df["Salary"] * 1.10  # Increase salary by 10%
# df["Category"] = df["Age"].apply(lambda x: "Senior" if x > 30 else "Junior")  # Apply function

# # 6️⃣ Sorting & Grouping
# df_sorted = df.sort_values("Salary", ascending=False)  # Sort by Salary (Descending)
# print("\n📌 Sorted Data by Salary:\n", df_sorted)

# df_grouped = df.groupby("Category")["Salary"].mean()  # Group by 'Category' and get mean salary
# print("\n📌 Average Salary by Category:\n", df_grouped)

# # 7️⃣ Save Data to CSV
# df.to_csv("output.csv", index=False)
# print("\n✅ Data saved to 'output.csv'")
import pandas as pd
p=pd.read_csv(r"C:\Users\srika\Downloads\pokemon.csv")
p.groupby(['Type']).mean()