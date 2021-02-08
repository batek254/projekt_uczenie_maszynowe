import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

path = str(Path(__file__).parents[2])

data = pd.read_csv(path + '/data/processed/data_processed_nans.csv')


sns.heatmap(data.isnull(), cbar=False)
plt.savefig(path + '/reports/figures/nans_plot.jpg')
