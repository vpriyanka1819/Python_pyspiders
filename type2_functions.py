'''
syntax:
      def fname(args):

          statement block
      fname(args)
       
'''
'''
#1.wap to count the number of digits in a given number.
def no_digits(n):
    count=0
    while n>0:
        count=count+1
        n=n//10
n=int(input('enter any number:'))
no_digits(n)
'''
'''
#2.wap to print the individual digits in a given number.
def individual_digit(n):
    t=n
    while n>=1:
        ld=n%10
        print(ld)
        n=n//10
    print(n)
n=int(input('enter number:'))
individual_digit(n)
'''

'''
#3.wap to remove the duplicate values from a given string.
def duplicate(st):
    out=''
    i=0
    while i<len(st):
        if st[i] not in out:
            out+=st[i]
        i=i+1
    print(out)
st=input('enter any string:')
duplicate(st)
'''
'''
#4.wap to check whether the given number is armstrong number or not.
def armstrong(n):
    s=0
    st=str(n)
    d=len(st)
    for i in st:
        st+=int(i)**d
    if s==n:
        print('armstrong number')
    else:
        print('not an armstrong number')
n=int(input('enter any number:'))
armstrong(n)
'''
'''
#5.wap to find even factors of a given number.
def even_fact(n):
    for i in range(1,n+1):
        if i%2==0 and n%i==0:
            print(i)
n=int(input('enter the number:'))
even_fact(n)
'''
        
    
