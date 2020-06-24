def edit_distance(source, target):
    table = [
        [0 for i in range(len(target) + 1)]
        for j in range(len(source) + 1)]

    for i in range(len(source) + 1):
        for j in range(len(target) + 1):
            if i == 0:
                table[i][j] = j
            elif j == 0:
                table[i][j] = i

            elif source[i-1] == target[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = 1 + min(
                    table[i-1][j-1], table[i][j-1], table[i-1][j])

    return table[-1][-1]


def test(source, target, output):
    print("Pass" if output == edit_distance(source, target) else "Fail")


if __name__ == "__main__":
    submit = 0
    if submit:
        print(edit_distance(input(), input()))

    else:
        test("short", "ports", 3)
        test("ab", "ab", 0)
        test("editing", "distance", 5)
