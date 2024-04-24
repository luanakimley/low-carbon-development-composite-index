import pandas as pd

# Load data

forest_area = pd.read_csv("dataset/Forest Area.csv")
freshwater = pd.read_csv("dataset/Freshwater.csv", skiprows=3)
gdp_per_capita = pd.read_csv("dataset/gdp_per_capita.csv")
governance = pd.read_csv("dataset/Governance.csv")
human_development_index = pd.read_csv("dataset/Human Development Index.csv")
sustainable_energy = pd.read_csv("dataset/Sustainable energy for all.csv", skiprows=3)
emissions = pd.read_csv("dataset/trends_in_greenhouse_gas_emissions.csv", skiprows=3)



# Choosing the relevant variables

# Forest area
forest_area_filtered = forest_area[['Country and Area', 'Forest Area, 2020 (1000 ha)', 'Total Land Area, 2020 (1000 ha)', "Forest Area as a  Proportion of (%)\nTotal Land Area, 2020"]]
# print(forest_area_filtered_2020.head())

# Freshwater
freshwater_filtered = freshwater[['Country', 'Internal renewable freshwater resources flows 2020']]
# print(freshwater_filtered_2020.head())

# GDP per capita
gdp_per_capita_filtered = gdp_per_capita[['Country Name', '2020']]
# print(gdp_per_capita_filtered_2020.head())

# Governance
governance_filtered = governance[['Country and area', 'Paris Agreement', 'UN Framework Convention on Climate Change']]
# print(governance_filtered.head())

# Human Development Index
human_development_index_filtered = human_development_index[['Country', 'Human Development Index (2021)']]
# print(human_development_index_filtered.head())

# Sustainable energy
sustainable_energy_filtered = sustainable_energy[['Country', 'Access to clean fuels and technologies for cooking 2021', 'Renewable energy consumption 2020']]
# print(sustainable_energy_filtered.head())

# Emissions
emissions_filtered = emissions[['Country', 'Carbon dioxide emissions 2020', 'Methane emissions 2020', 'Nitrous oxide emissions 2020']]
# print(emissions_filtered.head())
