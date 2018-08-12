import random

def CoinFlip(iteration):
    #this function does a coin flip the number
    #of times the user has requested --> iteration
    result = {'heads':0,'tails':0}

    for i in range(iteration):
        flip = random.randint(0,1)
        if flip == 0:
            result['heads'] += 1
        else:
            result['tails'] += 1

    print("We're done, here are your results")    
    return result

print("We are going to do a coin flip")
num = int(input("how many times do you want to flip the coin ? "))

print(CoinFlip(num))