x=1.2
N=25
k=1
s=x
sign=1.0
from sympy import*

while k<N:
      sign=-sign
      k=k+2
      term=sign*x**k/factorial(k)
      s=s+term

print 'sin(%g)=%g (approximation with %d terms)' %(x,s,N)
