### Gievn Question is

Imagine you have a dataset where you have different Instagram features

like u sername , Caption , Hashtag , Followers , Time_Since_posted , and likes , now your task is

to predict the number of likes and Time Since posted and the rest of the features are

your input features. Now you have to build a model which can predict the

number of likes and Time Since posted.


#### install all the dependencies and create virtual environment
`
conda create -p venv python==3.8
`

### install all the libraries 

`
pip install -r requirements.txt
`

#### solution 

The model is trained on the given dataset in which we have to build a model for predicting the **No. of likes**
and **No. of Time since posted**

The model is build with 99.9% accuracy and the best fitted model is **Lasso Regression**

even **XG-Boost** failed to give the accuracy of 11%

The code is present in

`
notebook/EDA.ipynb

notebook/Model_training.ipynb
`

The Build model is present in 
`artifacts/likes_model.pkl

artifacts/time_since_posted.pkl
`