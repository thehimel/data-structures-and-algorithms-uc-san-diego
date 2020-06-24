import sys


def optimal_sequence(n):
    sequence = []

    while n >= 1:
        sequence.append(n)

        if n % 3 == 0 or (n-1) % 3 == 0:
            if n % 3 == 0:
                n = n // 3
            else:
                n = n-1
        elif n % 2 == 0 or (n-1) % 2 == 0:
            if n % 2 == 0:
                n = n // 2
            else:
                n = n-1
        else:
            n = n - 1

    return reversed(sequence)


def test(n):
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
    print('\n')


if __name__ == '__main__':
    submit = 0

    if submit:
        input = sys.stdin.read()
        n = int(input)
        sequence = list(optimal_sequence(n))
        print(len(sequence) - 1)
        for x in sequence:
            print(x, end=' ')

    else:
        test(96234)
        test(5)
        test(1)
