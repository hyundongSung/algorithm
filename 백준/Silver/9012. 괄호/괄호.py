def find_pair(stack):
    if "(" not in stack:
        return False
    stack.pop()
    return True


def check(test_case):
    stack = []
    for paren in test_case:
        if paren == ")":
            if not find_pair(stack):
                return False
            continue
        stack.append(paren)
    if stack:
        return False
    return True


def run(testcase_number):
    while testcase_number > 0:
        if check(input()):
            print("YES")
        else:
            print("NO")
        testcase_number -= 1


def main():
    run(int(input()))


if __name__ == "__main__":
    main()
