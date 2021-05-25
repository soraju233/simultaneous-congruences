# 商と余りと割られる数の保存先
qlist =[]
rlist =[]
wlist =[]


print("[a,b][x]   [e]")
print("[c,d][y] ≡ [f] (mod n)")

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
d = int(input("d="))
e = int(input("e="))
f = int(input("f="))
n = int(input("n="))
print()

m = (a*d - b*c) % n #行列式の計算

s = m
t = n #値の保存


r = s #とりあえず余りとしてaをおく
i = 0 #式の番号

#ユークリッドの互除法----------
print("ユークリッドの互除法")
while(r != 0 ):
    q = s // t
    r = s % t
    # 商と余りを式の番号ごとに保存
    qlist.append(q)
    rlist.append(r)
    wlist.append(s)
    
    print("(",i,")",s,"=",t,"x",q,"+",r)

    s = t
    t = r
    i += 1
print()
print("GCD=",s)
print()
#-------------------------

#一次不定方程式------------
i = i - 2

q = qlist[i]
r = rlist[i]
bq = qlist[i-1] #前の式の商
br = rlist[i-1] #前の式の余り
w = wlist[i] #割られる数
bw = wlist[i-1] #前の式の割られる数

k = r #値の保存
v = q = -q
j = 1

print("一次不定方程式")
print("(",i,")","より")
print(r,"=",w,"+",br,"x","(",q,")")
print()

while(i > 0):
    q = qlist[i]
    r = rlist[i]
    bq = qlist[i-1]
    br = rlist[i-1]
    w = wlist[i]
    bw = wlist[i-1]
    
    print("(",i-1,")","を代入")
    
    bq = -bq #移項
    
    print("　","=",w,"x",j,"+","(",bw,"+",w,"x",bq,")","x",v)
    
    h = v #値の入れ替え
    v = j + bq * v
    k = q #値の入れ替え
    j = h #値の入れ替え

    print("　","=",bw,"x","(",j,")","+",w,"x",v)   
    print()

    i = i-1
#-------------------------
print()
print("x ≡",j,"(mod",n,")" )
print()
print()

h = a #値の保存
a = d * j % n
b = -b * j % n
c = -c * j % n
d = h * j % n

print(n,"を法とした逆行列は")
print("[",a,",",b,"]")
print("[",c,",",d,"]","(mod",n,")")
print()
print()

x = (a * e + b * f) % n
y = (c * e + d * f) % n

print("[x] ","[",x,"]")
print("[y]≡","[",y,"]","(mod ",n,")")
