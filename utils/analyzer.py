import pandas as pd

def ViewDataSetPreview(df):
  print("\nShowing first 5 rows...\n")
  print(df.head())

def ViewDataSetInfo(df):
  print("\nDataset Information:\n")
  print(df.info())

def BasicStats(df):
  print("\nBasic Statistics:\n")

  df_shape = df.shape
  total_orders = df_shape[0]
  min_price = df["price"].min()
  max_price = df["price"].max()
  total_quantity_sold = df["quantity"].sum()
  distinct_categories = sorted(set(df["category"]))

  print(f"Total orders: {total_orders}")
  print(f"Min. Price: {min_price}")
  print(f"Max. Price: {max_price}")
  print(f"Total quantity sold: {total_quantity_sold}")
  print(f"Sorted Categories:\n{distinct_categories}")

def ComputeTotalSales(df):
  print("\nComputing total sales...\n")
  print("'total_sales' column added successfully!\n")
  df["total_sales"] = df["price"] * df["quantity"]
  print(df.head())

def ApplyDiscount(df):
  print("\nApplying discounts...\n")
  print("Discount Applied\n")
  df["discount_rate"] = df["category"].apply(lambda x: 0.1 if x == "Electronics" else (0.05 if x == "Clothing" else 0 ))
  df["discounted_total"] = df["total_sales"] * (1 - df["discount_rate"])
  print(df.head())

def ShowAggregateData(df):
  print("\nEnter column name(s) to aggregate (e.g price, quantity):")
  print("Note: Add comma or space for multiple column names\n")

  UserInputColumns = input("> ")
  TransformedUserInputColumns = []
  if "," in UserInputColumns:
    TransformedUserInputColumns += UserInputColumns.replace(",","").split()
  else:
    TransformedUserInputColumns += UserInputColumns.split()

  print("\nAggregated Results:\n")

  GetAggregateColumnsSum(df,*TransformedUserInputColumns)

def CheckDataTypes(df):
  print("\nData Type Checks:\n")
  print(f"Type of dataset: {type(df)}")
  for col in df.columns:
    print(f"Type of '{col}' column: {type(df[col])}")

def GetAggregateColumnsSum(df,*args):

  for col in args:
    try:
      column_sum = df[col].sum()
      print(f"{col} sum: {column_sum}")
    except KeyError:
      print(f"Column: {col} not in the current dataframe.")






