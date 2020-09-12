#The prime-counting function is the function counting the number of prime numbers less than or equal to some positive integet  n.
#We usually call the function by  π(n) .


def Eratosthenes(n):
  a=list(range(2,n+1))  # 2,3,4, ... n
  b=[]                  # save prime 
  p=2
  i=1

  while p*p <= n:  #p^2 greater than n
    while i*p<=n:
      a.remove(i*p)
      i = i+1
    b.append(p)
    p=a[0]
  b=a+b  
  return b

if __name__ == "__main__":
  print(len(Eratosthenes(10)))


