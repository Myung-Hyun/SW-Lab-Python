#The prime-counting function is the function counting the number of prime numbers less than or equal to some positive integet  n.
#We usually call the function by  π(n) .

'''
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
'''

n=100000

def Eratosthenes(n):
  number = list(range(n+1)) #[0,1,2, ... n]
  isprime = list(range(n+1)) #1이면 소수(파이썬에서는 False는 0, True는 1) 이 list를 따로 만들어주는 것이 핵심. 코드를 이해하기 쉽게 해준다.
  primenumbers = []
  for i in number:
    isprime[i] = 1
  isprime[0], isprime[1] = 0, 0
  k=2
  while (k<=n):
    if (isprime[k]):
      primenumbers.append(k) 
      for j in range(2*k,n+1,k):
        isprime[j] = 0
    k += 1
  return primenumbers

def prime_counting_function(n):
  return len(Eratosthenes(n))
    
print(f'pi({n})={prime_counting_function(n)}')

