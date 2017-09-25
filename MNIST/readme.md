Fashion MNIST Datasets recognition

============
Datasets Source : https://www.kaggle.com/zalando-research/fashionmnist/data

* Title: German Credit data

* Number of Instances: 60,000(train) 10,000(test)

* Number of Classes: 10

* Target : 
CLASSES = { <br>
    '0': 'T-shirt/top',<br>
    '1': 'Trouser',<br>
    '2': 'Pullover',<br>
    '3': 'Dress',<br>
    '4': 'Coat',<br>
    '5': 'Sandal',<br>
    '6': 'Shirt',<br>
    '7': 'Sneaker',<br>
    '8': 'Bag',<br>
    '9': 'Ankle boot'<br>
}<br>
<br>
![sample image](./images/pullover.png) 
<br>
Label : Pullover <br>



—
1st Edition (09/25)
-------------

> Using Tensorflow 
: Layers = [ 784, 100, 100, 10 ] 

: Relu -> Relu -> Softmax 

: AdamOptimizer 

: learning-rate : 0.001

: Epoch Num : 30

: Training Result 

Epoch 25: Cost - 0.3133 Train Acc - 88.59 Test Acc - 86.66<br>
Epoch 26: Cost - 0.3119 Train Acc - 88.70 Test Acc - 86.41<br>
Epoch 27: Cost - 0.3100 Train Acc - 88.41 Test Acc - 86.24<br>
Epoch 28: Cost - 0.3082 Train Acc - 88.45 Test Acc - 86.49<Br>
Epoch 29: Cost - 0.3064 Train Acc - 89.09 Test Acc - 86.78<br>
<br>
![cost & accurary ](./images/0925.png) 
