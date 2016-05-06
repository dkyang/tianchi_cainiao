import pandas as pd
import numpy as np
import datetime

def convert_int_to_date(int_date):
    year = int_date / 10000
    month = int_date % 10000 / 100
    day = int_date % 10000 % 100

    return datetime.date(year, month, day)

def convert_date_to_int(date):
    return date.year * 10000 + date.month * 100 + date.day

def get_pre_date(int_date, days):
    date =  convert_int_to_date(int_date)
    pre_date = date - datetime.timedelta(days)

    return convert_date_to_int(pre_date)  
     
def gen_qty_two_week_item(item_df):
    uni_items = np.unique(item_df.item_id)
    res_df = pd.DataFrame()
    beg_date_list = []
    qty_list = []
    item_id_list = []
    for item_id in uni_items:
        print item_id
        cur_item_df = item_df[item_df.item_id == item_id]
        end_date = 20151227
        beg_date = get_pre_date(end_date, 13)
        while beg_date >= 20141010:
            item_id_list.append(item_id)
            beg_date_list.append(beg_date)
            qty_df = cur_item_df[(cur_item_df.date >= beg_date) & (cur_item_df.date <= end_date)]

            #print qty_df
            qty_list.append(qty_df.qty_alipay_njhs.sum())
            end_date = get_pre_date(beg_date, 1)
            beg_date = get_pre_date(end_date, 13)

    res_df['qty'] = qty_list
    res_df['item_id'] = item_id_list
    res_df['beg_date'] = beg_date_list

    return res_df
            
def gen_qty_two_week_item_store(item_store_df):
    uni_items = np.unique(item_store_df.item_id)
    res_df = pd.DataFrame()
    beg_date_list = []
    qty_list = []
    item_id_list = []
    store_code_list = []
    for item_id in uni_items:
        print item_id
        for store_code in xrange(1,6):
            cur_item_df = item_store_df[(item_store_df.item_id == item_id) & (item_store_df.store_code == store_code)]
            end_date = 20151227
            beg_date = get_pre_date(end_date, 13)
            while beg_date >= 20141010:
                item_id_list.append(item_id)
                beg_date_list.append(beg_date)
                store_code_list.append(store_code)
                qty_df = cur_item_df[(cur_item_df.date >= beg_date) & (cur_item_df.date <= end_date)]

                #print qty_df
                qty_list.append(qty_df.qty_alipay_njhs.sum())
                end_date = get_pre_date(beg_date, 1)
                beg_date = get_pre_date(end_date, 13)

    res_df['item_id'] = item_id_list
    res_df['beg_date'] = beg_date_list
    res_df['store_code'] = store_code_list
    res_df['qty'] = qty_list

    return res_df
        
if __name__ == '__main__':
    item_df = pd.read_csv('data/sorted_item_feature.csv')
    res_df = gen_qty_two_week_item(item_df)
    res_df.to_csv('data/qty_item.csv', index=False)

    item_store_df = pd.read_csv('data/sorted_item_store_feature.csv')
    res_df = gen_qty_two_week_item_store(item_store_df)
    res_df.to_csv('data/qty_item_store.csv', index=False)

'''
print convert_int_to_date(20151227)
print convert_int_to_date(20160103)
print get_pre_two_week_date(20151227)
print get_pre_two_week_date(20160103)
print get_pre_date(20151227, 13)
'''
