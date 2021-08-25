q = [0] * 10
front = -1
rear = -1

rear += 1
q[rear] = 1 # enqueue(1)

rear += 1
q[rear] = 2

rear += 1
q[rear] = 3

while front != rear:
    front += 1
    print(q[front], end=' ')


# enqueue -> append
# dequeue -> popleft


