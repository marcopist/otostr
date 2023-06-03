#from sample.jack import a

a = 2

def play(x):
    global a
    print("a was equal to", a)
    a += 100
    print("Now a is equal to", a)
    return x