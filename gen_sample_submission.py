import pandas as pd
import numpy as np

'''
data = pd.read_csv('data/item_feature2.csv')
uni_items = np.unique(data.item_id)
print len(uni_items)
'''

data = pd.read_csv('data/config2.csv')
print data

data = data.drop(['a_b'], axis=1)
data['target'] = [1 for i in xrange(data.shape[0])]

data.to_csv('data/sample_submission2.csv', index=False)
