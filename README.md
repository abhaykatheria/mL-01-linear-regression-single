# mL-01-linear-regreassion-single


In this project i have created a linear regression model to predict the salary of a given person depending upon their age of experience.
I had an option of using scikit learn but i always wanted to do it from scratch.

The first step in any machine learning model is to prepare data. Pandas is the library which grants us an immense power when it comes to data preprocessing and data divison.

Using sample method, I have shuffled the data set, iloc method is used to create separate test and train data. 
So I have divided the program in 4 parts: one is the pilot part and other are four methods.
costfun(): this is made to calculate the error function j for given t_1,t_0.
grad1 is function made to calculate the gradient wrt t_1
and similiarly grad_0 is made for t_0.

FUTURE SCOPE and CURRENT SHORT COMINGS

This code is bit incomplete although it's predicting efficiently but we had very clean and short data and only one feature
as more features and train set increases, we will need to adopt mini batching or stochastic linear regression.

Do check out this project and try to make your own code.

Cheers have a good one.
