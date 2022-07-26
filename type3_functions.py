'''
syntax:
    def fname():
        statement block
        return val1,val2,....,valn
    var=fname()
'''

'''
#1. wap to find the sum of individual digits in a given number.
def individual_digits():
    n=int(input('enter the number'))
    s=0
    while n>0:
        ld=n%10
        s=s+ld
        n=n//10
    return s
print(individual_digits())
'''

'''
#2. wap to find the sum of ASCII values of all the numbers present inside a given string.
def ascii_val():
    st=input('enter any string')
    i=0
    sum=0
    while i<len(st):
        if '0'<=st[i]<='9':
            sum=sum+ord(st[i])
        i=i+1
    return sum
print(ascii_val())
'''

'''
#3.wap to extract all the integer values along with the number of digits in a
#heterogeneous list collection.
def list():
    l=[497,'hai',1463,4.63]
    out=[]
    for i in l:
        if type(i)==int:
            c=0
            t=i
            while t!=0:
                c+=1
                t=t//10
            out+=[(i,c)]
    return out
print(list())
'''

'''
#4.wap to find the sum of length of all the collection datatype present inside
#a given heterogeneous list.
def list_len():
    l=[1,'hai',[1,2,3],{'hello'},{'a':100,'b':200}]
    sum=0
    for i in l:
        if type(i) in [str,list,tuple,set,dict]:
            for j in i:
                sum+=1
    return sum
print(list_len())
'''

'''
#5.wap to extract all the even integer numbers present at odd index in a tuple.
def tuple():
    t=(1,4,'963',[9,6],4,6,'hai')
    out=()
    for i in range(len(t)):
        if i%2!=0 and type(t[i])==int and t[i]%2==0:
            out+=(t[i],)
    return out
print(tuple())
'''
                
