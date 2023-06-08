import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

  # Create scatter plot
  plt.figure(figsize=(10, 6))
  plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

  # Create first line of best fit
  slope, intercept, r_value, p_value, std_err = linregress(
    df['Year'], df['CSIRO Adjusted Sea Level'])
  years = range(1880, 2051)
  sea_levels = [slope * year + intercept for year in years]
  plt.plot(years, sea_levels, color='red', label='Line of Best Fit')

  # Create second line of best fit
  df_filtered = df[df['Year'] >= 2000]
  slope, intercept, r_value, p_value, std_err = linregress(
    df_filtered['Year'], df_filtered['CSIRO Adjusted Sea Level'])
  years = range(2000, 2051)
  sea_levels = [slope * year + intercept for year in years]
  plt.plot(years,
           sea_levels,
           color='green',
           label='Line of Best Fit (2000 onwards)')

  # Add labels and title
  plt.title('Rise in Sea Level')
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.legend()

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
