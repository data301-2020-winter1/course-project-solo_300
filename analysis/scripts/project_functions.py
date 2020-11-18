#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from sklearn.datasets import load_insurance

def load_and_process("C:\Users\Karl\Documents\ProjCOSC301\course-project-solo_300\data\raw\Medical_Cost.csv"):

    df = (   
        pd.DataFrame(data.data,columns=data.feature_names)
        .drop(['Region'], axis=1)
        .dropna()
        .sort_values("Age", ascending=True)
        .reset_index(drop=True)
    )
    return df

