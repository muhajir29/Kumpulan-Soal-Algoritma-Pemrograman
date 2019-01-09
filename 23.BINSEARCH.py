n = int(input())
listn = input().split()
x = int(input())


def binary_search(x, listn):
    first = 0
    last = len(listn)
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if int(listn[midpoint]) == x:
            found = True
            return midpoint
        else:
            if x < int(listn[midpoint]):
                last = midpoint - 1
            else:
                first = midpoint + 1
    if found == False:
        return -1


print(binary_search(x, listn))