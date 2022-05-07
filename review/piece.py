# ID: 68130780
import sys
from math import ceil


def read_input() -> list:
    """Принимает и обрабатывает вводные данные."""
    long_street: int = int(input())
    line_pieces = sys.stdin.readline().rstrip()
    try:
        pieces = list(map(int, line_pieces.split()))
    except ValueError:
        raise ValueError('Номера участков должны быть целыми числами')
    if len(pieces) != long_street:
        raise ValueError('Введите корректное количество участков')
    return pieces


def get_empty_pieces(pieces: list, len_pieces: int) -> list:
    """Возращает список индексов пустых участков."""
    empty_pieces: list = []
    for i in range(len_pieces):
        if not pieces[i]:
            empty_pieces.append(i)
    return empty_pieces


def get_mid_empty(empty_pieces: list, len_empty_pieces: int) -> list:
    """Возвращает список индексов средних участков между пустыми.
    Если количество участков между пустыми четное,
    то запишеться индекс участка выше середины"""
    mid_empty_pieces: list = []*(len_empty_pieces -1)
    for i in range(len_empty_pieces - 1):
        midle = ceil((empty_pieces[i] + empty_pieces[i + 1])/2)
        mid_empty_pieces.append(midle)
    return mid_empty_pieces


def get_distance_to_empty(empty_pieces: list,
                          mid_empty_pieces: list,
                          len_empty_pieces: int,
                          len_pieces: int) -> list:
    """Возвращает список расстояний от участков до ближайших пустых."""
    distance_to_empty: list = []
    if len_empty_pieces == 1:
        for j in range(len_pieces):
            distance = abs(empty_pieces[0] - j)
            distance_to_empty.append(distance)
    else:
        for i in range(len_empty_pieces):
            if i == 0:
                for j in range(0, mid_empty_pieces[i]):
                    distance = abs(empty_pieces[i] - j)
                    distance_to_empty.append(distance)
            elif i == (len_empty_pieces-1):
                for j in range(mid_empty_pieces[i - 1], len_pieces):
                    distance = abs(empty_pieces[i] - j)
                    distance_to_empty.append(distance)
            else:
                for j in range(mid_empty_pieces[i - 1], mid_empty_pieces[i]):
                    distance = abs(empty_pieces[i] - j)
                    distance_to_empty.append(distance)
    return distance_to_empty


def main() -> None:
    pieces: list = read_input()
    len_pieces: int = len(pieces)
    empty_pieces: list = get_empty_pieces(pieces, len_pieces)
    len_empty_pieces: int = len(empty_pieces)
    mid_empty_pieces: list = get_mid_empty(empty_pieces, len_empty_pieces)
    distance_to_empty: list = get_distance_to_empty(empty_pieces,
                                                    mid_empty_pieces,
                                                    len_empty_pieces,
                                                    len_pieces)
    print(* distance_to_empty)


if __name__ == "__main__":
    main()
