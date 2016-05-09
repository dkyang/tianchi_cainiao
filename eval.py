import pandas as pd
import numpy as np
import cPickle as pk
import sys


def evaluation(res_df):
    with open('data/conf.dict', 'r') as f:
        conf_dict = pk.load(f) 

    with open('data/cv_target_pre_2week_true.dict', 'r') as f:
        true_qty_dict = pk.load(f) 

    count_less = 0

    C_N = 0
    C_R = 0
    for i in xrange(res_df.shape[0]):
        row = res_df.iloc[i]
        key = '%s_%s' % (str(row.item_id), str(row.store_code))
        target = row.target

        a_b = conf_dict[key] 
        A, B = a_b.split('_')
        A = float(A)
        B = float(B)

        D = true_qty_dict[key] # true sales(validation)

        cost = A * max(D - target, 0) + B * max(target - D, 0)

        if cmp(row.store_code, 'all') == 0:
            C_N += cost
        else:
            continue
            C_R += cost
        
        if D > target:
            status = 'less'
            count_less += 1
        else:
            status = 'more'
        
        print 'cost:%f, (%f - %f) = %f, a_b = %s' % (cost, D, target, D-target, a_b)


    C = C_N + C_R
    print 'C_N = %f, C_R = %f, total cost = %f' % (C_N, C_R, C)

if __name__ == '__main__':
    res_file = sys.argv[1] 

    res_df = pd.read_csv(res_file)
    evaluation(res_df)
