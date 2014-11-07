def sqrtBI(x, epsilon):
  
    low = 0
    high = max(x, 1.0)
    ## high = x
    guess = (low + high)/2.0
    counter = 1
    while (abs(guess ** 2 - x) > epsilon) and (counter <= 100):
        if guess ** 2 < x:
            low = guess
        else :
            high = guess
        guess = (low + high)/2.0
        counter += 1
    return guess

print sqrtBI(5,0.000001)