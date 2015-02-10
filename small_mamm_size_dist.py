import pandas as pd
from into import into
from glob import glob

def import_data():
    datafiles = glob('data/NEON.*.csv')
    data = pd.DataFrame()
    for datafile in datafiles:
        new_data = pd.read_csv(datafile)
        data = data.append(new_data, ignore_index=True)
    return data

data = import_data()
