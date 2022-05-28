class StackBracket:
    def __init__(self) -> None:
        self.brackets = []

    def push(self, bracket):
        self.brackets.append(bracket)

    def pop(self):
        self.brackets.pop()


def is_correct_bracket_seq(line):
    stack_brackets = StackBracket()
    for bracket in line:
        if (
            (bracket == ')' or bracket == ']' or bracket == '}')
            and len(stack_brackets.brackets) == 0
             ):
            return False
        elif (
            bracket == ')' and stack_brackets.brackets[-1] == '('
            or bracket == ']' and stack_brackets.brackets[-1] == '['
            or bracket == '}' and stack_brackets.brackets[-1] == '{'
             ):
            stack_brackets.pop()
        else:
            stack_brackets.push(bracket)
    if len(stack_brackets.brackets) == 0:
        return True
    return False


def main():
    line = str(input())
    print(is_correct_bracket_seq(line))


if __name__ == "__main__":
    main()
