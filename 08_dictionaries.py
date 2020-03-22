
x = int(input())
my_dict = {}
for i in range(x):
    k_v = input()
    k = k_v.split()[0]
    v = k_v.split()[1]
    #print("key :", k)
    #print("value :", v)
    my_dict[k] = v  # append key and value to dict


try:
    a_lst = []          # Start with empty list
    while True:
        a_str = input()
        if not a_str:   # Exit on empty string.
            break
        a_lst.append(a_str)
except EOFError as e:
    print(end="")


for new in a_lst:
    if new in my_dict:
        my_val = my_dict.get(new)
        print(new + "=" + str(my_val))
    if new not in my_dict:
        print("Not found")
