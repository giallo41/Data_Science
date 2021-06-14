import time
from sklearn.ensemble import RandomForestClassifier


def rfc_fit(X, y, param=None):

    rf_clf = RandomForestClassifier(max_depth = 6, 
                               max_features = 5,
                               n_estimators = 100,
                               criterion = 'gini')
    start_tm = time.time()
    rf_clf.fit(X, y)
    print ("Fitting time : {}".format(time.time() - start_tm))
    return rf_clf