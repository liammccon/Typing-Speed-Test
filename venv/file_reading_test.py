def main():
    f = open('phrases_to_type.txt')
    for line in f:
        if line[0: 1] == '#' :
            continue
        else: print(line.rstrip())

    if banana:
        print('yes')
    else: print('no')
if __name__=='__main__': main()