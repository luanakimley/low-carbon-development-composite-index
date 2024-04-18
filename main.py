from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import pearsonr
import statsmodels.api as sm
import pandas as pd

# Load data
ch4_emissions = pd.read_csv("dataset/CH4_Emissions.csv", skiprows=1)
co2_emissions = pd.read_csv("dataset/CO2_Emissions.csv", skiprows=1)
forest_area = pd.read_csv("dataset/Forest Area.csv", skiprows=1)
fresh_groundwater_abstracted = pd.read_csv("dataset/Fresh groundwater abstracted.csv")
fresh_surface_water_abstracted = pd.read_csv("dataset/Fresh surface water abstracted.csv")
gdp_per_capita = pd.read_csv("dataset/gdp_per_capita.csv")
governance = pd.read_csv("dataset/Governance.csv")
n2o_emissions = pd.read_csv("dataset/N2O_Emissions.csv", skiprows=1)
nox_emissions = pd.read_csv("dataset/NOx_Emissions.csv", skiprows=1)
renewable_electricity_production_percentage = pd.read_csv("dataset/Renewable elec production percentage.csv")
so2_emissions = pd.read_csv("dataset/SO2_Emissions.csv", skiprows=1)

# Inputation of missing values

# Multivariate analysis

# Normalisation

# Weighting and aggregation
