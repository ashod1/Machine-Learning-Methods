import numpy as np
import pylab as plt
import random

n=100

x=np.ones([n,2])
#EW=np.zeros(n)
for i in range(n):
    x[i,1]=i
    #EW[i]=x[i,1]+np.random.normal(0,3)
EW=np.loadtxt("test.txt",delimiter=',')

theta=[]
i_working=[]
nl=50 # nearest neighbor number
# for i in range(10):
#     w=[]
#     for j in range(n):
#         if j!=i:
#             distance=np.linalg.norm(x[i,:]-x[j,:])**2
#             w.append(1/distance)
#             if 1/distance!=1/distance:
#                 print(i,j)
#     #w.append(max(w))
#     w_sorted=np.array(w)
#     w_sorted=np.sort(w_sorted)
#     w_sorted = w_sorted[::-1]
#     # if w_sorted[nl-1]<1:
#     #     continue 
#     i_working.append(i)
#     positions_nbrs=np.zeros(nl,int)
#     W=np.zeros([nl,nl])
#     X=np.zeros([nl,x.shape[1]])
#     Y=np.zeros([nl,1])
#     for j in range(nl):
#         positions_nbrs[j]=np.where(w==w_sorted[j])[0][0]
#         W[j,j]=w[positions_nbrs[j]]
#         X[j,:]=x[positions_nbrs[j],:]
#         Y[j,:]=EW[positions_nbrs[j]]
#     a1=np.matmul(X.transpose(),np.matmul(W,Y))
#     a2=np.matmul(X.transpose(),np.matmul(W,X))
#     theta1=np.matmul(np.linalg.inv(a2),a1)
#     theta.append(theta1)

for i in range(n):
    w=np.zeros(n)
    for j in range(n):
        if j!=i:
            distance=np.linalg.norm(x[i,:]-x[j,:])**2
            w[j]=1/distance
            if 1/distance!=1/distance:
                print(i,j)
    w[i]=max(w)
    w_sorted=np.sort(w)
    w_sorted = w_sorted[::-1]
    positions_nbrs=np.argsort(w)
    positions_nbrs=positions_nbrs[::-1]
    # if w_sorted[nl-1]<1:
    #     continue 
    i_working.append(i)
    W=np.zeros([nl,nl])
    X=np.zeros([nl,x.shape[1]])
    Y=np.zeros([nl,1])
    for j in range(nl):
        W[j,j]=w[positions_nbrs[j]]
        X[j,:]=x[positions_nbrs[j],:]
        Y[j,:]=EW[positions_nbrs[j]]
    a1=np.matmul(X.transpose(),np.matmul(W,Y))
    a2=np.matmul(X.transpose(),np.matmul(W,X))
    theta1=np.matmul(np.linalg.inv(a2),a1)
    theta.append(theta1)
    
print(len(i_working))

y_test=np.zeros(n)
for i in range(n):
    y_test[i]=np.matmul(theta[i].transpose(),x[i_working[i],:])

plt.figure(2)
#plt.plot(x[:,1],EW,'*')
plt.plot(x[:,1],y_test)