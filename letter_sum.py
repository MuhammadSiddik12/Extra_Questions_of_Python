def alphabet_position(text):
    dictt = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8',
    'i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17',
    'r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}
    arr = []
    new_text = text.lower()
    for i in list(new_text):
        for k, j in dictt.items():
            if k == i:
                return int(j)
def letter():
    d=[]
    c=[]
    dic={}
    a=input('Enter a alphatbets:').split()
    for i in a:
        b=[]
        for j in i:
            b.append(alphabet_position(j))
        c.append(b)
    for i in c:
        s=sum(i)
        d.append(s)
    for j,i in zip(a,d):
        dic[j]=i
    print(dict_sort(dic))

def dict_sort(d):
    dict_={}
    key_=list(d.keys())
    value_=list(d.values())
    for i in range(len(value_)):
        for j in range(i,len(value_)):
            if value_[i]>value_[j]:
                value_[i],value_[j]=value_[j],value_[i]
                key_[i],key_[j]=key_[j],key_[i]
    for i in range(len(key_)):
        dict_[key_[i]]=value_[i]
    return dict_
letter()