#1.i/p--->st='what is your name'
#o/p---->[4,2,4,4]
'''
#type1:
def string():
    st='what is your name'
    out=[]
    l=st.split()
    for i in l:
        out+=[len(i)]
    print(out)
string()
'''
'''
#type2:
def string(st):
    out=[]
    l=st.split()
    for i in l:
        out+=[len(i)]
    print(out)
st='what is your name'
string(st)
'''
'''
#type3:
def string():
    st='what is your name'
    out=[]
    l=st.split()
    for i in l:
        out+=[len(i)]
    return out
print(string())
 '''
'''
#type4:
def string(st):
     out=[]
     l=st.split()
     for i in l:
         out+=[len(i)]
     return out
st='what is your name'
print(string(st))
'''
#====================================================================

#wap to extract all key value pairs from the dictionary only if value
#is of string data type.
'''
#type1:
def dict():
    d={1:'one','two':2,3:3,'four':'four'}
    out={}
    for i in d:
        if type(d[i])==str:
            out[i]=d[i]
    print(out)
dict()
'''
'''
#type2:
def dict(d):
    out={}
    for i in d:
        if type(d[i])==str:
            out[i]=d[i]
    print(out)
d={1:'one','two':2,3:3,'four':'four'}
dict(d)
'''
'''
#type3:
def dict():
    d={1:'one','two':2,3:3,'four':'four'}
    out={}
    for i in d:
        if type(d[i])==str:
            out[i]=d[i]
    return out
print(dict())
'''
'''
#type4:
def dict(d):
    out={}
    for i in d:
        if type(d[i])==str:
            out[i]=d[i]
    print(out)
d={1:'one','two':2,3:3,'four':'four'}
dict(d)
'''    

    
    
