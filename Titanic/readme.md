

This is for <b>Titanic Survive Machine Learning</b> Test 

<b>Overview</b>

The data can be assecible from the https://www.kaggle.com/c/titanic site 
( You may require to login ) 

training set (train.csv)
test set (test.csv)
test truth (gender_submission.csv)

<b>Data Dictionary</b> <br>

*Variable	Definition	Key <br>
*survival	Survival	0 = No, 1 = Yes <br>
*pclass	Ticket class	1 = 1st, 2 = 2nd, 3 = 3rd <br>
*sex	Sex	<br>
*Age	Age in years	<br>
*sibsp	# of siblings / spouses aboard the Titanic	<br>
*parch	# of parents / children aboard the Titanic	<br>
*ticket	Ticket number	<br>
*fare	Passenger fare	<br>
*cabin	Cabin number	<br>
*embarked	 [ Port of Embarkation	C = Cherbourg, Q = Queenstown, S = Southampton ] <br>

Pre-processed data from the reference <br>

https://triangleinequality.wordpress.com/2013/09/08/basic-feature-engineering-with-the-titanic-data/

<b>Serveral Key Processing</b> <br>

Applied Blank Fare to same class and sex because there are some differences between Male / Female 
<br>
<br>

-------------------------------------------------<br>
Pclass  Embarked  Sex     Fare <br>
1       C         female    118.895949 <br>
                  male       94.622560 <br>
        Q         female     90.000000 <br>
                  male       90.000000 <br>
        S         female    101.069145 <br>
                  male       53.670756 <br>
2       C         female     27.003791 <br>
                  male       20.904406 <br>
        Q         female     12.350000 <br>
                  male       11.489160 <br>
        S         female     23.023118 <br>
                  male       20.073322 <br>
3       C         female     13.834545 <br>
                  male        9.775901 <br>
        Q         female      9.791968 <br>
                  male       10.979167 <br>
        S         female     18.083851 <br>
                  male       13.145977 <br>
Name: Fare, dtype: float64 <br>
------------------------------------------------- <br>




<b> Feature in Use </b>

train_col_name=[ 'Age', 'Fare', 'Parch', 'Pclass', 'SibSp', 'nCabin_deck', 'nTitle', 'nSex']<br>
+ Age = numeric <br>
+ Fare = numeric <br>
+ Parch = numeric <br>
+ Pclass = numeric <br>
+ Sibsp = numeric <br>
+ nCabin_deck = Category<br>
+ nTitle = Category<br>
+ nSex = Category<br><br>

originally (nEmbark', 'Cabin_count') featured <br>
but after examining the feature_importaces_ (very small or zero ) <br>

Using Sklearn Library <br><br>

#### Random Forest Classifier ####<br>
--- Est Value is : 14.000<br>
Train Score : 97.419%<br>
Test Score : 83.254%<br>

#### SVM kernel Classifier ####<br>
--- C Value is : 100.000 Gamma value is : 0.200<br>
Train Score : 88.440%<br>
Test Score : 87.321%<br>

#### MLP Classifier ####<br>
----- Layer :  [30, 10]<br>
Train Score : 90.797%<br>
Test Score : 85.167%<br>

<b>Please recommend additional way to improve !! </b>




