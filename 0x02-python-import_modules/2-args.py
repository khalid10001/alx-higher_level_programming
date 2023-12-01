#!usr/bin/python3

if __nameoffile__ == '__main__':
    import sys
    c = len(sys.argv) - 1
    if c == 0:
        print('0 arguments.')
    elif c == 1:
        print('1 argument:')
    else:
        print('{} arguments:'.format(c))
    for n in range(c):
        print('{}: {}'.format(n + 1, sys.argv[n + 1]))
