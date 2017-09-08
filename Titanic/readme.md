

This is for <b>Titanic Survive Machine Learning</b> Test 

<b>Overview</b>

The data can be assecible from the https://www.kaggle.com/c/titanic site 
( You may require to login ) 

training set (train.csv)
test set (test.csv)
test truth (gender_submission.csv)

<b>Data Dictionary</b>

Variable	Definition	Key
survival	Survival	0 = No, 1 = Yes
pclass	Ticket class	1 = 1st, 2 = 2nd, 3 = 3rd
sex	Sex	
Age	Age in years	
sibsp	# of siblings / spouses aboard the Titanic	
parch	# of parents / children aboard the Titanic	
ticket	Ticket number	
fare	Passenger fare	
cabin	Cabin number	
embarked	 [ Port of Embarkation	C = Cherbourg, Q = Queenstown, S = Southampton ] 

Pre-processed data from the reference 

https://triangleinequality.wordpress.com/2013/09/08/basic-feature-engineering-with-the-titanic-data/

Serveral Key Processing is 

Applied Blank Fare to same class and sex because there are some differences between Male / Female 


-------------------------------------------------
Pclass  Embarked  Sex       Fare
1       C         female    118.895949
                  male       94.622560
        Q         female     90.000000
                  male       90.000000
        S         female    101.069145
                  male       53.670756
2       C         female     27.003791
                  male       20.904406
        Q         female     12.350000
                  male       11.489160
        S         female     23.023118
                  male       20.073322
3       C         female     13.834545
                  male        9.775901
        Q         female      9.791968
                  male       10.979167
        S         female     18.083851
                  male       13.145977
Name: Fare, dtype: float64
-------------------------------------------------


<b>Feature in Use</b>
train_col_name = [ 'Age', 'Fare', 'Parch', 'Pclass', 'SibSp', 'nCabin_deck', 'nTitle', 'nSex']
Age = numeric 
Fare = numeric 
Parch = numeric 
Pclass = numeric
Sibsp = numeric 
nCabin_deck = Category
nTitle = Category
nSex = Category

originally (nEmbark', 'Cabin_count') featured 
but after examining the feature_importaces_ (very small or zero ) 

Using Sklearn Library 

#### Random Forest Classifier ####
--- Est Value is : 14.000
Train Score : 97.419%
Test Score : 83.254%

#### SVM kernel Classifier ####
--- C Value is : 100.000 Gamma value is : 0.200
Train Score : 88.440%
Test Score : 87.321%

#### MLP Classifier ####
----- Layer :  [30, 10]
Train Score : 90.797%
Test Score : 85.167%

<b>Please recommend additional way to improve !! </b>




