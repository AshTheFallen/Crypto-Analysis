import pandas as pd
import numpy as np
from pathlib import Path
import torch

def read_coin_data(address, name):
    return pd.read_csv(Path(address + '/coin_' + name + '.csv'))

df = read_coin_data('H:\Projects\Datasets\Crypto','Aave')
print(df)

