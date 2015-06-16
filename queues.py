from collections import deque 
queue = deque(["Eric", "John", "Mitch"])
queue.append("Terry")
queue.append("Greg")

queue.popleft()

queue.popleft()

print queue
