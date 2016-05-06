from __future__ import print_function
import os
os.sys.path.append(os.path.join( os.path.dirname(__file__), '../'))
import pandas as pd
import numpy as np
from util import test_stationarity, convert_int_to_date
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
import numpy as np


def arima(item_id):

    ts_df = qty_item_df[(qty_item_df.item_id == item_id)]
    ts_df = ts_df.iloc[xrange(ts_df.shape[0]-1,-1,-1),:]
    ts_df['qty'] = ts_df.qty.values[xrange(ts_df.shape[0]-1,-1,-1)]

    # judge stationary
    #test_stationarity(ts_df.qty, 8)

    '''
    # judge order of difference
    ts_df.qty.plot(figsize=(12,8))

	fig = plt.figure(figsize=(12,8))
	ax1= fig.add_subplot(111)
	diff1 = ts_df.qty.diff(1)
    diff1.plot(ax=ax1)

	fig = plt.figure(figsize=(12,8))
	ax2= fig.add_subplot(111)
	diff2 = ts_df.qty.diff(2)
	diff2.plot(ax=ax2)
    plt.show()
	'''

    true_qty = ts_df.qty.iloc[-1]

    ts_df = ts_df.iloc[:-1,:]
    ts = ts_df.qty.diff(1)
    ts = ts_df.qty.astype(float)
    ts.index = pd.Index(ts_df.beg_date.apply(convert_int_to_date))
    #ts.index = pd.Index(sm.tsa.datetools.dates_from_range('2001','2031'))
    ts.index = pd.DatetimeIndex(ts_df.beg_date.apply(convert_int_to_date))
    fig = plt.figure(figsize=(12,8))
    ax1=fig.add_subplot(211)
    fig = sm.graphics.tsa.plot_acf(ts[1:],lags=20,ax=ax1)
    ax2 = fig.add_subplot(212)
    fig = sm.graphics.tsa.plot_pacf(ts[1:],lags=20,ax=ax2)
    #plt.show()

    #print(ts.index)
    arma_mod = sm.tsa.ARMA(ts,(4,2)).fit()
    #print(arma_mod.aic,arma_mod.bic,arma_mod.hqic)

    #print(ts)
    #predicted = arma_mod.predict('20151228', '20151228', dynamic=True)
    predicted = arma_mod.predict('20151214', '20151214', dynamic=True)
    print('%f\t%f' % (true_qty, predicted))
    fig, ax = plt.subplots(figsize=(12, 8))
    ax = ts.ix[:].plot(ax=ax)
    predicted.plot(ax=ax)
    #plt.plot(predicted, ax=ax)
    #plt.show()

if __name__ == '__main__':
    # qty, item_id, beg_date
    qty_item_df = pd.read_csv('../data/qty_item.csv')

    item_id = 168348 
    #item_id = 197 
    #item_id = 300 

    unique_items = np.unique(qty_item_df.item_id)

    for item_id in unique_items:
       arima(item_id)
