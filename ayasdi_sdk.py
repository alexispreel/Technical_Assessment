from __main__ import *
import pandas as pd
def ayasdi_loader(file_name):
    dataset = pd.read_csv(file_name)
    print 'Loading data from ', file_name, '...'
    print dataset.head(5)