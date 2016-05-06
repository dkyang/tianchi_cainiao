import pandas as pd

if __name__ == '__main__':

    week_2_item_df = pd.read_csv('data/2week_feature_item.csv')
    print week_2_item_df.shape
    columns = week_2_item_df.columns
    feat_cols = columns.tolist()
    #feat_cols.remove('qty_alipay_njhs')

    samples = week_2_item_df.loc[:,feat_cols]

    qty = week_2_item_df.qty_alipay_njhs 
    target = [qty[i] for i in xrange(0,len(qty)-1)]
    target = [0] + target
    
    '''
    samples['target'] = week_2_item_df.loc[:,'qty_alipay_njhs']
    print samples.target
    samples.loc[:samples.shape[0]-2, 'target'] = week_2_item_df.loc[1:,'qty_alipay_njhs']
    print samples.target
    '''
    samples['target'] = target
    #samples.to_csv('temp.csv', index=False)
    test_samples = samples[samples.beg_date == 20151214]
    valid_samples = samples[samples.beg_date == 20151130]
    # remove 0 zero qty(not on the shelves)
    train_samples = samples[(samples.beg_date != 20151214) & (samples.beg_date != 20151130) & (samples.target != 0.0)] 
    
    test_samples.to_csv('data/2week_test.csv', index=False)
    valid_samples.to_csv('data/2week_valid.csv', index=False)
    train_samples.to_csv('data/2week_train.csv', index=False)
    

