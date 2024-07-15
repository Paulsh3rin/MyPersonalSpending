import pandas as pd


# file_paths = ["RawData/CheqMay23-June24.csv",
#                 "RawData/CredMay23-June24.csv",
#                 "RawData/SavMay23-June24.csv"]

# df = [pd.read_csv(file) for file in file_paths]
file = "RawData/CheqMay23-June24.csv"

df = pd.read_csv(file)
print(df.head())