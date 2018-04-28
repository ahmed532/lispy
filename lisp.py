from parse import read

def leval(l):
    return l

def lprint(l):
    print(l)

def loop(f):
    while True:
        f()

def main():
    loop(lambda:lprint(leval(read())))

if __name__ == '__main__':
    main()


