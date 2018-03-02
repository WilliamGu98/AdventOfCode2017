def file_to_list(fileName):
    with open(fileName,'r') as f:
        num_list = []
        for line in f:
            for num in line.split():
                num_list.append(int(num))
    return num_list


def reallocate(banks):
    states = [(banks[:])] #holds history of bank states
    counter = 0
    while True:
        redistribute(banks)
        counter+=1
        for state in states: #Check current state against all past states
            if state==banks:
                return counter
        states.append(banks[:])


def redistribute(banks):
    max_val = max(banks)
    i_max = banks.index(max_val)
    banks[i_max] = 0
    while max_val > 0:
        i_max+=1
        banks[(i_max)%len(banks)]+=1
        max_val-=1
    return banks


def count_cycle_len(banks):
    states = [(banks[:])] #holds history of bank states
    counter = 0
    while True:
        redistribute(banks)
        counter+=1
        for state in states: #Check current state against all past states
            if state == banks:
                return counter - states.index(banks)
        states.append(banks[:])


def main():
    test = [0,2,7,0]
    banks = file_to_list("bank.txt")
    print(reallocate(test))
    print(reallocate(banks))
    print(count_cycle_len(test))
    print(count_cycle_len(banks))


if __name__ == "__main__":
    main()