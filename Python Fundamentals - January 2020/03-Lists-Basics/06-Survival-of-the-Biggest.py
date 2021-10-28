numbers = input().split()
n = int(input())

int_list = [int(i) for i in numbers]

for i in range(n):
    min_element = min(int_list)
    int_list.remove(min_element)

print(int_list)

