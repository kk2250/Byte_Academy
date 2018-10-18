i = []
def move_stack(n, start, stop, middle):
    if n == 1:
        i.append('1')
        return
    move_stack(n-1, start, middle, stop)
    base_case(start, stop)
    move_stack(n-1, stop, start, middle)
    i.append('1')
    return len(i)

def base_case(start, stop):
    print('move disk from ' + start + ' to ' + stop)


    # print the moves
    # this is going to be a recursive function

if __name__ == "__main__":
    print(move_stack(8, 'A', 'B', 'C'))

