coin = [500,100,50,1]

def a(w, c):
    s = 0
    for i in c:
        s += (w // i)
        w = w % i
    print(s)
a(4720,coin)