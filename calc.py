#  ID: 68487005
import operator
import sys

OPERATION: dict = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}


class StackCalc():
    """Класс описывающий стек и его методы."""

    def __init__(self) -> None:
        """Создает список стека"""
        self.__stack: list = []

    def push(self, x: int) -> None:
        """Добавляет элемент в конец стека."""
        self.__stack.append(x)

    def pop(self) -> int:
        """Возвращает последний элемент стека."""
        return self.__stack.pop()


def read_input() -> list:
    """Принимает и обрабатывает вводные данные."""
    line: str = sys.stdin.readline().rstrip()
    for char in line:
        if (not char.isnumeric()
                and char not in OPERATION.keys()
                and char != ' '):
            raise ValueError(f'Введен не допустимый символ {char}')
    return line.split()


def calculator(elements: list) -> int:
    """Производит математические действия с элементами стека."""
    calc: StackCalc = StackCalc()
    for elem in elements:
        operation = OPERATION.get(elem)
        if operation:
            elem_last: int = calc.pop()
            elem_prev_last: int = calc.pop()
            calc.push(operation(elem_prev_last, elem_last))
        else:
            calc.push(int(elem))

    return calc._StackCalc__stack.pop()


def main() -> None:
    elements: list = read_input()
    print(calculator(elements))


if __name__ == '__main__':
    main()
