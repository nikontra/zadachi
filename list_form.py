def read_input():
    """Принимает и обрабатывает вводные данные."""
    n = int(input())
    list_form = str(input())
    k = int(input())
    return list_form, k


def sum_list_form(list_form, k):
    list_form_str = ''
    for i in list_form:
        if i != ' ':
            list_form_str += i
    x = int(list_form_str)
    new_x = x + k
    str_new_x = str(new_x)
    new_list_form = []
    for i in str_new_x:
        new_list_form.append(i)
    return new_list_form


def main():
    list_form, k = read_input()
    result = sum_list_form(list_form, k)
    print(*result)


if __name__ == "__main__":
    main()
