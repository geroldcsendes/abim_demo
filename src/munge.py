# %%
import pandas as pd
import numpy as np
import os

# %%
# BAD WAY = ABSOLUTE PATH :-(
# raw_df = pd.read_csv(r"C:\Users\gcsendes\Desktop\munka\egyeb\DIM_data_science_env\demo\data\transactions.csv")

# GOOD WAY = RELATIVE PATH :-)
# works for every team member on the project
data_path = "data/"
raw_df = pd.read_csv(data_path + "raw/transactions.csv")

# %%
# check data
raw_df.info()

# %%
# impute missing cols
raw_df["county"].fillna(value="unknown", inplace=True)

# %%
raw_df.info()

# %%
# save interim data: cleaned raw data
raw_df.to_csv(data_path + "interim/transactions_interim.csv", index=False)
