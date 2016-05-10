import pandas as pd
import numpy as np
import cPickle as pk

if __name__ == '__main__':
    conf_df = pd.read_csv('data/config1.csv')
    weights = []

    train = pd.read_csv("data/2week_train.csv")
    for i in xrange(train.shape[0]):
        row = train.iloc[i]
        a_b_value = conf_df[(int(row.item_id) == conf_df.item_id)].a_b
        a,b = a_b_value.iloc[0].split("_")
        weight = float(a)  + float(b)
        weights.append(weight)
    np.savetxt('data/sample_weight.txt',weights)       
