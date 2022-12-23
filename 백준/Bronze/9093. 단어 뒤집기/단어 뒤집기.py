def run(sentence_number):
    sentence_num = int(sentence_number)
    while sentence_num > 0:
        reverse(input().split(' '))
        print()
        sentence_num -= 1


def reverse(sentence):
    for word in sentence:
        stack = list(word)
        for i in range(len(stack)):
            print(stack.pop(), end='')
        print(" ", end='')


def main():
    run(input())


if __name__ == "__main__":
    main()
