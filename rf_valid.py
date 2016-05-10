import pandas as pd
import numpy as np
import xgboost as xgb
import random
from sklearn.ensemble import RandomForestRegressor

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
    params["subsample"] = 1 
    params["colsample_bytree"] = 1
    params["silent"] = 1
    params["max_depth"] = 5 
    plst = list(params.items())
    return plst


xgb_num_rounds = 200 

train = pd.read_csv("data/2week_train.csv") # the train dataset is now a Pandas DataFrame
valid = pd.read_csv("data/2week_valid.csv") # the train dataset is now a Pandas DataFrame
test = pd.read_csv("data/2week_test.csv") # the train dataset is now a Pandas DataFrame

#train_columns_to_drop = ['target', 'num_alipay_njhs']
#valid_columns_to_drop = ['num_alipay_njhs']
#train_columns_to_drop = ['beg_date', 'target']
#valid_columns_to_drop = ['beg_date', 'target']
#test_columns_to_drop = ['beg_date', 'target']

train_columns_to_drop = ['target']
valid_columns_to_drop = ['target']
test_columns_to_drop = ['target']
valid_target = valid.target


train_feat = train.drop(train_columns_to_drop, axis=1)
valid_feat = valid.drop(valid_columns_to_drop, axis=1)
test_feat = test.drop(test_columns_to_drop, axis=1)


xgtrain = xgb.DMatrix(train_feat, train.target.values)
xgvalid = xgb.DMatrix(valid_feat, valid_target.values)
xgtest = xgb.DMatrix(test_feat)

plst = get_params()
print(plst)
clf = RandomForestRegressor(n_estimators=1000, n_jobs=-1)
clf = clf.fit(train_feat, train['target'].values)
feat_imp = clf.feature_importances_
feat_imp = np.array(feat_imp)
print feat_imp

test_preds = clf.predict(test_feat)
preds_out = pd.DataFrame({"item_id": test['item_id'].values, "qty": test_preds})
preds_out = preds_out.set_index('item_id')
preds_out.to_csv('data/rf_qty_1.csv')

valid_preds = clf.predict(valid_feat)
store_code_list = ["all" for i in xrange(valid.shape[0])]
preds_out = pd.DataFrame({"item_id": valid['item_id'].values, "store_code": store_code_list, "target": valid_preds})
preds_out = preds_out.set_index('item_id')
preds_out.to_csv('data/rf_qty_valid_1.csv')


'''
model = xgb.train(params = plst, 
				dtrain = xgtrain, 
                evals = watchlist,
				num_boost_round = xgb_num_rounds)

# feature importance 
importance = model.get_fscore()
tuples = [(k, importance[k]) for k in importance]
tuples = sorted(tuples, key=lambda x: -x[1])
for k,v in tuples:
    print '%s\t%d' % (k,v)

#xgb.plot_importance(model)
valid_preds = model.predict(xgvalid, ntree_limit=model.best_iteration)
test_preds = model.predict(xgtest, ntree_limit=model.best_iteration)


preds_out = pd.DataFrame({"item_id": test['item_id'].values, "qty": test_preds})
preds_out = preds_out.set_index('item_id')
preds_out.to_csv('data/xgb_qty_1.csv')

store_code_list = ["all" for i in xrange(valid.shape[0])]
preds_out = pd.DataFrame({"item_id": valid['item_id'].values, "store_code": store_code_list, "target": valid_preds})
preds_out = preds_out.set_index('item_id')
preds_out.to_csv('data/xgb_qty_valid_1.csv')
print 'finish'
'''
