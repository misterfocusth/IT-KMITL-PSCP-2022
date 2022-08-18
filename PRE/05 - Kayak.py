"""[Pre] Kayak / https://ejudge.it.kmitl.ac.th/problem/8101"""


def main():
    """Main Functions"""
    count, weight = int(input()), [int(x) for x in input().split(" ")]
    result, kayak_count = 0, count - 1
    for _ in range(2):
        weight.remove(max(weight))
    for weight_idx in range(0, len(weight), 2):
        if kayak_count == 0:
            break
        result += (weight[weight_idx]) - (weight[weight_idx + 1])
        kayak_count -= 1
    print(abs(result))


main()
