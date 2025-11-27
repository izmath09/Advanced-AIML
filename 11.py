import time
from collections import deque
W, H = 5, 5
obstacles = {(1, 1), (2, 4), (3, 4)}
tasks = {(0, 2), (2, 1), (3, 0)}
agent = (0, 0)
def bfs(s, g):
q = deque([(s, [s])])
seen = {s}
while q:
(x, y), path = q.popleft()
if (x, y) == g:
return path
for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
nx, ny = x + dx, y + dy
if 0 <= nx < W and 0 <= ny < H and (nx, ny) not in obstacles and (nx, ny) not in seen:
seen.add((nx, ny))
q.append(((nx, ny), path + [(nx, ny)]))
def show():
print("\n".join(" ".join(
"A" if (x, y) == agent else
"T" if (x, y) in tasks else
"X" if (x, y) in obstacles else
"." for x in range(W)) for y in range(H)))
print()
time.sleep(1)
print("Initial Board")
show()
while tasks:
# Find the closest reachable task
valid_paths = [(bfs(agent, t), t) for t in tasks if bfs(agent, t) is not None]
if not valid_paths:
print("No reachable tasks left.")
break
path, goal = min(valid_paths, key=lambda p: len(p[0]))

# Move along the path
for step in path[1:]:
agent = step
show()
print(f"Picked task at {goal}\n")
tasks.remove(goal)
