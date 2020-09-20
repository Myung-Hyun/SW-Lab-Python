#Eigenvalues of real matrices
#In general, the eigenvalues of real square matrices are complex

import numpy as np

count=0

for i in range(1000):
  A=np.random.rand(100,100) #실행할 때마다 달라진다. 
  D, Q = np.linalg.eig(A) # D가 eigen value, Q가 eigen vector
  DD = np.imag(D) 
  if np.linalg.norm(DD,2)<10e-12:
    count=count+1

print(count) # 결과가 0이고, 1000번의 경우 모두 허수부가 존재함을 알 수 있다. 


#Eigenvalues of real symmetric matrices
#In general, the eigenvalues of real symmetric matrices are always real.

for i in range(1000):
  A=np.random.rand(100,100) #실행할 때마다 달라진다. 
  A=A+A.T #symmetrix matrix
  D, Q = np.linalg.eig(A) # D가 eigen value, Q가 eigen vector
  DD = np.imag(D) 
  if np.linalg.norm(DD,2)<10e-12:
    count=count+1

print(count) # 결과가 1000이고, 1000번의 경우 모두 허수부가 존재하지 않음을 알 수 있다.

#Eigenvectors of real symmetric matrices
#orthonormal (orthogonal and normal) basis

A=np.random.rand(1000,1000)
A=A+A.T #symmetrix matrix
D, Q = np.linalg.eig(A)

print(np.max(abs(np.eye(1000)-Q.T@Q)))  #결과가 3.1366768991208938e-12로 매우 작고, 두 행렬이 같다는 것을 알 수 있다. 



