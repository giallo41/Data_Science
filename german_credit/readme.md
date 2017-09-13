German Credit Datasets analysis
============
Datasets Source : https://www.openml.org/d/31 

* Title: German Credit data

* Number of Instances: 1000

* Number of features: 20

* Target : Good / Bad (70%/30%) 

 : Base Accuracy rate should be above 70% (random choice)



—
1st Edition (09/13)

> Feature Selection from 

: DecisionTreeClassifier (1)

: RandomForestClassifier (2) and SelectFromModel 

> Selected Features 

![Selected Features](./images/features_0913.png) 

> Cross Validation Result 

{'criterion': 'gini', 'max_depth': 8, 'max_features': 1, 'n_estimators': 300} <br>
best cross score : 0.76125 <br>
test score : 0.72 <br>
