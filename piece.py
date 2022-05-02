import sys

def read_input():
    long_street = int(input())
    line_pieces= sys.stdin.readline().rstrip()
    list_pieces = list(map(int, line_pieces.split()))
    return list_pieces

def get_empty_pieces(list_pieces):
    empty_pieces = []
    for i in range(len(list_pieces)):
        if list_pieces[i] == 0:
            empty_pieces.append(i)
    return empty_pieces

def get_distance_to_empty(list_pieces, empty_pieces):
    a = len(list_pieces)
    distance_to_empty = [a]*a
    for empty_piece in empty_pieces:
        for piece in range(len(list_pieces)):
            distance = abs(empty_piece - piece)
            if distance_to_empty[piece] > distance:
                distance_to_empty[piece] = distance
    return distance_to_empty

def main():
    list_pieces = read_input()
    empty_pieces = get_empty_pieces(list_pieces)
    distance_to_empty = get_distance_to_empty(
        list_pieces, empty_pieces
    )
    print(' '.join(list(map(str, distance_to_empty))))

if __name__ == "__main__":
    main()
