import pandas as pd
import numpy as np
import scipy as sp  

def rmse(y_test, y):  
    return sp.sqrt(sp.mean((y_test - y) ** 2)) 

true_df = pd.read_csv('data/pre_2week_true_qty.csv')
cv_df = pd.read_csv('res/cv_pre_qty.csv')
xgb_cv_df = pd.read_csv('data/xgb_qty_valid_2.csv')
#xgb_cv_df = pd.read_csv('data/rf_qty_valid_1.csv')

true_df = true_df[true_df.store_code == 'all']
cv_df = cv_df[cv_df.store_code == 'all']
xgb_cv_df = xgb_cv_df.rename(columns={'target':'xgb_target'})
cv_df = pd.merge(cv_df, xgb_cv_df, on = ['item_id'])
print cv_df

true_qty = true_df.target.values
cv_qty = cv_df.target.values
xgb_cv_qty = cv_df.xgb_target.values

#print np.sqrt(np.sum((true_qty - cv_qty)**2)/cv_qty.shape[0])

print rmse(true_qty, cv_qty)
print rmse(true_qty, xgb_cv_qty)

true_df = true_df.rename(columns={'target':'true_target'})
test_df = pd.merge(true_df, cv_df, on = ['item_id']) 
test_df.to_csv('temp.csv', index=False)


