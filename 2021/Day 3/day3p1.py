with open('2021/Day 3/input.txt') as f:
    contents = f.readlines()
    #open file and make it a list

gamma = 0
epsilon = 0
#powercon = gamma * epsilon (but in decimal)


# find each bit in the gamma rate
    # split each binary number into individual digits
    # iterate over each column with a for loop, most common digit 'wins' and is added to gamma (using a string?)
    # add all 'winning' values to gamma rate

#find epsilon rate
    # take gamma rate (binary) and change all 0's to 1's and vice versa

#find power comsumption
    #convert gamma and epsilon from binary to decimal
    #print (decimal)