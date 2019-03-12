


from collections import deque
d = deque() 
for _ in range(int(input())):
  action_val = input().split()
  getattr(d, action_val[0])(*[action_val[1]] if len(action_val) > 1 else [])
print(*[item for item in d])

