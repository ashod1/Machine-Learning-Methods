import numpy as np
import pylab as plt
import random
from sklearn.neighbors import KDTree

n=100

x=np.ones([n,2])
EW=np.zeros(n)
for i in range(n):
    x[i,1]=i
    EW[i]=x[i,1]+np.random.normal(0,3)
#EW=np.loadtxt("test.txt",delimiter=',')

theta=[]
i_working=[]
nl=5 # nearest neighbor number

tree=KDTree(x[:,:])
dist, ind=tree.query(x[:,:],k=nl)
W=np.zeros([n,nl,nl])
X=np.zeros([n,nl,x.shape[1]])
Y=np.zeros([n,nl,1])
for j in range(nl):
    W[:,j,j]=1/dist[:,j]**2
    X[:,j,:]=x[ind[:,j],:]
    Y[:,j,0]=EW[ind[:,j]]
W[:,0,0]=W[:,1,1]   
theta=np.zeros([n,x.shape[1],1])
a1=np.zeros([n,x.shape[1],1])
a2=np.zeros([n,x.shape[1],x.shape[1]])
for ii in range(n):
    a1[ii,:,:]=np.matmul(X[ii,:,:].transpose(),np.matmul(W[ii,:,:],Y[ii,:,:]))
    a2[ii,:,:]=np.matmul(X[ii,:,:].transpose(),np.matmul(W[ii,:,:],X[ii,:,:]))
    theta[ii,:,:]=np.matmul(np.linalg.inv(a2[ii,:,:]),a1[ii,:,:])
            
y_test=np.zeros(n)
for i in range(n):
    y_test[i]=np.matmul(theta[i,:,:].transpose(),x[i,:])


### A slower way of doing it without a tree

# for i in range(n):
#     w=np.zeros(n)
#     for j in range(n):
#         if j!=i:
#             distance=np.linalg.norm(x[i,:]-x[j,:])**2
#             w[j]=1/distance
#             if 1/distance!=1/distance:
#                 print(i,j)
#     w[i]=max(w)
#     w_sorted=np.sort(w)
#     w_sorted = w_sorted[::-1]
#     positions_nbrs=np.argsort(w)
#     positions_nbrs=positions_nbrs[::-1]
#     # if w_sorted[nl-1]<1:
#     #     continue 
#     i_working.append(i)
#     W=np.zeros([nl,nl])
#     X=np.zeros([nl,x.shape[1]])
#     Y=np.zeros([nl,1])
#     for j in range(nl):
#         W[j,j]=w[positions_nbrs[j]]
#         X[j,:]=x[positions_nbrs[j],:]
#         Y[j,:]=EW[positions_nbrs[j]]
#     a1=np.matmul(X.transpose(),np.matmul(W,Y))
#     a2=np.matmul(X.transpose(),np.matmul(W,X))
#     theta1=np.matmul(np.linalg.inv(a2),a1)
#     theta.append(theta1)
    
# print(len(i_working))

# y_test=np.zeros(n)
# for i in range(n):
#     y_test[i]=np.matmul(theta[i].transpose(),x[i_working[i],:])

plt.figure(2)
plt.plot(x[:,1],EW,'*')
plt.plot(x[:,1],y_test)