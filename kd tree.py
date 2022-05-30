import numpy as np
import pylab as plt

n=21
x1=np.random.rand(n)*10
x2=np.random.rand(n)*10

plt.figure(1)
plt.scatter(x1,x2)
plt.axvline(x=np.median(x1))

def med(x):
    return np.sort(x)[int(len(x)/2)]
# x1=np.sort(x1)
# x2=np.sort(x2)
tree_x=[]
tree_x.append([x1,x2])
tree=[]
tree.append([med(x1)])
i=0
number_of_branches=2**i
leftover=len(x1)
tree_pos=[]
while leftover>2:
    for k in range(number_of_branches):
        xl1=[]
        xr1=[]
        xl2=[]
        xr2=[]
        for j in range(len(tree_x[i][i%2])):
            if tree_x[i][i%2+2*k][j]<tree[i][k]:
                xl1.append(tree_x[i][0+2*k][j])
                xl2.append(tree_x[i][1+2*k][j])
            elif tree_x[i][i%2+2*k][j]>tree[i][k]:
                xr1.append(tree_x[i][0+2*k][j])
                xr2.append(tree_x[i][1+2*k][j])
        
        tree_x.append([xl1,xl2,xr1,xr2])
        tree.append([med(tree_x[i+1+k][(i+1)%2]),med(tree_x[i+1+k][(i+1)%2+2])])
        
    leftover=len(tree_x[i+1][0])
    i+=1
    number_of_branches=2**i
    if i==2:
        leftover=1
xl1=[]
xr1=[]
xl2=[]
xr2=[]
for i in range(n):
    if x1[i]<tree[0]:
        xl1.append(x1[i])
        xl2.append(x2[i])
    elif x1[i]>tree[0]:
        xr1.append(x1[i])
        xr2.append(x2[i])

plt.figure(1)
plt.plot(np.linspace(0,tree[0][0]),med(xl2)*np.ones(50),'r')
plt.plot(np.linspace(tree[0][0],10),med(xr2)*np.ones(50),'k')
plt.xlim([0,10])
# plt.axhline(y=med(xl2),xmin=0,xmax=tree[0][0]/10,color='r')
# plt.axhline(y=med(xr2),xmin=tree[0][0]/10,xmax=10,color='k')