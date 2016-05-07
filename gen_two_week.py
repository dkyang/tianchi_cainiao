import pandas as pd
import numpy as np
import datetime
from util import convert_int_to_date, convert_date_to_int, get_pre_date   


def gen_qty_two_week_item(item_df):
    uni_items = np.unique(item_df.item_id)
    res_df = pd.DataFrame()
    beg_date_list = []
    #qty_list = []
    item_id_list = []
    num_list = []
    id_list = []
    for item_id in uni_items:
        print item_id
        cur_item_df = item_df[item_df.item_id == item_id]
        end_date = 20151227
        beg_date = get_pre_date(end_date, 13)
        while beg_date >= 20141010:
            item_id_list.append(item_id)
            id_list.append(cur_item_df.loc[:,['item_id','cate_id','cate_level_id','brand_id','supplier_id']].iloc[0])
            beg_date_list.append(beg_date)
            qty_df = cur_item_df[(cur_item_df.date >= beg_date) & (cur_item_df.date <= end_date)]

            #print qty_df
            num_df = qty_df.loc[:, ['pv_ipv','pv_uv','cart_ipv','cart_uv','collect_uv','num_gmv','amt_gmv','qty_gmv','unum_gmv','amt_alipay','num_alipay','qty_alipay','unum_alipay','ztc_pv_ipv','tbk_pv_ipv','ss_pv_ipv','jhs_pv_ipv','ztc_pv_uv','tbk_pv_uv','ss_pv_uv','jhs_pv_uv','num_alipay_njhs','amt_alipay_njhs','qty_alipay_njhs','unum_alipay_njhs']]
            num_list.append(num_df.sum())
           # qty_list.append(qty_df.qty_alipay_njhs.sum())
            end_date = get_pre_date(beg_date, 1)
            beg_date = get_pre_date(end_date, 13)

    id_df = pd.DataFrame(id_list)
    id_df['beg_date'] = beg_date_list
    num_df = pd.DataFrame(num_list)
    num_df['item_id'] = item_id_list
    num_df['beg_date'] = beg_date_list
    res_df = pd.merge(id_df, num_df, on = ['item_id','beg_date'])
    #res_df['qty'] = qty_list
    #res_df['item_id'] = item_id_list
    #res_df['beg_date'] = beg_date_list

    return res_df
            
def gen_qty_two_week_item_store(item_store_df):
    uni_items = np.unique(item_store_df.item_id)
    res_df = pd.DataFrame()
    beg_date_list = []
    qty_list = []
    item_id_list = []
    store_code_list = []
    num_list = []
    id_list = []
    for item_id in uni_items:
        print item_id
        for store_code in xrange(1,6):
            cur_item_df = item_store_df[(item_store_df.item_id == item_id) & (item_store_df.store_code == store_code)]
            print cur_item_df.shape
            if cur_item_df.shape[0] == 0:
                continue
            end_date = 20151227
            beg_date = get_pre_date(end_date, 13)
            while beg_date >= 20141010:
                qty_df = cur_item_df[(cur_item_df.date >= beg_date) & (cur_item_df.date <= end_date)]

                if qty_df.shape[0] != 0:
                    item_id_list.append(item_id)
                    beg_date_list.append(beg_date)
                    id_list.append(cur_item_df.loc[:,['item_id','store_code','cate_id','cate_level_id','brand_id','supplier_id']].iloc[0])
                    num_df = qty_df.loc[:, ['pv_ipv','pv_uv','cart_ipv','cart_uv','collect_uv','num_gmv','amt_gmv','qty_gmv','unum_gmv','amt_alipay','num_alipay','qty_alipay','unum_alipay','ztc_pv_ipv','tbk_pv_ipv','ss_pv_ipv','jhs_pv_ipv','ztc_pv_uv','tbk_pv_uv','ss_pv_uv','jhs_pv_uv','num_alipay_njhs','amt_alipay_njhs','qty_alipay_njhs','unum_alipay_njhs']]
                    num_list.append(num_df.sum())

                end_date = get_pre_date(beg_date, 1)
                beg_date = get_pre_date(end_date, 13)

    id_df = pd.DataFrame(id_list)
    id_df['beg_date'] = beg_date_list
    num_df = pd.DataFrame(num_list)
    num_df['item_id'] = item_id_list
    num_df['beg_date'] = beg_date_list
    res_df = pd.merge(id_df, num_df, on = ['item_id','beg_date'])

    return res_df
        
if __name__ == '__main__':
    
    '''
    item_df = pd.read_csv('data/item_feature1.csv')
    res_df = gen_qty_two_week_item(item_df)
    res_df.to_csv('data/2week_feature_item.csv', index=False)
    '''
    
    item_store_df = pd.read_csv('data/item_store_feature1.csv')
    res_df = gen_qty_two_week_item_store(item_store_df)
    res_df.to_csv('data/2week_feature_item_store.csv', index=False)

'''
print convert_int_to_date(20151227)
print convert_int_to_date(20160103)
print get_pre_two_week_date(20151227)
print get_pre_two_week_date(20160103)
print get_pre_date(20151227, 13)
'''
