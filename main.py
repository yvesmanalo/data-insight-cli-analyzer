import pandas as pd
from utils.loader import FileLoader
from utils.analyzer import ViewDataSetPreview, ViewDataSetInfo, BasicStats, ComputeTotalSales, ApplyDiscount, ShowAggregateData, CheckDataTypes
from utils.filter import ShowFilteredData


print('''

========================================
   DATA INSIGHTS CLI ANALYZER
========================================
  
''')

file = FileLoader("data/sales_data.csv")
df = pd.DataFrame(file)

def MainMenu():
  print('''
  ========================================
  MAIN MENU
  ========================================
  1. View Dataset Preview
  2. View Dataset Info
  3. Show Basic Statistics
  4. Compute Total Sales
  5. Apply Discounts
  6. Aggregate Data (*args)
  7. Filter Data (**kwargs)
  8. Type Checks
  9. Exit
  ========================================
        ''')

  UserChoice = input("Enter choice using corresponding number: ")

  if UserChoice == "1":
    ViewDataSetPreview(df)
    PromptReturnToMainMenu()
  if UserChoice == "2":
    ViewDataSetInfo(df)
    PromptReturnToMainMenu()
  if UserChoice == "3":
    BasicStats(df)
    PromptReturnToMainMenu()
  if UserChoice == "4":
    ComputeTotalSales(df)
    PromptReturnToMainMenu()
  if UserChoice == "5":
    ApplyDiscount(df)
    PromptReturnToMainMenu()
  if UserChoice == "6":
    ShowAggregateData(df)
    PromptReturnToMainMenu()
  if UserChoice == "7":
    ShowFilteredData(df)
    PromptReturnToMainMenu()
  if UserChoice == "8":
    CheckDataTypes(df)
    PromptReturnToMainMenu()               
  if UserChoice == "9":
    ExitApplication()


def PromptReturnToMainMenu():
  choice = input("\nPress Enter to return to main menu... ")
  if choice == "":
    MainMenu()

def ExitApplication():
  print("\nThank you for using the app!")
  exit()


MainMenu()
