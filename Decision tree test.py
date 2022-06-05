import numpy as np
import pylab as plt
import random
from sklearn.neighbors import KDTree
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

n=100

x=np.zeros(n)
y=np.zeros(n)
for i in range(n):
    x[i]=i
    y[i]=x[i]+np.random.normal(0,3)
#EW=np.loadtxt("test.txt",delimiter=',')

### Split into training and validation
x_train, x_val, y_train, y_val = train_test_split(x, y, random_state = 0)

model=DecisionTreeRegressor()
model.fit(x_train.reshape(-1,1),y_train.reshape(-1,1))

y_test=model.predict(x_val.reshape(-1,1))
I=mean_squared_error(y_test,y_val)

plt.figure(1)
plt.plot(x_val,y_val,'*',color='r')
plt.plot(x_val,y_test,'*')


## Overfitting

# model=DecisionTreeRegressor()
# model.fit(x.reshape(-1,1),y)

# x_test=np.linspace(0,100,1000)
# y_test=model.predict(x_test.reshape(-1,1))

# plt.figure(2)
# plt.plot(x,y,'*')
# plt.plot(x_test,y_test)