# %%
import pandas as pd 
import numpy as np
import src.lib.feature_helper as hp

# %%
# read in data
data_path = "data/"
transactions = pd.read_csv(data_path + "interim/transactions_interim.csv")

# %%
# lets create lagged vars for selected vars
# check how it works for one variable
transactions["trx_cnt_1"] = (transactions
                            .groupby("id")["trx_cnt"]
                            .shift(1))
# check res
transactions[["id", "yearmonth", "trx_cnt", "trx_cnt_1"]]

# %%
myres = hp.lag1_var(df=transactions, var_list=["trx_cnt", "sales", "churn_flag"])

# %%
# save feature engineered df
myres.to_csv(data_path + "/processed/transactions_processed.csv", index=False)

# %%
