import pandas as pd 
import numpy as np

def lag1_var(df, var_list):
    """
    Returns dataframe augmented with lagged vars as specifiend in var_list.
    Args:
        df: (pd.DataFrame) df to work with
        var_list: (list) variables to make lag(1)
    """

    var_list_1 = [element + "_1" for element in var_list]
    df[var_list_1] = df. \
                        groupby("id")[var_list]. \
                            shift(1)

    return df
