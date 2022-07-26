'''
syntax:
       def fname(args):
           statement block
       fname(args)
'''


'''
#1.wap to check middle value is present in a given list is int or not
def middle_value():
    l=[1,2,1.5,4,5]
    if len(l)%2!=0:
        mi=len(l)//2
        if type(l[mi])==int:
            print("integer value")
        else:
            print("not an integer value")
    else:
        print('no middle value')
middle_value()
'''

'''
#2.wap to get the product of all numbers from 1 to n
def number():
    n=int(input("enter the numbers:"))
    i=1
    sum=1
    while i<=n:
        sum=sum*i
        i+=1
    print('the product of all numbers are:',sum)
number()
#logic---> if 3--> 1*2*3=6
'''

'''
#3.wap to replace all spaces by underscore
def underscore():
    st=input('enter a string:')
    out=''
    i=0
    while i<len(st):
        if st[i]==' ':
            out+='_'
        else:
            out+=st[i]
        i=i+1
    print(out)
underscore()
# o/p---> i_love_magic
'''

'''
#4.wap to toggle the given i/p if 'AbCdE', o/p--> 'aBcDe'
def toggle():
    st=input('enter any string:')
    i=0
    result=''
    while i<len(st):
        if 'A'<=st[i]<='Z':
            result+=chr(ord(st[i])+32)
        elif 'a'<=st[i]<='z':
            result+=chr(ord(st[i])-32)
        else:
            result+=st[i]
        i+=1
    print(result)
toggle()
#output-->enter any string:@123ABC&cdef
#@123abc&CDEF
'''

'''
#5.reverse the given string without slicing.
def reverse_str():
    st=input('enter any string:')
    out=''
    for i in st:
        out=i+out
    print(out)
reverse_str()
'''
  

    
