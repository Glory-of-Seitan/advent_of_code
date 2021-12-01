with open('2021/Day 1/input.txt') as f:
    contents = f.readlines()
    #open file and make it a list

    prev = 100000
    total = 0
    a = 0
    i = 1
    l = 2
    #set starting values

    for line in contents:
    #beginning of 'for' loop
        

        abbi = int(contents[a])
        ilana = int(contents[i])
        lincoln = int(contents[l])

        depav = (abbi+ilana+lincoln)


        if prev < depav:
            total = total +1

        prev = depav

        if l+1 == len(contents):
            break

        a = a+1
        i = i+1
        l = l+1


    print(total)
