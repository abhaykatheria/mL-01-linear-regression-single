# Simple Linear Regression
#@author-Abhay Katheria

#IN THIS CODE I HAVE USED Xdum as dummy variable as i dont want to change the 
#main training set we convert the then formed n.nd array to list for easier operations 







# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#HERE WE DEFINED THE COST FUNCTION 
def costfun(t_0,t_1,Xtrain,ytrain,m):
        Xdum = Xtrain
        Xdum = [i * t_1 for i in Xdum]
        Xdum = [i + t_0 for i in Xdum]
        j = 0
        for i in range(20):
            j = j + ((1/(2*m))*((Xdum[i]-ytrain[i])**2))
            return j
        
# i have formed two functions to calculate the partial derivatives of cost function wrt t_0 and t_1
def grad1(t_0,t_1,m,Xtrain,ytrain):
        Xdum = Xtrain
        Xdum = [i * t_1 for i in Xdum]
        Xdum = [i + t_0 for i in Xdum]
        G1 = 0
        for i in range(20):
            G1 = G1 + ((1/m)*((Xdum[i]-ytrain[i])))
        return G1
            

def grad0(t_0,t_1,m,Xtrain,ytrain):
        Xdum = Xtrain
        Xdum = [i * t_1 for i in Xdum]
        Xdum = [i + t_0 for i in Xdum]
        G0 = 0
        for i in range(20):
            G0 = G0 + ((1/m)*((Xdum[i]-ytrain[i])))
        return G0
            
def regressor(Xtrain,ytrain):
        #INTIALISING PARAMETERS
        t_0 = 0
        t_1 = 0
        a = 0.05 #LEARING RATE MUST BE WITHIN 0.01-0.1
        m= 30 # BATCH SIZE
        
        for i in range(400):
            #here the magic happens a simple yet so powerful piece of code
            #REFER TO ANDREW NG VIDEOS FOR PROPER EXPLANATION
            t_0 = t_0 - ( a*(grad0(t_0,t_1,m,Xtrain,ytrain)))
            temp0 = t_0
            t_1 = t_1 - (a*(grad1(t_0,t_1,m,Xtrain,ytrain)))
            temp1 = t_1
            t_0 = temp0
            t_1 = temp1
      
        x = np.linspace(0,20,100) #NUMPY LINSPACE FUNCTION IS USED TO CREATE 100 EQUALLY SPACED POINTS BETWEEN 0-20
        y = t_0 + t_1*x  # this is our hypothesis t_1 and _0 are parameters
        plt.scatter(Xtest, ytest, color = 'red')#plotting a scatter graph to visualise and compare our predictions
        plt.plot(x, y, '-r', label='y = t_0 + t_1*x')#plotting our predicted hypothesis
        #usual matplotlib stuff
        plt.title('Graph of y = t_0 + t_1*x')
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        plt.show()
         

    

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
#the sorted data was randomised using pandas samle function
dataset = dataset.sample(n=29)
#preparing training sets and test sets for regression
Xtrain=dataset.iloc[0:20,:-1].values#extracting trai data 
Xtrain = [row[0] for row in Xtrain]#convertng numpy n dimensional array into simple list cuz they are awesome
ytrain =dataset.iloc[0:20,1:2].values
ytrain = [row[0] for row in ytrain ]#convertng numpy n dimensional array into simple list cuz they are awesome
#extracting test data,, we dont need to convert this into list as we dont have to erform any operation on it
Xtest=dataset.iloc[20:30,:-1].values
ytest=dataset.iloc[20:30,1:2].values

regressor(Xtrain,ytrain)


