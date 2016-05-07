import pandas as pd
import numpy as np

qty_item_df = pd.read_csv('data/xgb_qty.csv')
qty_item_store_df = pd.read_csv('data/qty_item_store.csv')
sub_df = pd.read_csv('data/sample_submission.csv')

target_list = []
for i in xrange(sub_df.shape[0]):
    print i
    row = sub_df.iloc[i,:]
    item_id = row.item_id 
    store_code = row.store_code
    if cmp(store_code, 'all') == 0:
        target = qty_item_df[(qty_item_df.item_id == item_id)].qty.iloc[0]
        #row.target = target
    else:
        target = qty_item_store_df[(qty_item_store_df.item_id == item_id) & (qty_item_store_df.store_code == int(store_code))].qty.iloc[0]
        #row.target = target
    target_list.append(target)

sub_df['target'] = target_list


sub_df.item_id = sub_df.item_id.astype('string')
sub_df.store_code = sub_df.store_code.astype('string')
sub_df.target = sub_df.target.astype(np.float64)


sub_df.to_csv('sub_xgb_base_qty.csv', index=False)
