"""
Author: Lucas Mendes
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# INPUT VALUES
country = "Brazil"
column = "total_confirmed_new_cases"
title = country + " - Total Confirmed New Cases"

files_folder = "outputs/"
files = ["20200601-covid-19-sitrep-133.csv",
         "20200602-covid-19-sitrep-134.csv",
         "20200616-covid-19-sitrep-148-draft.csv",
         "20200617-covid-19-sitrep-149.csv",
         "20200618-covid-19-sitrep-150.csv",
         "20200619-covid-19-sitrep-151.csv"]

# Begin Code
final_data = pd.DataFrame()

for file in files:
    try:
        data = pd.read_csv(files_folder + file)
        r1 = data.query('country_territory_area == "' + country + '"')
        final_data = final_data.append(r1)
    except:
        print("Error in file reading - " + file)

try:
    plt.interactive(True)
    plt.figure(figsize=(10, 6))
    final_data = final_data.sort_values(by=['date'])
    final_data_plot = sns.barplot(x='date', y=column, data=final_data)
    plt.title(title)
    plt.show(block=True)
except:
    print("Error on trying to plot the result data.")
