# Enter your code here. Read input from STDIN. Print output to STDOUT


x = int(input())

s_list = []
for i in range(x):
    a = input()
    s_list.append(a)

for my_str in s_list:
    even_list = []  # 0 2 4
    odd_list = []
    curr_len = len(my_str)
    for j in range(curr_len):
        if j % 2 == 0:
            even_list.append(my_str[j])
        else:
            odd_list.append(my_str[j])
    # we have 2 lists
    even_str = ""
    odd_str = ""
    for e in even_list:
        even_str += e

    for o in odd_list:
        odd_str += o
    print(even_str + " " + odd_str)


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
