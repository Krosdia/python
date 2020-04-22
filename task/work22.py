
def read_file():
    L = []
    try:
        f = open("e:/input.txt","rt")
        while True:
            s = f.readline()
            if not s:
                f.close()
                return L
            s = s.rstrip()
            L.append(s)
    except IOError:
        print("Open Error.")
#格式化输出
def print_file(L):
    print(L)
    for id,s in enumerate(L,1):
        print("第{}行: {}".format(id,s))
def main():
    print_file(read_file())
main()
