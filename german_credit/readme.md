German Credit Datasets analysis
============
Datasets Source : https://www.openml.org/d/31 

* Title: German Credit data

* Number of Instances: 1000

* Number of features: 20

* Target : Good / Bad (70%/30%) 

 : Base Accuracy rate should be above 70% (random choice)
<br>
<br>



—
2nd Edition (09/17)
-------------

> Feture Engineering 
=> Set Small size sample of features -> consolidate & resizing 


> Selected Feature 

![Selected Features](./image/feature_0917.png) 

> Cross Validation Result<br>
using RandomForest Classifier 

{'criterion': 'gini', 'max_depth': 7, 'max_features': 3, 'n_estimators': 100}<br>
best cross score : 0.765<br>
test score : 0.755<br>
Much reduced variance (train & test score)<br>
but still has a lot of room to improve "Bias"<br>
<br>

> Confustion Matrix <br>
[157,  83], <br>
[  5, 555]  <br>

FN - 5, FP - 83 <br> 
one of the sample data that recoginize the FP is <br><br>

index 331 - FP <Br>
index 324 - PP <br>
 
<br>
2 sample's are same feature after feature engineering expect Credit Amount and Age <br>

original featrue <br>
331 - purpose : 'education', 	savings_statu : '100<=X<500' <br>
324 - purpose : 'new car', 	savings_statu : 'X<100' <br>





<Br><br><br>

—
1st Edition (09/13)
-------------

> Feature Selection from 

: DecisionTreeClassifier (1)

: RandomForestClassifier (2) and SelectFromModel 

> Selected Features 

![Selected Features](./image/features_0913.png) 

> Cross Validation Result 

{'criterion': 'gini', 'max_depth': 8, 'max_features': 1, 'n_estimators': 300} <br>
best cross score : 0.76125 <br>
test score : 0.72 <br>


