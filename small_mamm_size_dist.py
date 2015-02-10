import pandas as pd
from into import into
from glob import glob
import numpy as np
import matplotlib.pyplot as plt

def import_data():
    """Import data files from the ./data directory"""
    datafiles = glob('data/NEON.*.csv')
    data = pd.DataFrame()
    for datafile in datafiles:
        new_data = pd.read_csv(datafile)
        data = data.append(new_data, ignore_index=True)
    return data

def make_size_dist(weights):
    """Make a histogram representing the individual size distribution"""
    weights = weights.dropna().values
    plt.hist(np.log(weights))

data = import_data()
for i, (site, site_data) in enumerate(data.groupby('siteID')):
    plt.subplot(3, 4, i)
    make_size_dist(site_data['weight'])
plt.show()
