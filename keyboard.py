# ID: 68130852
import sys

ALLOWER_CHAR = ['.', '1', '2', '3', '4',
                '5', '6', '7', '8',  '9']
NUMBER_LINES = 4
NUMBER_SYMBOLS = 4


def read_input():
    """Принимает и обрабатывает вводные данные."""
    k: int = int(input())
    list_line: list = []
    for i in range(NUMBER_LINES):
        line: str = sys.stdin.readline().rstrip()
        if len(line) != NUMBER_SYMBOLS:
            raise ValueError(
                'Количество символов в строке '
                f'должно равняться {NUMBER_SYMBOLS}'
            )
        for symbol in line:
            if symbol not in ALLOWER_CHAR:
                raise ValueError(f'Введен недопустимый символ: {symbol}')
            list_line.append(symbol)
    return k, list_line


def get_points(list_line: list, k: int) -> int:
    """Возвращает количество набранных баллов."""
    points: int = 0
    set_line: set = set(list_line)
    set_line.discard('.')
    for i in set_line:
        counter: int = 0
        for j in range(len(list_line)):
            if i == list_line[j]:
                counter += 1
        if counter <= (2 * k):
            points += 1
    return points


def main() -> None:
    k, list_line = read_input()
    points: int = get_points(list_line, k)
    print(points)


if __name__ == '__main__':
    main()
