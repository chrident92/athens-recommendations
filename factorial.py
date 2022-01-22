#factotial=n*(n-1)*(n-2)..*1

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
x=int(input('give a number'))          

if __name__=="__main__":
  def  main(x):
    f=factorial(x)
    print(f)

main(x)

##factorial generator

def factorialGenerator(n):
    fact=1
    b=1
    if n==0:
        fact=1
    elif n>0:
        while b<n:
            fact=fact*b
            b+=1
        yield fact
x=int(input('Give number'))
for n in range(0,x):
    f=factorialGenerator(n)
        
