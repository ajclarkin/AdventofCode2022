# test sort

l = [4,2,5,8,6,1,3,7,9]

counter = True
while counter:
    counter = False
    for k, v in enumerate(l):
        if k+1 < len(l):
            print('key', k)
            print(f'Value {v}, {l[k+1]}')
            if v > l[k+1]:
                print(f'We shoud swap {v} and {l[k+1]}')
                temp = l.pop(k)
                l.insert(k+1, temp)
                counter = True

    print(l)