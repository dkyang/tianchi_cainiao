import pandas as pd
import cPickle as pk

if __name__ == '__main__':
    conf_df = pd.read_csv('data/config1.csv')
    conf_dict = {}
    for i in xrange(conf_df.shape[0]):
        row = conf_df.iloc[i] 
        key = '%s_%s' % (str(row.item_id), str(row.store_code))
        conf_dict[key] = row.a_b

    with open('data/conf.dict', 'w') as f:
        pk.dump(conf_dict, f)

    true_df = pd.read_csv('data/pre_2week_true_qty.csv')
    cv_qty_dict = {}
    for i in xrange(true_df.shape[0]):
        row = true_df.iloc[i] 
        key = '%s_%s' % (str(row.item_id), str(row.store_code))
        cv_qty_dict[key] = row.target

    with open('data/cv_target_pre_2week_true.dict', 'w') as f:
        pk.dump(cv_qty_dict, f)
