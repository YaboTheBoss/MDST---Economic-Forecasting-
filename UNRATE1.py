import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


unrate1 = pd.read_csv(r"D:\MAE\Michigan Data Science Team\Econ Forecasting\Econ Project forecast\MDST---Economic-Forecasting-\UNRATE.csv")

unrate1 ['DATE'] =pd.to_datetime(unrate1['DATE'])
unrate1['YEAR'] = unrate1['DATE'].dt.year
unrate1['MONTH_NAME'] = unrate1['DATE'].dt.month_name()

year_trend= unrate1.groupby('YEAR')['UNRATE'].median().reset_index()
plt.figure(figsize=(10, 6))
plt.plot(year_trend['YEAR'], year_trend['UNRATE'], marker='o', linestyle='-', color='b')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate')
plt.title('Unemployment Per Year')
plt.grid(True)

plt.show