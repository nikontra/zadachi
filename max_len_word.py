import sys

def main():
    num_symbol = int(input())
    line = sys.stdin.readline().rstrip()
    word_list = line.split()
    max_len_word = 0
    max_word = ''
    for word in word_list:
        len_word = len(word)
        if len_word > max_len_word:
            max_len_word = len_word
            max_word = word
    
    print(f'{max_word} \n{max_len_word}')

if __name__ == "__main__":
    main()
