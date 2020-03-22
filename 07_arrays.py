def print_rev_order(myarr):
    n = len(arr)

    A = []
    for i in range(n - 1, -1, -1):

        A.append(myarr[i])
    for j in A:
        print(j, end=' ')


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print_rev_order(arr)
