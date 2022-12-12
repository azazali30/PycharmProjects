arr = []


def insert(num):
    arr.append(num)
    swim(len(arr) - 1)


def swim(i):
    parent = int((i - 1) / 2)
    while parent >= 0 and arr[parent] > arr[i]:
        exch(parent, i)
        i = parent
        parent = int((i - 1) / 2)


def sink(i):
    smaller_child = i * 2 + 1
    while smaller_child < len(arr):
        if arr[smaller_child] > arr[smaller_child + 1]:
            smaller_child += 1
        if arr[smaller_child] > arr[i]:
            exch(smaller_child, i)
        i = smaller_child


def del_min():
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr.pop(0)
    arr[0] = arr.pop(len(arr) - 1)
    sink(0)


def exch(s, d):
    tmp = arr[s]
    arr[s] = arr[d]
    arr[d] = tmp


def display():
    print(arr)


while True:
    num = int(input("Choose an option: 1. insert 2. display 3.delmin\n"))
    if num == 1:
        insert(int(input("Enter new entry:")))
    elif num == 2:
        display()
    elif num == 3:
        print(del_min())
