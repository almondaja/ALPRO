class StackQueue:
    def __init__(self):
        self.stack = []
        self.queue = []

    def push(self, item):
        self.stack.append(item)
        print(f"Item {item} ditambahkan ke stack.")

    def pop(self):
        if self.is_stack_empty():
            print("Stack kosong, tidak dapat pop.")
            return None
        return self.stack.pop()

    def peek_stack(self):
        if self.is_stack_empty():
            print("Stack kosong.")
            return None
        return self.stack[-1]

    def is_stack_empty(self):
        return len(self.stack) == 0

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Item {item} ditambahkan ke queue.")

    def dequeue(self):
        if self.is_queue_empty():
            print("Queue kosong, tidak dapat dequeue.")
            return None
        return self.queue.pop(0)

    def peek_queue(self):
        if self.is_queue_empty():
            print("Queue kosong.")
            return None
        return self.queue[0]

    def is_queue_empty(self):
        return len(self.queue) == 0


sq = StackQueue()

sq.push(10)
sq.push(20)
sq.push(30)
print(f"Pop dari stack: {sq.pop()}")
print(f"Peek stack: {sq.peek_stack()}")

sq.enqueue(100)
sq.enqueue(200)
sq.enqueue(300)
print(f"Dequeue dari queue: {sq.dequeue()}")
print(f"Peek queue: {sq.peek_queue()}")
