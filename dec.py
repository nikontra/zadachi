#  ID: 68486970
from typing import Union


class DequeRingBuffer():
    """Описывает кольцевой буфер и его методы."""

    def __init__(self, n: int) -> None:
        """Создает буфер заданного размера."""
        self.__max_n: int = n
        self.__deque: list = [None] * n
        self.__head: int = 0
        self.__tail: int = 0
        self.__size: int = 0

    def is_empty(self) -> bool:
        """Проверяет пустой ли буфер."""
        return self.__size == 0

    def push_back(self, x: int) -> None:
        """Добавляет элемент сзади."""
        if self.__size == self.__max_n:
            raise BufferError('error')
        self.__deque[self.__tail] = x
        self.__tail = (self.__tail + 1) % self.__max_n
        self.__size += 1

    def push_front(self, x: int) -> None:
        """Добавляет элемент спереди."""
        if self.__size == self.__max_n:
            raise BufferError('error')
        self.__head -= 1
        if self.__head < 0:
            self.__head = self.__max_n - 1
        self.__deque[self.__head] = x
        self.__size += 1

    def pop_front(self) -> Union[int, str]:
        """Возвращает элемент спереди."""
        if self.is_empty():
            raise BufferError('error')
        x: int = self.__deque[self.__head]
        self.__deque[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_n
        self.__size -= 1
        return x

    def pop_back(self) -> Union[int, str]:
        """Возвращает элемент сзади"""
        if self.is_empty():
            raise BufferError('error')
        self.__tail -= 1
        if self.__tail < 0:
            self.__tail = self.__max_n - 1
        x: int = self.__deque[self.__tail]
        self.__deque[self.__tail] = None
        self.__size -= 1
        return x


def read_input() -> Union[int, list]:
    """Принимает и обрабатывает вводные данные."""
    num_command: int = int(input())
    max_size: int = int(input())
    commands: list = []
    for command in range(num_command):
        command: str = input()
        commands.append(command)

    return max_size, commands


def stack_operations(max_size: int, commands: list) -> None:
    """Выполняет операции с кольцевым буфером."""
    deq: DequeRingBuffer = DequeRingBuffer(max_size)
    for command in commands:
        list_command: list = command.split()
        try:
            if len(list_command) > 1:
                getattr(deq, list_command[0])(list_command[1])
            else:
                print(getattr(deq, list_command[0])())
        except BufferError as error:
            print(error)


def main() -> None:
    max_size, commands = read_input()
    stack_operations(max_size, commands)


if __name__ == '__main__':
    main()
