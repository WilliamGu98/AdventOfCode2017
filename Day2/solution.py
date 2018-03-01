def fileToMatrix(fileName):
    with open(fileName,'r') as f:
        matrix = []
        for line in f:
            row = []
            numbers = line.split()
            for num in numbers:
                row.append(int(num))
            matrix.append(row)
    return matrix

def solution1(matrix):
    check_sum = 0
    for row in matrix:
        smallest = row[0]
        largest = row[0]
        for num in row:
            if num<smallest:
                smallest = num
            if num>largest:
                largest=num
        diff = largest - smallest;
        check_sum += diff
    return check_sum

def solution2(matrix):
    check_sum = 0
    for row in matrix:
        larger = 1;
        smaller = 1;
        class Found(Exception): pass
        try:
            for i in range(len(row)):
                 for j in range(i+1,len(row)):
                    if (row[i]%row[j]==0):
                        larger = row[i]
                        smaller = row[j]
                        raise Found
                    elif (row[j]%row[i]==0):
                        larger = row[j]
                        smaller = row[i]
                        raise Found
        except Found:
            check_sum += larger/smaller
    return check_sum

def main():
    matrix = fileToMatrix('checksum.txt')

    testM = [[5,9,2,8],[9,4,7,3],[3,8,6,5]]

    print(solution1(testM))
    print(solution1(matrix))

    print(solution2(testM))
    print(solution2(matrix))

if __name__ == "__main__":
    main()