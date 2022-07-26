'''
syntax:
       def fname(args):
           statement block
           return val1,val2,...valn
        print(fname(args))
'''
'''
#1.wap to count the number of prime numbers m and n.
def prime(m,n):
    c=0
    for i in range(m,n+1):
        if i==1:
            continue
        else:
            for j in range(2,n+1):
                if i%j==0 and i==j:
                    c+=1
                elif i%j==0:
                    break
    return c
m,n=int(input('enter any number:')),int(input('enter any number:'))
print(prime(m,n))
'''
'''
#2.wap to count number of vowels ,if i/p-->['harry','potter'],o/p-->[1,2]
def vowels(l):
    out=[]
    for i in l:
        c=0
        for j in i:
            if j in 'AEIOUaeiou':
                c+=1
        out+=[c]
    return out
l=['harry','potter']
print(vowels(l))
'''

'''
#3. if st='aabacbdabdcc', o/p='a4b3c3d2'
def occurance(st):
    out=''
    for i in st:
        if i not in out:
            c=0
            for j in st:
                if j==i:
                    c+=1
            out+=i+str(c)
    return out
st='aabacbdabdcc'
print(occurance(st))
'''
'''
#4.wap to extract all the integer values along with the number of digits
#in a heterogenous list collection
def int_val(l):
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
l=[497,'hai',1463,4.63]
print(int_val(l))
'''

'''
#5.wap to extract all key value pairs in a dict, only if values is of
#mutable datatype and key is of svdt.
def dict(d):
    out={}
    for i in d:
        if type(d[i])in[list,set,dict]and type(i)in[int,float,complex,bool]:
            out[i]=d[i]
    return out
d={1:'one','two':[2,3,4],4+3j:{4,3}}
print(dict(d))
'''
    

