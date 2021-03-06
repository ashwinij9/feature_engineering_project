# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')

def skewness_sqrt(ny_housing):
    ny_housing['GrLivArea'] = np.sqrt(ny_housing['GrLivArea'])
    ny_housing['SalePrice'] = np.sqrt(ny_housing['SalePrice'])
    return skew(ny_housing.GrLivArea),skew(ny_housing.SalePrice)
