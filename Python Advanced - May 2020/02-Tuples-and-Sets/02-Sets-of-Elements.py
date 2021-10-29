n, m = list(map(int, input().split()))

n_set = set()
m_set = set()

for i in range(n):
    numbers = int(input())
    n_set.add(numbers)

for _ in range(m):
    numbers = int(input())
    m_set.add(numbers)

intersection = n_set.intersection(m_set)

[print(x) for x in intersection]
