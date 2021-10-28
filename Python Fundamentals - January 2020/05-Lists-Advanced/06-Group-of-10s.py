import math

nums = list(map(int, input().split(', ')))
max_num = max(nums)
groups_count = math.ceil(max_num / 10)

for group in range(1, groups_count + 1):
    groups_count = [num for num in nums if group * 10 - 10 < num <= group * 10]
    print(f"Group of {group * 10}'s: {groups_count}")
