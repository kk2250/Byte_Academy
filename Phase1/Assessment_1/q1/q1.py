def move_zeros(num_list):
    a = []
    for _ in range(len(num_list)-1, -1, -1):
        if num_list[_] == 0:
            a.append(num_list[_])
        else:
            a.insert(0, num_list[_])
    return a

def move_zeros1(num_list):
    for _ in range(0, len(num_list)):
        if num_list[_] == 0:
            for __ in range(_, len(num_list)-1):
                num_list[__],num_list[__+1] = num_list[__+1],num_list[__]
    return num_list

x = [0, 1, 0, 3, 5, 0, 10, 4, 0, 12]

if __name__ == '__main__':
    print(move_zeros1(x))