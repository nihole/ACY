import yaml
import pandas as pd

data = """
thermal_properties:
- temp: 0.0
  free_energy: 10

- temp: 1.0
  free_energy: 11

- temp: 2.0
  free_energy: 12
"""
x = yaml.load(data,Loader=yaml.FullLoader)

pd.DataFrame(x['thermal_properties']).to_excel('file.xlsx')
