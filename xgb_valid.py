import pandas as pd
import numpy as np
import xgboost as xgb
import random

#Some parameters to play with
rnd=1234
random.seed(rnd)



def get_params():
    params = {}
    params["objective"] = "reg:linear"
    params["booster"] = "gbtree"
    params["eta"] = 0.1
    params["min_child_weight"] = 1
    #params["eval_meric"] = 'auc'
    params["subsample"] = 0.6815
    params["colsample_bytree"] = 0.701
    params["silent"] = 0
    params["max_depth"] = 3 
    plst = list(params.items())
    return plst


xgb_num_rounds = 50 

train = pd.read_csv("data/2week_train.csv") # the train dataset is now a Pandas DataFrame
valid = pd.read_csv("data/2week_valid.csv") # the train dataset is now a Pandas DataFrame

train_columns_to_drop = ['beg_date', 'target']
valid_columns_to_drop = ['beg_date', 'target']
#train_columns_to_drop = ['target', 'num_alipay_njhs']
#valid_columns_to_drop = ['num_alipay_njhs']
valid_target = valid.target


train_feat = train.drop(train_columns_to_drop, axis=1)
valid_feat = valid.drop(valid_columns_to_drop, axis=1)
print train_feat


xgtrain = xgb.DMatrix(train_feat, train.target.values)
xgvalid = xgb.DMatrix(valid_feat)

plst = get_params()
print(plst)
watchlist = [(xgtrain, 'train')]
model = xgb.train(params = plst, 
				dtrain = xgtrain, 
				num_boost_round = xgb_num_rounds)

# feature importance 
importance = model.get_fscore()
tuples = [(k, importance[k]) for k in importance]
tuples = sorted(tuples, key=lambda x: -x[1])
for k,v in tuples:
    print '%s\t%d' % (k,v)

#xgb.plot_importance(model)
test_preds = model.predict(xgvalid, ntree_limit=model.best_iteration)


preds_out = pd.DataFrame({"item_id": valid['item_id'].values, "target": test_preds, "true_target": valid_target})
preds_out = preds_out.set_index('item_id')
preds_out.to_csv('xgb_valid_baseline_n_begdate_1.csv')
print 'finish'
