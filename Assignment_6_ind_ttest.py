import pandas as pd

import numpy as np

from scipy.stats import ttest_ind


df = pd.read_excel("/autograder/source/insulationdata.xlsx")

before_temp_array = np.array(df.loc[df["Insulate"] == "Before" , "Temp"])

after_temp_array = np.array(df.loc[df["Insulate"] == "After" , "Temp"])

equal_variance = True
if before_temp_array.std() > after_temp_array.std():
    if (before_temp_array.std()/after_temp_array.std()) > 2:
        equal_variance = False
else:
    if (after_temp_array.std()/before_temp_array.std()) > 2:
        equal_variance = False

results = ttest_ind(before_temp_array, after_temp_array, equal_var=equal_variance)

Temp_P_Value = results.pvalue


