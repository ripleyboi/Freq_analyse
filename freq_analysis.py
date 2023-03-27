import matplotlib.pyplot as plt


#ALPHANUMERIC ONLY
#NO SYMBOLS CAN BE PARSED

#accept encoded string
AnalyseMe = input(">")
CharList = ([*AnalyseMe])

#initialize lists
ticklocs = [0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
ticknames = ['a','b','c','d','e','f','g','h', 'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
I=[]
j=[]
k=[]
l=[]
m=[]
n=[]
o=[]
p=[]
q=[]
r=[]
s=[]
t=[]
u=[]
v=[]
w=[]
x=[]
y=[]
z=[]
one=[]
two=[]
three=[]
four=[]
five=[]
six=[]
seven=[]
eight=[]
nine=[]
zero=[]

#PARSE STRING

for i in CharList:
    if i == "a" or i == "A":
        a.append(i)
    elif i == "b" or i == "B":
        b.append(i)
    elif i == "c" or i == "C":
        c.append(i)
    elif i == "d" or i == "D":
        d.append(i)
    elif i == "e" or i == "E":
        e.append(i)
    elif i == "f" or i == "F":
        f.append(i)
    elif i == "g" or i == "G":
        g.append(i)
    elif i == "h" or i == "H":
        h.append(i)
    elif i == "i" or i == "I":
        I.append(i)
    elif i == "j" or i == "J":
        j.append(i)
    elif i == "k" or i == "K":
        k.append(i)
    elif i == "l" or i == "L":
        l.append(i)
    elif i == "m" or i == "M":
        m.append(i)
    elif i == "n" or i == "N":
        n.append(i)
    elif i == "o" or i == "O":
        o.append(i)
    elif i == "p" or i == "P":
        p.append(i)
    elif i == "q" or i == "Q":
        q.append(i)
    elif i == "r" or i == "R":
        r.append(i)
    elif i == "s" or i == "S":
        s.append(i)
    elif i == "t" or i == "T":
        t.append(i)
    elif i == "u" or i == "U":
        u.append(i)
    elif i == "v" or i == "V":
        v.append(i)
    elif i == "w" or i == "W":
        w.append(i)
    elif i == "x" or i == "X":
        x.append(i)
    elif i == "y" or i == "Y":
        y.append(i)
    elif i == "z" or i == "Z":
        z.append(i)
    elif i == "1":
        one.append(i)
    elif i == "2":
        two.append(i)
    elif i == "3":
        three.append(i)
    elif i == "4":
        four.append(i)
    elif i == "5":
        five.append(i)
    elif i == "6":
        six.append(i)
    elif i == "7":
        seven.append(i)
    elif i == "8":
        eight.append(i)
    elif i == "9":
        nine.append(i)
    elif i == "0":
        zero.append(i)
    else:
        print('character thrown out: ' + i)

#MAKE PLOT
data = [len(a), len(b), len(c), len(d), len(e), len(f), len(g), len(h), len(i), len(j), len(k), len(l), len(m), len(n), len(o), len(p), len(q), len(r), len(s), len(t), len(u), len(v), len(w), len(x), len(y), len(z), len(one), len(two), len(three), len(four), len(five), len(six), len(seven), len(eight), len(nine), len(zero)]

plt.xticks(ticklocs, ticknames)
plt.bar(range(len(data)), data)
plt.title("frequency analysis")
#DISPLAY
plt.show()