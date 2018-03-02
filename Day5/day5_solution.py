def file_to_list(fileName):
    with open(fileName,'r') as f:
        num_list = []
        for line in f:
            for num in line.split():
                num_list.append(int(num))
    return num_list


def list_jump(list_nums):
    i = 0
    counter = 0
    while i>=0 and i<len(list_nums):
        curr = list_nums[i]
        if (list_nums[i]>=3):
            list_nums[i]-=1
        else:
            list_nums[i]+=1
        i += curr
        counter+=1
    return counter


def main():
    test = [0,3,0,1,-3]
    num_list = file_to_list("listvalues.txt")
    print(list_jump(test))
    print(list_jump(num_list))


if __name__ == "__main__":
    main()