def ShowFilteredData(df):
  print("\nEnter category to filter:")
  UserInputCategory = input("> ").title().strip()
  print("Enter minimum price to filter:")
  UserInputMinPrice = int(input("> "))

  GetFilteredData(df, category=UserInputCategory, min_price = UserInputMinPrice) 

def GetFilteredData(df, **kwargs):
  if kwargs["category"] in set(df["category"]):
    df_filtered_data = df[(df["category"] == kwargs["category"]) & (df["price"] >= kwargs["min_price"])]
    df_filtered_data_shape = df_filtered_data.shape
    print("\nFiltered Results:\n")
    print(f"Matching records: {df_filtered_data_shape[0]}\n")
    print(df_filtered_data)
  else:
    print(f"Category: {kwargs["category"]} not in the current list of distinct categories")

  
