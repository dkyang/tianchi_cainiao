import pandas as pd
import numpy as np

def compute_feature(data, i, col, v1_list, v2_list, v3_list, v4_list, d1_list, d2_list, d3_list):
    if i+3 >= data.shape[0]:
        return False

    v1 = data.iloc[i][col]
    v2 = data.iloc[i+1][col]
    v3 = data.iloc[i+2][col]
    v4 = data.iloc[i+3][col]

    d1 = v2 - v1
    d2 = v3 - v2
    d3 = v4 - v3

    v1_list.append(v1)
    v2_list.append(v2)
    v3_list.append(v3)
    v4_list.append(v4)

    d1_list.append(d1)
    d2_list.append(d2)
    d3_list.append(d3)
    
    return True

if __name__ == '__main__':

    week_2_item_df = pd.read_csv('data/2week_feature_item2.csv')
    columns = week_2_item_df.columns
    feat_cols = columns.tolist()

    samples = week_2_item_df.loc[:,feat_cols]

    qty = week_2_item_df.qty_alipay_njhs 
    target = [qty[i] for i in xrange(0,len(qty)-1)]
    target = [0] + target
    samples['target'] = target

    target_list = []    
    # feature engineering
    item_id_list = []
    cate_id_list = []
    cate_level_list = []
    brand_id_list = []
    supplier_id_list = []
    beg_date_list = []

    pv_ipv_1_list = []
    pv_ipv_2_list = []
    pv_ipv_3_list = []
    pv_ipv_4_list = []
    pv_ipv_d1_list = []
    pv_ipv_d2_list = []
    pv_ipv_d3_list = []

    pv_uv_1_list = []
    pv_uv_2_list = []
    pv_uv_3_list = []
    pv_uv_4_list = []
    pv_uv_d1_list = []
    pv_uv_d2_list = []
    pv_uv_d3_list = []

    cart_ipv_1_list = []
    cart_ipv_2_list = []
    cart_ipv_3_list = []
    cart_ipv_4_list = []
    cart_ipv_d1_list = []
    cart_ipv_d2_list = []
    cart_ipv_d3_list = []

    cart_uv_1_list = []
    cart_uv_2_list = []
    cart_uv_3_list = []
    cart_uv_4_list = []
    cart_uv_d1_list = []
    cart_uv_d2_list = []
    cart_uv_d3_list = []

    collect_uv_1_list = []
    collect_uv_2_list = []
    collect_uv_3_list = []
    collect_uv_4_list = []
    collect_uv_d1_list = []
    collect_uv_d2_list = []
    collect_uv_d3_list = []

    num_gmv_1_list = []
    num_gmv_2_list = []
    num_gmv_3_list = []
    num_gmv_4_list = []
    num_gmv_d1_list = []
    num_gmv_d2_list = []
    num_gmv_d3_list = []

    amt_gmv_1_list = []
    amt_gmv_2_list = []
    amt_gmv_3_list = []
    amt_gmv_4_list = []
    amt_gmv_d1_list = []
    amt_gmv_d2_list = []
    amt_gmv_d3_list = []

    qty_gmv_1_list = []
    qty_gmv_2_list = []
    qty_gmv_3_list = []
    qty_gmv_4_list = []
    qty_gmv_d1_list = []
    qty_gmv_d2_list = []
    qty_gmv_d3_list = []

    unum_gmv_1_list = []
    unum_gmv_2_list = []
    unum_gmv_3_list = []
    unum_gmv_4_list = []
    unum_gmv_d1_list = []
    unum_gmv_d2_list = []
    unum_gmv_d3_list = []

    amt_alipay_1_list = []
    amt_alipay_2_list = []
    amt_alipay_3_list = []
    amt_alipay_4_list = []
    amt_alipay_d1_list = []
    amt_alipay_d2_list = []
    amt_alipay_d3_list = []

    num_alipay_1_list = []
    num_alipay_2_list = []
    num_alipay_3_list = []
    num_alipay_4_list = []
    num_alipay_d1_list = []
    num_alipay_d2_list = []
    num_alipay_d3_list = []

    qty_alipay_1_list = []
    qty_alipay_2_list = []
    qty_alipay_3_list = []
    qty_alipay_4_list = []
    qty_alipay_d1_list = []
    qty_alipay_d2_list = []
    qty_alipay_d3_list = []

    unum_alipay_1_list = []
    unum_alipay_2_list = []
    unum_alipay_3_list = []
    unum_alipay_4_list = []
    unum_alipay_d1_list = []
    unum_alipay_d2_list = []
    unum_alipay_d3_list = []

    ztc_pv_ipv_1_list = []
    ztc_pv_ipv_2_list = []
    ztc_pv_ipv_3_list = []
    ztc_pv_ipv_4_list = []
    ztc_pv_ipv_d1_list = []
    ztc_pv_ipv_d2_list = []
    ztc_pv_ipv_d3_list = []

    tbk_pv_ipv_1_list = []
    tbk_pv_ipv_2_list = []
    tbk_pv_ipv_3_list = []
    tbk_pv_ipv_4_list = []
    tbk_pv_ipv_d1_list = []
    tbk_pv_ipv_d2_list = []
    tbk_pv_ipv_d3_list = []

    ss_pv_ipv_1_list = []
    ss_pv_ipv_2_list = []
    ss_pv_ipv_3_list = []
    ss_pv_ipv_4_list = []
    ss_pv_ipv_d1_list = []
    ss_pv_ipv_d2_list = []
    ss_pv_ipv_d3_list = []

    jhs_pv_ipv_1_list = []
    jhs_pv_ipv_2_list = []
    jhs_pv_ipv_3_list = []
    jhs_pv_ipv_4_list = []
    jhs_pv_ipv_d1_list = []
    jhs_pv_ipv_d2_list = []
    jhs_pv_ipv_d3_list = []

    ztc_pv_uv_1_list = []
    ztc_pv_uv_2_list = []
    ztc_pv_uv_3_list = []
    ztc_pv_uv_4_list = []
    ztc_pv_uv_d1_list = []
    ztc_pv_uv_d2_list = []
    ztc_pv_uv_d3_list = []

    tbk_pv_uv_1_list = []
    tbk_pv_uv_2_list = []
    tbk_pv_uv_3_list = []
    tbk_pv_uv_4_list = []
    tbk_pv_uv_d1_list = []
    tbk_pv_uv_d2_list = []
    tbk_pv_uv_d3_list = []

    ss_pv_uv_1_list = []
    ss_pv_uv_2_list = []
    ss_pv_uv_3_list = []
    ss_pv_uv_4_list = []
    ss_pv_uv_d1_list = []
    ss_pv_uv_d2_list = []
    ss_pv_uv_d3_list = []

    jhs_pv_uv_1_list = []
    jhs_pv_uv_2_list = []
    jhs_pv_uv_3_list = []
    jhs_pv_uv_4_list = []
    jhs_pv_uv_d1_list = []
    jhs_pv_uv_d2_list = []
    jhs_pv_uv_d3_list = []

    num_alipay_njhs_1_list = []
    num_alipay_njhs_2_list = []
    num_alipay_njhs_3_list = []
    num_alipay_njhs_4_list = []
    num_alipay_njhs_d1_list = []
    num_alipay_njhs_d2_list = []
    num_alipay_njhs_d3_list = []

    amt_alipay_njhs_1_list = []
    amt_alipay_njhs_2_list = []
    amt_alipay_njhs_3_list = []
    amt_alipay_njhs_4_list = []
    amt_alipay_njhs_d1_list = []
    amt_alipay_njhs_d2_list = []
    amt_alipay_njhs_d3_list = []

    qty_alipay_njhs_1_list = []
    qty_alipay_njhs_2_list = []
    qty_alipay_njhs_3_list = []
    qty_alipay_njhs_4_list = []
    qty_alipay_njhs_d1_list = []
    qty_alipay_njhs_d2_list = []
    qty_alipay_njhs_d3_list = []

    unum_alipay_njhs_1_list = []
    unum_alipay_njhs_2_list = []
    unum_alipay_njhs_3_list = []
    unum_alipay_njhs_4_list = []
    unum_alipay_njhs_d1_list = []
    unum_alipay_njhs_d2_list = []
    unum_alipay_njhs_d3_list = []

    uni_items = np.unique(samples.item_id) 
    for item_id in uni_items:
        print item_id
        cur_item_df = samples[samples.item_id == item_id]
        for i in xrange(cur_item_df.shape[0]):
            if i+3 >= cur_item_df.shape[0]:
                continue
 
            item_id_list.append(item_id)
            cate_id_list.append(cur_item_df.iloc[i]['cate_id'])
            cate_level_list.append(cur_item_df.iloc[i]['cate_level_id'])
            brand_id_list.append(cur_item_df.iloc[i]['brand_id'])
            supplier_id_list.append(cur_item_df.iloc[i]['supplier_id'])
            beg_date_list.append(cur_item_df.iloc[i]['beg_date'])
            target_list.append(cur_item_df.iloc[i]['target'])

            compute_feature(cur_item_df, i, 'pv_ipv', pv_ipv_1_list, pv_ipv_2_list, pv_ipv_3_list, pv_ipv_4_list, pv_ipv_d1_list, pv_ipv_d2_list, pv_ipv_d3_list)
            compute_feature(cur_item_df, i, 'pv_uv', pv_uv_1_list, pv_uv_2_list, pv_uv_3_list, pv_uv_4_list, pv_uv_d1_list, pv_uv_d2_list, pv_uv_d3_list)
            compute_feature(cur_item_df, i, 'cart_ipv', cart_ipv_1_list, cart_ipv_2_list, cart_ipv_3_list, cart_ipv_4_list, cart_ipv_d1_list, cart_ipv_d2_list, cart_ipv_d3_list)
            compute_feature(cur_item_df, i, 'cart_uv', cart_uv_1_list, cart_uv_2_list, cart_uv_3_list, cart_uv_4_list, cart_uv_d1_list, cart_uv_d2_list, cart_uv_d3_list)
            compute_feature(cur_item_df, i, 'collect_uv', collect_uv_1_list, collect_uv_2_list, collect_uv_3_list, collect_uv_4_list, collect_uv_d1_list, collect_uv_d2_list, collect_uv_d3_list)
            compute_feature(cur_item_df, i, 'num_gmv', num_gmv_1_list, num_gmv_2_list, num_gmv_3_list, num_gmv_4_list, num_gmv_d1_list, num_gmv_d2_list, num_gmv_d3_list)
            compute_feature(cur_item_df, i, 'amt_gmv', amt_gmv_1_list, amt_gmv_2_list, amt_gmv_3_list, amt_gmv_4_list, amt_gmv_d1_list, amt_gmv_d2_list, amt_gmv_d3_list)
            compute_feature(cur_item_df, i, 'qty_gmv', qty_gmv_1_list, qty_gmv_2_list, qty_gmv_3_list, qty_gmv_4_list, qty_gmv_d1_list, qty_gmv_d2_list, qty_gmv_d3_list)
            compute_feature(cur_item_df, i, 'unum_gmv', unum_gmv_1_list, unum_gmv_2_list, unum_gmv_3_list, unum_gmv_4_list, unum_gmv_d1_list, unum_gmv_d2_list, unum_gmv_d3_list)
            compute_feature(cur_item_df, i, 'amt_alipay', amt_alipay_1_list, amt_alipay_2_list, amt_alipay_3_list, amt_alipay_4_list, amt_alipay_d1_list, amt_alipay_d2_list, amt_alipay_d3_list)
            compute_feature(cur_item_df, i, 'num_alipay', num_alipay_1_list, num_alipay_2_list, num_alipay_3_list, num_alipay_4_list, num_alipay_d1_list, num_alipay_d2_list, num_alipay_d3_list)
            compute_feature(cur_item_df, i, 'qty_alipay', qty_alipay_1_list, qty_alipay_2_list, qty_alipay_3_list, qty_alipay_4_list, qty_alipay_d1_list, qty_alipay_d2_list, qty_alipay_d3_list)
            compute_feature(cur_item_df, i, 'unum_alipay', unum_alipay_1_list, unum_alipay_2_list, unum_alipay_3_list, unum_alipay_4_list, unum_alipay_d1_list, unum_alipay_d2_list, unum_alipay_d3_list)
            compute_feature(cur_item_df, i, 'ztc_pv_ipv', ztc_pv_ipv_1_list, ztc_pv_ipv_2_list, ztc_pv_ipv_3_list, ztc_pv_ipv_4_list, ztc_pv_ipv_d1_list, ztc_pv_ipv_d2_list, ztc_pv_ipv_d3_list)
            compute_feature(cur_item_df, i, 'tbk_pv_ipv', tbk_pv_ipv_1_list, tbk_pv_ipv_2_list, tbk_pv_ipv_3_list, tbk_pv_ipv_4_list, tbk_pv_ipv_d1_list, tbk_pv_ipv_d2_list, tbk_pv_ipv_d3_list)
            compute_feature(cur_item_df, i, 'ss_pv_ipv', ss_pv_ipv_1_list, ss_pv_ipv_2_list, ss_pv_ipv_3_list, ss_pv_ipv_4_list, ss_pv_ipv_d1_list, ss_pv_ipv_d2_list, ss_pv_ipv_d3_list)
            compute_feature(cur_item_df, i, 'jhs_pv_ipv', jhs_pv_ipv_1_list, jhs_pv_ipv_2_list, jhs_pv_ipv_3_list, jhs_pv_ipv_4_list, jhs_pv_ipv_d1_list, jhs_pv_ipv_d2_list, jhs_pv_ipv_d3_list)
            compute_feature(cur_item_df, i, 'ztc_pv_uv', ztc_pv_uv_1_list, ztc_pv_uv_2_list, ztc_pv_uv_3_list, ztc_pv_uv_4_list, ztc_pv_uv_d1_list, ztc_pv_uv_d2_list, ztc_pv_uv_d3_list)
            compute_feature(cur_item_df, i, 'tbk_pv_uv', tbk_pv_uv_1_list, tbk_pv_uv_2_list, tbk_pv_uv_3_list, tbk_pv_uv_4_list, tbk_pv_uv_d1_list, tbk_pv_uv_d2_list, tbk_pv_uv_d3_list)
            compute_feature(cur_item_df, i, 'ss_pv_uv', ss_pv_uv_1_list, ss_pv_uv_2_list, ss_pv_uv_3_list, ss_pv_uv_4_list, ss_pv_uv_d1_list, ss_pv_uv_d2_list, ss_pv_uv_d3_list)
            compute_feature(cur_item_df, i, 'jhs_pv_uv', jhs_pv_uv_1_list, jhs_pv_uv_2_list, jhs_pv_uv_3_list, jhs_pv_uv_4_list, jhs_pv_uv_d1_list, jhs_pv_uv_d2_list, jhs_pv_uv_d3_list)
            compute_feature(cur_item_df, i, 'num_alipay_njhs', num_alipay_njhs_1_list, num_alipay_njhs_2_list, num_alipay_njhs_3_list, num_alipay_njhs_4_list, num_alipay_njhs_d1_list, num_alipay_njhs_d2_list, num_alipay_njhs_d3_list)
            compute_feature(cur_item_df, i, 'amt_alipay_njhs', amt_alipay_njhs_1_list, amt_alipay_njhs_2_list, amt_alipay_njhs_3_list, amt_alipay_njhs_4_list, amt_alipay_njhs_d1_list, amt_alipay_njhs_d2_list, amt_alipay_njhs_d3_list)
            compute_feature(cur_item_df, i, 'qty_alipay_njhs', qty_alipay_njhs_1_list, qty_alipay_njhs_2_list, qty_alipay_njhs_3_list, qty_alipay_njhs_4_list, qty_alipay_njhs_d1_list, qty_alipay_njhs_d2_list, qty_alipay_njhs_d3_list)
            compute_feature(cur_item_df, i, 'unum_alipay_njhs', unum_alipay_njhs_1_list, unum_alipay_njhs_2_list, unum_alipay_njhs_3_list, unum_alipay_njhs_4_list, unum_alipay_njhs_d1_list, unum_alipay_njhs_d2_list, unum_alipay_njhs_d3_list)
                
    samples = pd.DataFrame()

    samples['item_id'] = item_id_list
    samples['cate_id'] = cate_id_list
    samples['cate_level'] = cate_level_list
    samples['brand_id'] = brand_id_list
    samples['supplier_id'] = supplier_id_list
    samples['beg_date'] = beg_date_list

    samples['pv_ipv_1'] = pv_ipv_1_list
    samples['pv_ipv_2'] = pv_ipv_2_list
    samples['pv_ipv_3'] = pv_ipv_3_list
    samples['pv_ipv_4'] = pv_ipv_4_list
    samples['pv_ipv_d1'] = pv_ipv_d1_list
    samples['pv_ipv_d2'] = pv_ipv_d2_list
    samples['pv_ipv_d3'] = pv_ipv_d3_list

    samples['pv_uv_1'] = pv_uv_1_list
    samples['pv_uv_2'] = pv_uv_2_list
    samples['pv_uv_3'] = pv_uv_3_list
    samples['pv_uv_4'] = pv_uv_4_list
    samples['pv_uv_d1'] = pv_uv_d1_list
    samples['pv_uv_d2'] = pv_uv_d2_list
    samples['pv_uv_d3'] = pv_uv_d3_list

    samples['cart_ipv_1'] = cart_ipv_1_list
    samples['cart_ipv_2'] = cart_ipv_2_list
    samples['cart_ipv_3'] = cart_ipv_3_list
    samples['cart_ipv_4'] = cart_ipv_4_list
    samples['cart_ipv_d1'] = cart_ipv_d1_list
    samples['cart_ipv_d2'] = cart_ipv_d2_list
    samples['cart_ipv_d3'] = cart_ipv_d3_list

    samples['cart_uv_1'] = cart_uv_1_list
    samples['cart_uv_2'] = cart_uv_2_list
    samples['cart_uv_3'] = cart_uv_3_list
    samples['cart_uv_4'] = cart_uv_4_list
    samples['cart_uv_d1'] = cart_uv_d1_list
    samples['cart_uv_d2'] = cart_uv_d2_list
    samples['cart_uv_d3'] = cart_uv_d3_list

    samples['collect_uv_1'] = collect_uv_1_list
    samples['collect_uv_2'] = collect_uv_2_list
    samples['collect_uv_3'] = collect_uv_3_list
    samples['collect_uv_4'] = collect_uv_4_list
    samples['collect_uv_d1'] = collect_uv_d1_list
    samples['collect_uv_d2'] = collect_uv_d2_list
    samples['collect_uv_d3'] = collect_uv_d3_list

    samples['num_gmv_1'] = num_gmv_1_list
    samples['num_gmv_2'] = num_gmv_2_list
    samples['num_gmv_3'] = num_gmv_3_list
    samples['num_gmv_4'] = num_gmv_4_list
    samples['num_gmv_d1'] = num_gmv_d1_list
    samples['num_gmv_d2'] = num_gmv_d2_list
    samples['num_gmv_d3'] = num_gmv_d3_list

    samples['amt_gmv_1'] = amt_gmv_1_list
    samples['amt_gmv_2'] = amt_gmv_2_list
    samples['amt_gmv_3'] = amt_gmv_3_list
    samples['amt_gmv_4'] = amt_gmv_4_list
    samples['amt_gmv_d1'] = amt_gmv_d1_list
    samples['amt_gmv_d2'] = amt_gmv_d2_list
    samples['amt_gmv_d3'] = amt_gmv_d3_list

    samples['qty_gmv_1'] = qty_gmv_1_list
    samples['qty_gmv_2'] = qty_gmv_2_list
    samples['qty_gmv_3'] = qty_gmv_3_list
    samples['qty_gmv_4'] = qty_gmv_4_list
    samples['qty_gmv_d1'] = qty_gmv_d1_list
    samples['qty_gmv_d2'] = qty_gmv_d2_list
    samples['qty_gmv_d3'] = qty_gmv_d3_list

    samples['unum_gmv_1'] = unum_gmv_1_list
    samples['unum_gmv_2'] = unum_gmv_2_list
    samples['unum_gmv_3'] = unum_gmv_3_list
    samples['unum_gmv_4'] = unum_gmv_4_list
    samples['unum_gmv_d1'] = unum_gmv_d1_list
    samples['unum_gmv_d2'] = unum_gmv_d2_list
    samples['unum_gmv_d3'] = unum_gmv_d3_list

    samples['amt_alipay_1'] = amt_alipay_1_list
    samples['amt_alipay_2'] = amt_alipay_2_list
    samples['amt_alipay_3'] = amt_alipay_3_list
    samples['amt_alipay_4'] = amt_alipay_4_list
    samples['amt_alipay_d1'] = amt_alipay_d1_list
    samples['amt_alipay_d2'] = amt_alipay_d2_list
    samples['amt_alipay_d3'] = amt_alipay_d3_list

    samples['num_alipay_1'] = num_alipay_1_list
    samples['num_alipay_2'] = num_alipay_2_list
    samples['num_alipay_3'] = num_alipay_3_list
    samples['num_alipay_4'] = num_alipay_4_list
    samples['num_alipay_d1'] = num_alipay_d1_list
    samples['num_alipay_d2'] = num_alipay_d2_list
    samples['num_alipay_d3'] = num_alipay_d3_list

    samples['qty_alipay_1'] = qty_alipay_1_list
    samples['qty_alipay_2'] = qty_alipay_2_list
    samples['qty_alipay_3'] = qty_alipay_3_list
    samples['qty_alipay_4'] = qty_alipay_4_list
    samples['qty_alipay_d1'] = qty_alipay_d1_list
    samples['qty_alipay_d2'] = qty_alipay_d2_list
    samples['qty_alipay_d3'] = qty_alipay_d3_list

    samples['unum_alipay_1'] = unum_alipay_1_list
    samples['unum_alipay_2'] = unum_alipay_2_list
    samples['unum_alipay_3'] = unum_alipay_3_list
    samples['unum_alipay_4'] = unum_alipay_4_list
    samples['unum_alipay_d1'] = unum_alipay_d1_list
    samples['unum_alipay_d2'] = unum_alipay_d2_list
    samples['unum_alipay_d3'] = unum_alipay_d3_list

    samples['ztc_pv_ipv_1'] = ztc_pv_ipv_1_list
    samples['ztc_pv_ipv_2'] = ztc_pv_ipv_2_list
    samples['ztc_pv_ipv_3'] = ztc_pv_ipv_3_list
    samples['ztc_pv_ipv_4'] = ztc_pv_ipv_4_list
    samples['ztc_pv_ipv_d1'] = ztc_pv_ipv_d1_list
    samples['ztc_pv_ipv_d2'] = ztc_pv_ipv_d2_list
    samples['ztc_pv_ipv_d3'] = ztc_pv_ipv_d3_list

    samples['tbk_pv_ipv_1'] = tbk_pv_ipv_1_list
    samples['tbk_pv_ipv_2'] = tbk_pv_ipv_2_list
    samples['tbk_pv_ipv_3'] = tbk_pv_ipv_3_list
    samples['tbk_pv_ipv_4'] = tbk_pv_ipv_4_list
    samples['tbk_pv_ipv_d1'] = tbk_pv_ipv_d1_list
    samples['tbk_pv_ipv_d2'] = tbk_pv_ipv_d2_list
    samples['tbk_pv_ipv_d3'] = tbk_pv_ipv_d3_list

    samples['ss_pv_ipv_1'] = ss_pv_ipv_1_list
    samples['ss_pv_ipv_2'] = ss_pv_ipv_2_list
    samples['ss_pv_ipv_3'] = ss_pv_ipv_3_list
    samples['ss_pv_ipv_4'] = ss_pv_ipv_4_list
    samples['ss_pv_ipv_d1'] = ss_pv_ipv_d1_list
    samples['ss_pv_ipv_d2'] = ss_pv_ipv_d2_list
    samples['ss_pv_ipv_d3'] = ss_pv_ipv_d3_list

    samples['jhs_pv_ipv_1'] = jhs_pv_ipv_1_list
    samples['jhs_pv_ipv_2'] = jhs_pv_ipv_2_list
    samples['jhs_pv_ipv_3'] = jhs_pv_ipv_3_list
    samples['jhs_pv_ipv_4'] = jhs_pv_ipv_4_list
    samples['jhs_pv_ipv_d1'] = jhs_pv_ipv_d1_list
    samples['jhs_pv_ipv_d2'] = jhs_pv_ipv_d2_list
    samples['jhs_pv_ipv_d3'] = jhs_pv_ipv_d3_list

    samples['num_alipay_njhs_1'] = num_alipay_njhs_1_list
    samples['num_alipay_njhs_2'] = num_alipay_njhs_2_list
    samples['num_alipay_njhs_3'] = num_alipay_njhs_3_list
    samples['num_alipay_njhs_4'] = num_alipay_njhs_4_list
    samples['num_alipay_njhs_d1'] = num_alipay_njhs_d1_list
    samples['num_alipay_njhs_d2'] = num_alipay_njhs_d2_list
    samples['num_alipay_njhs_d3'] = num_alipay_njhs_d3_list

    samples['qty_alipay_njhs_1'] = qty_alipay_njhs_1_list
    samples['qty_alipay_njhs_2'] = qty_alipay_njhs_2_list
    samples['qty_alipay_njhs_3'] = qty_alipay_njhs_3_list
    samples['qty_alipay_njhs_4'] = qty_alipay_njhs_4_list
    samples['qty_alipay_njhs_d1'] = qty_alipay_njhs_d1_list
    samples['qty_alipay_njhs_d2'] = qty_alipay_njhs_d2_list
    samples['qty_alipay_njhs_d3'] = qty_alipay_njhs_d3_list

    samples['unum_alipay_njhs_1'] = unum_alipay_njhs_1_list
    samples['unum_alipay_njhs_2'] = unum_alipay_njhs_2_list
    samples['unum_alipay_njhs_3'] = unum_alipay_njhs_3_list
    samples['unum_alipay_njhs_4'] = unum_alipay_njhs_4_list
    samples['unum_alipay_njhs_d1'] = unum_alipay_njhs_d1_list
    samples['unum_alipay_njhs_d2'] = unum_alipay_njhs_d2_list
    samples['unum_alipay_njhs_d3'] = unum_alipay_njhs_d3_list

    samples['target'] = target_list

    test_samples = samples[samples.beg_date == 20151214]
    valid_samples = samples[samples.beg_date == 20151130]
    # remove 0 zero qty(not on the shelves)
    train_samples = samples[(samples.beg_date != 20151214) & (samples.beg_date != 20151130) & (samples.target != 0.0)] 
    
    test_samples.to_csv('data/2week_feature_test2.csv', index=False)
    valid_samples.to_csv('data/2week_feature_valid2.csv', index=False)
    train_samples.to_csv('data/2week_feature_train2.csv', index=False)
    

