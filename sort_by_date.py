import pandas as pd
import numpy as np

def sort_by_date_items(item_df):
    uni_items = np.unique(item_df.item_id)
    res_df = pd.DataFrame()
    for item in uni_items:
        print item
        cur_item_df = item_df[item_df.item_id == item]
        cur_item_df.sort_values('date', axis=0, inplace=True)
        if res_df.shape[0] == 0:
            res_df = cur_item_df
        else:
            res_df = pd.concat([res_df, cur_item_df])

    return res_df
 
def sort_by_date_item_stores(item_store_df):
    uni_items = np.unique(item_store_df.item_id)
    res_df = pd.DataFrame()
    for item in uni_items:
        print item
        cur_item_df = item_store_df[item_store_df.item_id == item]
        cur_item_df.sort_values(['date', 'store_code'], axis=0, inplace=True)
        if res_df.shape[0] == 0:
            res_df = cur_item_df
        else:
            res_df = pd.concat([res_df, cur_item_df])

    return res_df

if __name__ == '__main__':

    item_store_df = pd.read_csv('data/item_store_feature2.csv')
    item_df = pd.read_csv('data/item_feature2.csv')

    sorted_item_df = sort_by_date_items(item_df)
    sorted_item_df.to_csv('data/sorted_item_feature2.csv', index=False)    

    sorted_item_store_df = sort_by_date_item_stores(item_store_df)
    sorted_item_store_df.to_csv('data/sorted_item_store_feature2.csv', index=False)    
