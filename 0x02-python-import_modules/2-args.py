#!/usr/bin/python3
if __name__=='__main__':
    import sys
    name_script = sys.argv[0]
    argv = sys.argv[1:]
    i = len(argv)
    if i < 1:
        print("0 arguments")
    elif i == 1:
        print("1 argument:")
        print("1: {}".format(argv[0]))
    else:
        print("{} arguments:".format(len(argv)))
        for j in range(len(argv)):
            print("{}: {}".format(j+1, argv[j]))

