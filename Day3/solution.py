def solution1(input):
    if (input==1):
        return 0

    square = 1
    while ((square)**2<input): #sets square to min possible square higher then input
        square += 2

    base_steps = square-1 #represents furthest possible number of steps in the 'loop'
    squared = square**2
    prev_squared = (square-2)**2
    #the distance between input and the closest corner is the # of steps we can subtract from base_steps
    distToCorner = (input-prev_squared)%int((squared-prev_squared)/4)
    if (((squared-prev_squared)/4)-distToCorner < distToCorner):
        distToCorner = int((squared-prev_squared)/4 - distToCorner)
    return base_steps - distToCorner

def solution2(input):
    counter = 1

def main():
    print(solution1(1))
    print(solution1(12))
    print(solution1(23))
    print(solution1(1024))
    print(solution1(289326))


if __name__ == "__main__":
    main()