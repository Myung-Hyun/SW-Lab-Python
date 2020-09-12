#https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

import math

a_0=1
a_1=0
b_0=1/math.sqrt(2)
b_1=0
t=1/4
p=1
result=0  #pi

def calculate_pi(n):
  for i in range(1,n+1):
    global a_0,a_1,b_0,b_1,t,p

    a_1=(a_0+b_0)/2
    b_1=math.sqrt(a_0*b_0)
    t=t-p*math.pow((a_0-a_1),2)
    p=2*p

    result=math.pow((a_1+b_1),2)/(4*t)
    
    a_0=a_1
    b_0=b_1
  return result

if __name__ == "__main__":
  print(calculate_pi(3))
