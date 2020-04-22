def input_L():
    L = []
    while True:
        s = input('>>>')
        if not s:
            return L
        L.append(s)
def write_file(L):
    try:
        f = open("e:/input.txt","w")
        for x in L:
            f.write(x)
            f.write('\n')
        f.close()
    except IOError:
        print("write error;")
