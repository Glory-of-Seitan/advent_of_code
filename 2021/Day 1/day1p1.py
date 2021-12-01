with open('2021/Day 1/input.txt') as f:
    contents = f.readlines()
    #open file and make it a list

    prev = 100000
    total = 0
    #set starting values

    for line in contents:
    #beginning of 'for' loop

        depmeas = int(line)
        #set the depth to an integer
        

        if prev < depmeas:
            total = total +1

        prev = depmeas

    print(total)




        


        





#for num in contents:
    #print(num)
    #print(contents)
