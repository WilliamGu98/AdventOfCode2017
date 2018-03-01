import numpy


def solution1(input):
    if input==1:
        return 0
    square = 1
    while ((square)**2<input): #sets square to min possible square higher then input
        square += 2
    base_steps = square-1 #represents furthest possible number of steps in the 'loop'
    squared = square**2
    prev_squared = (square-2)**2
    #the distance between input and the closest corner is the # of steps we can subtract from base_steps
    dist_to_corner = (input-prev_squared)%int((squared-prev_squared)/4)
    if (((squared-prev_squared)/4)-dist_to_corner < dist_to_corner):
        dist_to_corner = int((squared-prev_squared)/4 - dist_to_corner)
    return base_steps - dist_to_corner


def solution2(input):
    val = 0
    x = 50
    y = 50
    matrix = numpy.zeros((100,100))
    matrix[y][x] = 1 #starting value
    curr_direction = 0  # 0 right, 1 up, 2 left, 3 down

    while (val<=input):
        #move x and y values
        if curr_direction==0:
            x+=1
        elif curr_direction==1:
            y+=1
        elif curr_direction==2:
            x-=1
        elif curr_direction==3:
            y-=1

        val = matrix[y][x+1] + matrix[y][x-1] + matrix[y+1][x] + matrix[y-1][x] +\
             matrix[y+1][x+1] + matrix[y+1][x-1] + matrix[y-1][x-1] + matrix[y-1][x+1] #Calculate surrounding values
        matrix[y][x] = val

        #Turn direction if necc
        if curr_direction==0 and matrix[y+1][x]==0.0: #if matrix value to "left" of curr direction is 0, change directions
            curr_direction=1
        elif curr_direction==1 and matrix[y][x-1]==0.0:
            curr_direction=2
        elif curr_direction==2 and matrix[y-1][x]==0.0:
            curr_direction=3
        elif curr_direction==3 and matrix[y][x+1]==0.0:
            curr_direction = 0
        print("")

    return val


def main():

    print(solution1(1))
    print(solution1(12))
    print(solution1(23))
    print(solution1(1024))
    print(solution1(289326))

    #print(solution2(1))
    #print(solution2(2))
    #print(solution2(3))
    print(solution2(289326))


if __name__ == "__main__":
    main()