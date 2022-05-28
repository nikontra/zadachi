class MyQueueSized:
    def __init__(self, n) -> None:
        self.max_n = n
        self.queue = [None]*n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]


def main():
    num_command = int(input())
    n = int(input())
    queue_sized = MyQueueSized(n)
    list_stack = []
    for command in range(num_command):
        command = str(input())
        list_stack.append(command)
    for command in list_stack:
        if command == 'peek':
            print(queue_sized.peek())
        elif command == 'pop':
            print(queue_sized.pop())
        elif command == 'size':
            print(queue_sized.size)
        else:
            list_command = command.split()
            queue_sized.push(list_command[1])


if __name__ == '__main__':
    main()
