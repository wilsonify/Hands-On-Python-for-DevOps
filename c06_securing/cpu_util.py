# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.6
#   kernelspec:
#     display_name: Python 3
#     name: python3
# ---

# + id="GYLjRPQEBRBo"
# !pip install pandas matplotlib

# + id="Z3v5jtatBUoU"
import pandas as pd

df = pd.read_csv("MOCK_DATA.csv")
df.sort_values(by="timestamp", inplace=True)
df

# + id="z2wq3iLxDPIi"
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 20))
plt.plot(df['timestamp'], df['cpu_utilization'], label='Data')

plt.title('Plot for CPU utilization')
plt.xlabel('Time')
plt.ylabel('CPU utilization')
plt.grid(True)
plt.legend()

plt.show()

# + id="hSZlW__ZLtBR"

