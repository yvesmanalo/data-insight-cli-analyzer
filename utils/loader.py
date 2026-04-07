import pandas as pd

def FileLoader(file_location):

  try:
    file = pd.read_csv(file_location)
    print("Loading dataset...")
    print("\nFile loaded successfully!\n")
    return file

        
  except FileNotFoundError:
    print(f"Error: File '{file_location}' not found.")
    print("Please check the file path and try again.")

    print("\nProgram terminated.")
    exit()
