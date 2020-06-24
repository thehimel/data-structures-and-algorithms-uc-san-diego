import sys


def optimal_sequence(n):
    sequence = []
    optimal_num = dynamic_optimal(n)

    while n >= 1:
        sequence = sequence + [n]

        if n % 3 == 0 and optimal_num[n//3 - 1] + 1 == optimal_num[n-1]:
            n //= 3

        elif n % 2 == 0 and optimal_num[n//2 - 1] + 1 == optimal_num[n-1]:
            n //= 2

        else:
            n -= 1

    return reversed(sequence)


def get_min(x, y, z):
    if x == -1:
        return get_min(z + 1, y, z)
    if y == -1:
        return get_min(x, z + 1, z)
    else:
        return min(x, y, z)


def dynamic_optimal(n):
    optimal_num = [0 for _ in range(n)]

    for i in range(2, n+1):
        first, second, third = -1, -1, -1

        if i % 3 == 0:
            third = optimal_num[i//3 - 1]

        if i % 2 == 0:
            second = optimal_num[i//2 - 1]

        first = optimal_num[i - 1 - 1]
        optimal_num[i - 1] = get_min(first, second, third) + 1

    return optimal_num


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
