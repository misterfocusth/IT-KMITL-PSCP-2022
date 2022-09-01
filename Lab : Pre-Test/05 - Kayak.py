"""[Pre] Kayak / https://ejudge.it.kmitl.ac.th/problem/8101"""


def main():
    """Main Functions"""
    _, weight_list = int(input()), [int(x) for x in input().split(" ")]
    weight_diff = []
    min_diff, new_diff = 0, 0
    removal_index = [0, 0]
    while len(weight_list) != 2:
        for x in range(0, len(weight_list) - 1):
            for i in range(1, len(weight_list) - 1):
                if i == 0:
                    min_diff = weight_list[x] - weight_list[i]
                    new_diff = min_diff
                else:
                    min_diff = weight_list[x] - weight_list[i]

            if new_diff < min_diff:
                min_diff = new_diff
                removal_index[1] = i
                removal_index[0] = x

        weight_diff.append(min_diff)
        weight_list.pop(removal_index[0])
        weight_list.pop(removal_index[1])

        print(weight_list)
        print(weight_diff)
    return print(str(int(sum(weight_diff))))


main()
