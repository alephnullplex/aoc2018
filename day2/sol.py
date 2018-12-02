from collections import Counter
import editdistance

with open("./input.txt") as input:
    all = [v.strip() for v in input.readlines()]
    all.sort()

    checksum_twos = 0
    checksum_threes = 0

    for id in all:
        c = [v for k,v in Counter(id).items()]
        if 2 in c:
            checksum_twos += 1
        if 3 in c:
            checksum_threes += 1

    print("Checksum: {}".format(checksum_threes * checksum_twos))

    found_edit = None
    for this_one in all:
        for test in all:
            if editdistance.eval(this_one, test) == 1:
                found_edit = (this_one, test)
                break

    a, b = found_edit
    final = "".join([a[i] for i in range(len(a)) if a[i] == b[i]])

    print("Final: ", final)
            
        
                

        
